import numpy as np

N = 10000
valor_exato_teorico = np.pi**2 / 8  # Convergência da série infinita

print(f"Valor teórico exato da série: {valor_exato_teorico:.10f}\n")

# 1. ALGORITMO DE SOMA CRESCENTE
soma_crescente = np.float32(0.0)

for k in range(1, N + 1):
    termo = np.float32(1.0 / (2*k - 1)**2)
    soma_crescente += termo

erro_crescente = abs(valor_exato_teorico - soma_crescente)
print("--- ALGORITMO 1: SOMA CRESCENTE ---")
print(f"Resultado Obtido: {soma_crescente:.10f}")
print(f"Erro Absoluto:    {erro_crescente:.4e}\n")

# 2. ALGORITMO DE SOMA DECRESCENTE
soma_decrescente = np.float32(0.0)

for k in range(N, 0, -1):
    termo = np.float32(1.0 / (2*k - 1)**2)
    soma_decrescente += termo

erro_decrescente = abs(valor_exato_teorico - soma_decrescente)
print("--- ALGORITMO 2: SOMA DECRESCENTE ---")
print(f"Resultado Obtido: {soma_decrescente:.10f}")
print(f"Erro Absoluto:    {erro_decrescente:.4e}\n")

# 3. ANÁLISE COMPARATIVA
print("--- ANÁLISE ---")
if erro_decrescente < erro_crescente:
    print("A soma decrescente minimizou a perda de dígitos significativos,")
    print("pois somou valores de grandezas parecidas antes de adicioná-los")
    print("aos termos de maior peso.")