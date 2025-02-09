import numpy as np

def newton_raphson(f, J, x0, tol, max_iter):
    
    iter = 0
    if isinstance(f(x0), float) or isinstance(f(x0), int):
        while np.abs(f(x0)) > tol:
            delta_x = -f(x0)/J(x0)
            x0 += delta_x
            iter += 1
            if max_iter < iter:
                print("Solution did not converge with these iterations")
                break
        else:
            return x0
    else:    
        while np.abs(f(x0)[0]) > tol:
            delta_x = -np.linalg.inv(np.array(J(x0))) @ f(x0)
            x0 += delta_x
            iter += 1
            if max_iter < iter:
                print("Solution did not converge with these iterations")
                break
        else:
            return x0