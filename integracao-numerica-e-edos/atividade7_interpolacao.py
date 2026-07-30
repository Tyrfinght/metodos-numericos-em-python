import numpy as np
import matplotlib.pyplot as plt

# 1. Definição dos domínios (intervalos [0, 1] e [1, 2])
x1 = np.arange(0, 1.1, 0.1)
x2 = np.arange(1, 2.1, 0.1)

# 2. Funções das derivadas encontradas analiticamente
def p1_prime(x):
    # Retorna um array de -2 com o mesmo formato de x
    return -2 * np.ones_like(x)

def p2_prime(x):
    # Derivada no segundo intervalo: 6x - 8
    return 6 * x - 8

# 3. Plotagem do gráfico s'(x)
plt.figure(figsize=(8, 5))

# Plotando os pontos discretos como no Octave
plt.plot(x1, p1_prime(x1), '.b', markersize=10, label="p1'(x)")
plt.plot(x2, p2_prime(x2), '.g', markersize=10, label="p2'(x)")

plt.ylim(-4, 4)
plt.xlabel("x")
plt.ylabel("s'(x)")
plt.title("Derivada de s(x)")
plt.legend(loc="upper left")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()