# Fundamentos do Cálculo Numérico: Erros de Ponto Flutuante

## O Projeto
A matemática contínua pressupõe precisão infinita, mas a computação científica lida com limitações físicas de memória e processamento. O objetivo deste projeto foi explorar as deficiências do Sistema de Ponto Flutuante (SPF) e provar que, em algoritmos computacionais, a ordem das operações afeta diretamente o resultado final devido ao descarte de dígitos significativos.

O experimento utilizou a série matemática finita $S[N]=\sum_{k=1}^{N}\frac{1}{(2k-1)^{2}}$ para avaliar como a propagação de erros absolutos e relativos arruína aproximações em precisão simples.

## Metodologia e Algoritmos
Dois algoritmos opostos foram construídos para calcular o acúmulo da mesma série, buscando atingir um erro na casa de $1\times 10^{-7}$:

1. **Algoritmo de Soma Crescente:** Realiza a iteração na ordem natural, de $k=1$ até $N$.
2. **Algoritmo de Soma Decrescente:** Realiza a soma de forma invertida, partindo do termo $N$ (o menor valor) até o termo $1$ (o maior valor).

## Resultados e Análise Computacional
Os resultados comprovaram a vulnerabilidade do alinhamento de expoentes em processadores padrão:

* **Falha da Soma Crescente:** O erro estacionou em $1\times 10^{-4}$ e não se alterou com novas iterações. Após cerca de 2000 ciclos, a variável `soma` acumulou uma grandeza muito superior à do novo termo calculado por $f(k)$. Isso forçou o truncamento da parcela minúscula, perdendo-se os dígitos significativos e impedindo a convergência.
* **Sucesso da Soma Decrescente:** O segundo algoritmo resolveu o problema puramente por reorganização arquitetural. Ao iniciar a soma pelos menores termos possíveis, garantiu-se que as operações ocorressem sempre entre parcelas de grandezas muito próximas, evitando perdas por alinhamento e alcançando com precisão a tolerância exigida de $1\times 10^{-7}$.

## 📄 Documentação e Códigos
Os detalhes de implementação logarítmica e a plotagem da mitigação do erro estão disponíveis no relatório:
**[Relatório(PDF)](./Atividade_1-Numerico.pdf)**
