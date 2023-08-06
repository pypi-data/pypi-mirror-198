"""Classes for defining systems.

Systems can compute the exact signature via brute force.

If component types (colours) are not provided, system is considered of single component type.

Systems:
- `System` - base class. Requires structure function definition
- `KMSystem` - K-out-of-M system. Requires the K delimiter of dim == no. of component types.
- `Network` - requires a nx.Graph. Components are the edges and the system functions if all nodes are connected.

"""

# ...

import numpy as np
import matplotlib.pyplot as plt  # type: ignore
import scipy.stats as sts

from collections.abc import Callable, Sequence
from typing import Literal
import numpy.typing as npt

import networkx as nx

from syreal.myutilities import bConfig, getLogger, stateIteratorBin, Progressbar

Vector = npt.NDArray[float]
logger = getLogger("systems")


class System:
    """Specifies system and its structure function."""

    def __init__(
        self,
        N: int,
        fi: Callable[[bConfig], bool],
        colours: Sequence[int] | None = None,
    ):
        """
        Arguments:
            N: system size
            fi: structure function
            colours: component type assignment (len == N),
                                                                        None for single type
        """

        self.N = N
        self.fi = fi
        self.colours = np.array(colours, dtype=int) if colours else None

        ### component types and their counts
        if colours is None:
            self.sc = [0]
            self.nc = 1
            self.M = np.array([N])
        else:
            self.sc = list(set(self.colours))
            self.nc = len(self.sc)
            self.M = np.array([len(self.colours[self.colours == k]) for k in self.sc])

        ## precalc binom coeff
        K = max(self.M)
        bc = np.zeros(K + 1, dtype=float)
        bc[0] = 1

        self.binomCoeff = [None for d in range(self.nc)]

        for i in range(K):
            for j in range(i + 1, 0, -1):
                bc[j] = bc[j] + bc[j - 1]

            for d in range(self.nc):
                if i + 1 == self.M[d]:
                    self.binomCoeff[d] = bc[: i + 2].copy()

    def calc_L(self, x: bConfig) -> list[int]:
        """transforms a state vector into the number of functioning components"""

        # single component type
        if self.nc == 1:
            return [np.sum(x)]

        out = [np.sum(x, where=self.colours == k, dtype=int) for k in self.sc]
        return out

    def pTensor(self, ps: Sequence[float], ns: Sequence[int]):
        """computes probabilities of observing L=l of n for independent samples"""

        K = len(ns)
        binomProbs = []
        for i in range(K):
            distrib = sts.binom(ns[i], ps[i])
            probs = [distrib.pmf(c) for c in range(ns[i] + 1)]
            binomProbs += [probs]

        logger.debug(binomProbs)

        out = 1
        for d in range(K):
            out = np.tensordot(out, binomProbs[d], axes=0)
        return out

    def binomTensor(self) -> npt.NDArray[float]:
        """Computes tensor product representing binom coeffs for each combination of functioning components"""

        bc = self.binomCoeff

        out = 1
        for d in range(self.nc):
            out = np.tensordot(out, bc[d], axes=0)
        return out

    def survival_signature(self) -> npt.NDArray[float]:
        """Computes the survival signature by brute force."""

        w = self.binomTensor()

        counts = np.zeros_like(w, dtype=int)

        bar = Progressbar(
            "computing signature",
            fill="#",
            suffix="remaining: %(remaining)d, eta %(eta)ds",
            max=2**self.N,
        )

        for pos in stateIteratorBin(self.N):
            state = self.fi(pos)
            bar.next()
            if state:
                l = self.calc_L(pos)
                counts[tuple(l)] += 1

        return counts / w


class KMSystem(System):
    def __init__(
        self,
        K: Sequence[int] | int,
        colours: Sequence[int],
    ):
        """K out of M system

        Arguments:
        K ... cutoff (L >= K to function)
        colours ... component types
        """

        def fi(x: bConfig):
            out = True
            l = self.calc_L(x)
            for d in range(self.nc):
                out = out and l[d] >= self.K[d]
            return out

        super().__init__(len(colours), fi, colours)
        self.K = [K] if type(K) is int else K


class Network(System):
    def __init__(
        self,
        g: nx.Graph,
        colours: Sequence[int] = None,
    ):
        """Network system - needs to be connected."""

        def fi(x: bConfig):
            g = self.g
            E = len(g.edges)
            selection = []
            edges = list(g.edges)
            for i in range(E):
                if x[i]:
                    selection += [edges[i]]
            gg = g.edge_subgraph(selection)
            if len(gg) < len(g):
                return False
            return nx.is_connected(gg)

        super().__init__(len(g.edges), fi, colours)
        self.g = g


if __name__ == "__main__":
    ### simple test
    N = 15
    C = 3

    fi = lambda x: np.sum(x) > N / 3
    colours = list(np.random.randint(C, size=N))

    system = System(N, fi, colours=colours)

    ### network test
    g = nx.gnp_random_graph(8, 0.4)
    while not nx.is_connected(g) or len(g.edges) > 16:
        g = nx.gnp_random_graph(len(g.nodes), 0.6)
    print(nx.is_connected(g), "  edges= ", len(g.edges))

    C = 3
    colours = []
    while len(set(colours)) < C:
        colours = np.random.randint(C, size=len(g.edges))

    sys = Network(g, list(colours))
