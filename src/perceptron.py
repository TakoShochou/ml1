import numpy as np

def AND(x1, x2):
    w1, w2, th = 0.5, 0.5, 0.7
    if x1 * w1 + x2 * w2 <= th:
        return 0
    return 1

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-.5, -.5])
    b = 0.7
    if np.sum(x * w) + b <= 0:
        return 0
    return 1

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([.5, .5])
    b = -.2
    if np.sum(x * w) + b <= 0:
        return 0
    return 1

def XOR(x1, x2):
    return AND(
        NAND(x1, x2),
        OR(x1, x2)
    )