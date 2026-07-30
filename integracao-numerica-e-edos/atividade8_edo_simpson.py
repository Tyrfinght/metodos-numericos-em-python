import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def f(y, t):
    return (4 * t * np.exp(-t) - 1) * y

y0 = 2.0 

t_21 = np.linspace(0, 5, 21)
h_21 = t_21[1] - t_21[0]

y_21 = odeint(f, y0, t_21).flatten()

plt.figure(figsize=(8, 5))
plt.plot(t_21, y_21, '.-', color="#1f77b4", markersize=10, linewidth=1)
plt.title("Trajetória do PVI - EDO")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

Qsc_21 = (h_21 / 3) * (y_21[0] + 4 * np.sum(y_21[1:-1:2]) + 2 * np.sum(y_21[2:-2:2]) + y_21[-1])
print(f"Área sob a curva (21 pontos): {Qsc_21:.10f}\n")

print("Calculando erro para alta precisão (6 casas decimais)...")

N1 = 1000001
t_N1 = np.linspace(0, 5, N1)
h_N1 = t_N1[1] - t_N1[0]
y_N1 = odeint(f, y0, t_N1).flatten()
Qsc1 = (h_N1 / 3) * (y_N1[0] + 4 * np.sum(y_N1[1:-1:2]) + 2 * np.sum(y_N1[2:-2:2]) + y_N1[-1])

N2 = 900001
t_N2 = np.linspace(0, 5, N2)
h_N2 = t_N2[1] - t_N2[0]
y_N2 = odeint(f, y0, t_N2).flatten()
Qsc2 = (h_N2 / 3) * (y_N2[0] + 4 * np.sum(y_N2[1:-1:2]) + 2 * np.sum(y_N2[2:-2:2]) + y_N2[-1])

E = abs(Qsc2 - Qsc1)

print(f"Qsc1 (Malha Densa 1): {Qsc1:.15f}")
print(f"Qsc2 (Malha Densa 2): {Qsc2:.15f}")
print(f"Erro E (Diferença):   {E:.15e}")