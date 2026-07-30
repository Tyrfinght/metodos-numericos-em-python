# =========================================================================
# AJUSTE DE CURVAS: MÉTODO DOS MÍNIMOS QUADRADOS (PYTHON)
# Modelo Exponencial - Consumo de Energia Elétrica
# =========================================================================


import numpy as np
import matplotlib.pyplot as plt


x = np.arange(1, 13).reshape(-1, 1)
y = np.array([140, 220, 150, 170, 190, 180, 170, 160, 180, 200, 170, 199]).reshape(-1, 1)

phi1 = np.exp(-x)
phi2 = np.ones_like(x)
phi3 = np.exp(x)

P = np.hstack((phi1, phi2, phi3))

coeficientes, residuos, rank, s = np.linalg.lstsq(P, y, rcond=None)

c1, c2, c3 = coeficientes.flatten()

y_predito = P @ coeficientes
norma_residuo = np.linalg.norm(y_predito - y)**2
print(f"Resíduo Quadrático (Modelo Exponencial): {norma_residuo:.1f}")

x_continuo = np.linspace(0, 12, 100).reshape(-1, 1)
y_continuo = c1 * np.exp(-x_continuo) + c2 * np.ones_like(x_continuo) + c3 * np.exp(x_continuo)

plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='blue', marker='x', label='Dados Reais', s=80)
plt.plot(x_continuo, y_continuo, color='magenta', label='Ajuste Exponencial')
plt.title('Ajuste de Curvas - Consumo KWh (Mínimos Quadrados)')
plt.xlabel('Mês')
plt.ylabel('Consumo (KWh)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()