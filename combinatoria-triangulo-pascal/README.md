# Matemática Computacional: Combinatória e Triângulo de Pascal

## O Projeto
Na computação, o cálculo direto de combinações e coeficientes binomiais através da fórmula de fatoriais $(C_p^n = n! / (p!(n-p)!))$ é ineficiente e altamente propenso a falhas de estouro de memória (*Integer Overflow*), dado o crescimento hiper-rápido da função fatorial. 

Este projeto explora uma solução algorítmica clássica baseada em **Programação Dinâmica**: a construção do Triângulo de Pascal. Ele permite o cálculo de combinações e probabilidades utilizando apenas operações de soma sequenciais, armazenando os estados anteriores para construir os próximos.

## Fundamentação Matemática e Histórica
O trabalho resgata a evolução histórica do algoritmo, que precede Blaise Pascal, tendo sido desenvolvido no século X na Pérsia por Al-Karaji e, posteriormente, por Omar Khayyám e Yang Hui.

Matematicamente, o algoritmo computacional é sustentado pela relação de Stifel:
$X(n+1, p) = X(n, p) + X(n, p-1)$.
Onde qualquer posição no triângulo pode ser calculada somando os dois elementos diretamente acima dela, com a condição base de que os limites do triângulo são sempre $1$.

## Aplicações Práticas
O documento explora a aplicação do modelo para resolução de problemas reais de contagem múltipla, tais como:
1. **Formação de Equipes:** Cálculo de arranjos sem repetição (ex: formar 462 times distintos de 5 pessoas a partir de um grupo de 11).
2. **Probabilidade Discreta:** Considerando que a soma de qualquer linha $n$ do triângulo é igual a $2^n$, o triângulo modela perfeitamente distribuições binomiais (como lançamentos de moedas).
3. **Análise de Erros de Contagem:** Identificação e mitigação de erros lógicos de contagem múltipla ao distinguir artificialmente elementos idênticos em problemas de combinatória.

**[Artigo Teórico (PDF)](./Trabalho_1_MA220.pdf)**
