from newtonsmethod import newtons_method as nm
import numpy as np
import pytest


def f1(x):
    return x - 3
def J1(x):
    return 1

def f2(x):
    return np.array([
        [2*x[0] + x[1] - 5,
         x[0] - x[1]] - 1
    ])
def J2(x):
    return np.array([
        [2, 1],
        [1, -1]
    ])


def test_newtons_method():
    assert np.isclose(nm.newton_raphson(f1, J1, 50, 1e-10, 50), 3.0)
    assert np.isclose(nm.newton_raphson(f2, J2, np.array([50, 20]), 1e-10, 50)[0], 2.0)
    assert np.isclose(nm.newton_raphson(f2, J2, np.array([50, 20]), 1e-10, 50)[1], 1.0)