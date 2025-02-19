import numpy as np

def is_scalar(value):
    """Check if the function output is a scalar."""
    return isinstance(value, (float, int))

def compute_update_scalar(f, J, x0):
    """Compute the Newton-Raphson update for scalar functions."""
    return -f(x0) / J(x0)

def compute_update_vector(f, J, x0):
    """Compute the Newton-Raphson update for vector-valued functions."""
    return -np.linalg.inv(np.array(J(x0))) @ f(x0)

def newton_raphson_scalar(f, J, x0, tol, max_iter):
    """Newton-Raphson method for scalar functions."""
    iter_count = 0
    while np.abs(f(x0)) > tol:
        x0 += compute_update_scalar(f, J, x0)
        iter_count += 1
        if iter_count > max_iter:
            raise ValueError("Solution did not converge within max iterations.")
            Break
    return x0

def newton_raphson_vector(f, J, x0, tol, max_iter):
    """Newton-Raphson method for vector-valued functions."""
    x0 = np.array(x0, dtype=float)
    iter_count = 0
    while np.linalg.norm(f(x0)) > tol:
        x0 += compute_update_vector(f, J, x0)
        iter_count += 1
        if iter_count > max_iter:
            raise ValueError("Solution did not converge within max iterations.")
            Break
    return x0

def newton(f, J, x0, tol, max_iter):
    """Main function to determine which Newton-Raphson method to use."""
    return newton_raphson_scalar(f, J, x0, tol, max_iter) if is_scalar(f(x0)) else newton_raphson_vector(f, J, x0, tol, max_iter)