# evidenceSignature/myutilities.py

"""Various helpful utilities to keep by side.

Provides:
- `getLogger` - defines preformatted loggers
- `stateIteratorBin` - to walk through the n-dim hypercube
- `profile` - a profiling function

"""

# ...

import sys
import logging

import numpy as np
from progress.bar import Bar as Progressbar

from typing import Iterator, Callable, Literal
import numpy.typing as npt

bConfig = npt.NDArray[np.bool_]


def getLogger(name=None):
    """Creates a logger, which saves debug into file(name.log) and prints rest into std"""
    # Create a custom logger
    logging.basicConfig(format="%(name)s - %(levelname)s - %(message)s")
    name = __name__ if name is None else name
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    # Create handlers
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler(name + ".log", mode="w")
    c_handler.setLevel(logging.INFO)
    f_handler.setLevel(logging.DEBUG)

    # Create formatters and add it to handlers
    c_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
    f_format = logging.Formatter(
        "%(levelname)s - line:(%(lineno)d) file: %(filename)s :\n%(message)s"
    )
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger


def stateIteratorBin(n: int) -> Iterator[bConfig]:
    """Iterator through all binary combinations."""
    pos = np.zeros(n, dtype=bool)

    while True:
        yield pos.copy()
        if not iterateStatesBin(pos):
            break


def iterateStatesBin(pos):
    """Updates position until finishing."""
    n = len(pos)

    for i in range(n):
        if not pos[i]:
            pos[i] = True
            break

        if i == n - 1:
            return False

    for j in range(i):
        pos[j] = False

    return True


def profile(fnc: Callable, fname=None):
    """runs and profiles (fnc),
    saves results to (fname) if specified, else std

    Arguments:
        fnc: function to be profiled
        fname: file name if the results are to be written into a file
    """

    import cProfile
    from pstats import Stats, SortKey

    # sortby = SortKey.TIME  # CUMULATIVE
    sortby = SortKey.CUMULATIVE
    with cProfile.Profile() as pr:
        fnc()

        if fname:
            with open(fname, "w") as f:
                ps = Stats(pr, stream=f).sort_stats(sortby)
                ps.print_stats()
        else:
            ps = Stats(pr).sort_stats(sortby)


if __name__ == "__main__":
    dim = 5
    for pos in stateIteratorBin(dim):
        print(pos)

    test = "this is something way too long and i would like to see how it behaves on save with enabled automated formatting"

    print("hello")
