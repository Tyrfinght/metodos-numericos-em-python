import numpy as np
import scipy.linalg as la

n = 5 # Dimensão do sistema

np.random.seed(42)
A = np.random.rand(n, n)
H = la.hilbert(n)

e_vec = np.ones((n, 1))
b = A @ e_vec
c = H @ e_vec

P_A, L_A, U_A = la.lu(A)
P_H, L_H, U_H = la.lu(H)

y_A = la.solve_triangular(L_A, P_A.T @ b, lower=True)
x_A = la.solve_triangular(U_A, y_A)

y_H = la.solve_triangular(L_H, P_H.T @ c, lower=True)
x_H = la.solve_triangular(U_H, y_H)

erro_rel_A = np.linalg.norm(A @ x_A - b) / np.linalg.norm(x_A)
erro_rel_H = np.linalg.norm(H @ x_H - c) / np.linalg.norm(x_H)

print(f"Erro Relativo (Matriz A): {erro_rel_A:.4e}")
print(f"Erro Relativo (Matriz de Hilbert): {erro_rel_H:.4e}")

B = np.zeros((n, n))
I = np.eye(n)

for k in range(n):
    y_inv = la.solve_triangular(L_A, P_A.T @ I[:, k], lower=True)
    B[:, k] = la.solve_triangular(U_A, y_inv)

erro_inversa = np.linalg.norm(B - la.inv(A)) / np.linalg.norm(B)
erro_identidade = np.linalg.norm((A @ B) - I) / np.linalg.norm(I)

print(f"\nQualidade da Inversa Computada: {erro_inversa:.4e}")
print(f"Teste A * A^(-1) = I (Erro): {erro_identidade:.4e}")