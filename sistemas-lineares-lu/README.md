# Álgebra Linear Computacional: Sistemas e Decomposição LU

## O Projeto
A resolução de grandes sistemas de equações lineares ($Ax = b$) é uma das operações mais custosas e recorrentes na computação científica e na modelagem financeira. Inverter matrizes diretamente é altamente ineficiente e propenso a erros numéricos catastróficos. 

Neste projeto, explorei a estabilidade de métodos diretos, focando na **Decomposição LU com Pivoteamento Parcial** ($PA = LU$). O objetivo foi decompor matrizes densas e utilizar matrizes triangulares para resolver sistemas e encontrar a matriz inversa com alta precisão, evitando a perda de dígitos significativos.

## Abordagem Matemática e Teste de Estresse
O algoritmo foi submetido a um teste de estresse utilizando matrizes aleatórias densas e a famosa **Matriz de Hilbert**, conhecida por ser extremamente mal condicionada (pequenas perturbações causam grandes erros na solução).

*   **Fatoração:** A matriz original $A$ foi decomposta em uma matriz triangular inferior ($L$) e uma superior ($U$), acompanhada de uma matriz de permutação ($P$) para garantir que o maior pivô fosse utilizado, minimizando erros de arredondamento.
*   **Inversão:** A matriz inversa $A^{-1}$ foi construída iterativamente resolvendo $LUx = Pb$ para cada vetor da base canônica.

## Resultados e Precisão Numérica
A qualidade das soluções foi avaliada pelo cálculo analítico das normas dos resíduos e erros relativos. 
Os resultados demonstraram alta robustez do modelo:
* A precisão na resolução do sistema atingiu a grandeza de erro na escala de 1e-13.
* O cálculo de similaridade da matriz inversa teórica com a computada ($||M - I|| / ||I|| \approx 0$) apresentou um erro mínimo na casa de 1e-15, provando a eficácia do pivoteamento em mitigar a propagação de erros de ponto flutuante, mesmo em condições adversas.

## Documentação e Códigos
A matemática das matrizes, a extração dos valores teóricos e as tabelas comparativas estão no texto do projeto:
**[Ler o Relatório (PDF)](./Atividade_3_Numerico.pdf)**
