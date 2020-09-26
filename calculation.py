import numpy as np


def pqsolver(p, q):
    if ((p / 2) ** 2 - q) < 0:
        x1 = -p / 2
        x2 = -p / 2
        return x1, x2
    else:
        x1 = -p / 2 + np.sqrt((p / 2) ** 2 - q)
        x2 = -p / 2 - np.sqrt((p / 2) ** 2 - q)
        return float(x1), float(x2)
