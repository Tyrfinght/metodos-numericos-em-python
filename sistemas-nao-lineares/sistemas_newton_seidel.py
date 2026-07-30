import numpy as np
from scipy.optimize import least_squares


# MÉTODO DE NEWTON
def f(x):
    return np.array([
        x[0]**2 + x[1]**2 - x[2],
        (1/4)*x[0]**2 + (1/9)*x[1]**2 + x[2]**2 - 1,
        x[0] + x[1]
    ])

def j(x):
    return np.array([
        [2*x[0], 2*x[1], -1],
        [(1/2)*x[0], (2/9)*x[1], 2*x[2]],
        [1, 1, 0]
    ])

x0 = np.array([6.0, -6.0, 6.0]) # Ponto inicial
k_newton = 0

while np.linalg.norm(f(x0), np.inf) > 1e-14:
    s = np.linalg.solve(j(x0), -f(x0))
    x0 = x0 + s
    k_newton += 1

print("--- METODO DE NEWTON ---")
print(f"Iterações: {k_newton}")
print(f"Norma do erro: {np.linalg.norm(f(x0), np.inf):.4e}")
print(f"Raiz encontrada:\n{x0}\n")


# MÉTODO DE GAUSS-SEIDEL ADAPTADO
x0_seidel = np.array([6.0, -6.0, 6.0])
k_seidel = 0

def a(x): return np.array([x[0]**2 + x[1]**2 - x[2]])
def b(x): return np.array([(1/4)*x[0]**2 + (1/9)*x[1]**2 + x[2]**2 - 1])
def c(x): return np.array([x[0] + x[1]])

while np.linalg.norm(f(x0_seidel), np.inf) > 1e-14:
    # Usando least_squares para lidar com as equações subdeterminadas (1 eq, 3 vars)
    # da mesma forma que o fsolve atua no Octave.
    x1 = least_squares(a, x0_seidel).x
    x2 = least_squares(b, x1).x
    x3 = least_squares(c, x2).x
    
    x0_seidel = x3
    k_seidel += 1

print("--- METODO DE GAUSS-SEIDEL ADAPTADO ---")
print(f"Iterações: {k_seidel}")
print(f"Norma do erro: {np.linalg.norm(f(x0_seidel), np.inf):.4e}")
print(f"Raiz encontrada:\n{x0_seidel}")