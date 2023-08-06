import numpy as np
from syreal.Systems import System

def main():
    nComponents = 5
    nNecessary = 3
    sys = System(nComponents, lambda x: np.sum(x)>nNecessary)

    print('Hello from syreal!')

if __name__ == '__main__':
    main()