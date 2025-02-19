import numpy as np
from newtonsmethod import newtons_method as nm
import pytest

def test_is_scalar():
    assert nm.is_scalar(5.0) == True
    assert nm.is_scalar(3) == True
    assert nm.is_scalar(np.array([1, 2])) == False

def test_compute_update_scalar():
    f = lambda x: x**2 - 4
    J = lambda x: 2*x
    x0 = 2.0
    assert np.isclose(nm.compute_update_scalar(f, J, x0), 0)

def test_compute_update_vector():
    f = lambda x: np.array([x[0]**2 + x[1] - 2, x[0] + x[1]**2 - 2])
    J = lambda x: np.array([[2*x[0], 1], [1, 2*x[1]]])
    x0 = np.array([1.0, 1.0])
    expected_update = np.linalg.solve(J(x0), -f(x0))
    assert np.allclose(nm.compute_update_vector(f, J, x0), expected_update)

def test_newton_raphson_scalar():
    f = lambda x: x**2 - 4
    J = lambda x: 2*x
    x0 = 3.0
    tol = 1e-6
    max_iter = 100
    root = nm.newton_raphson_scalar(f, J, x0, tol, max_iter)
    assert np.isclose(root, 2.0) or np.isclose(root, -2.0)

def test_newton_raphson_vector():
    f = lambda x: np.array([x[0]**2 + x[1] - 2, x[0] + x[1]**2 - 2])
    J = lambda x: np.array([[2*x[0], 1], [1, 2*x[1]]])
    x0 = np.array([1.0, 1.0])
    tol = 1e-6
    max_iter = 100
    root = nm.newton_raphson_vector(f, J, x0, tol, max_iter)
    expected_root = np.array([1.0, 1.0])
    assert np.allclose(root, expected_root)

def test_newton_raphson():
    # Scalar case
    f_scalar = lambda x: x**2 - 4
    J_scalar = lambda x: 2*x
    x0_scalar = 3.0
    assert np.isclose(nm.newton(f_scalar, J_scalar, x0_scalar, 1e-11, 300), 2.0)
    
    # Vector case
    f_vector = lambda x: np.array([x[0]**2 + x[1] - 2, x[0] + x[1]**2 - 2])
    J_vector = lambda x: np.array([[2*x[0], 1], [1, 2*x[1]]])
    x0_vector = np.array([1.0, 1.0])
    expected_root = np.array([1.0, 1.0])
    assert np.allclose(nm.newton(f_vector, J_vector, x0_vector, 1e-11, 300), expected_root)