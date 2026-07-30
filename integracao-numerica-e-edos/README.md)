# Integração Numérica e EDOs: Áreas e Trajetórias Dinâmicas

## O Contexto
Na modelagem matemática aplicada, frequentemente lidamos com funções que não possuem primitivas analíticas ou com sistemas dinâmicos descritos apenas por suas taxas de variação. Esta subpasta agrupa dois trabalhos complementares de Cálculo Numérico que demonstram como os princípios básicos de quadratura (cálculo de área) evoluem para a resolução preditiva de sistemas dinâmicos (EDOs).

---

## Estudo 1: Interpolação e Continuidade (Atividade 7)
Focado na construção de funções polinomiais por partes que garantem não apenas a passagem pelos pontos de dados, mas a suavidade matemática da curva.

###  Abordagem Matemática
* **Problema:** Determinar polinômios $p_1(x)$ e $p_2(x)$ para modelar uma função $s(x)$ nos intervalos $[0, 1]$ e $[1, 2]$[cite: 7].
* **Restrição de Continuidade:** O modelo exigiu e impôs que a derivada $s'(x)$ fosse contínua no ponto de transição, fornecendo a terceira condição para a formulação do sistema[cite: 7]. 
* **Resultado:** O sistema linear foi resolvido analiticamente, resultando em derivadas lineares contínuas de $-2$ e $6x - 8$[cite: 7]. O comportamento foi devidamente validado via plotagem computacional.

---

##  Estudo 2: Resolução de PVI e Regra de Simpson (Atividade 8)
Focado em prever a trajetória de um sistema a partir de um Problema de Valor Inicial (PVI) e calcular o seu acúmulo global sob a curva.

###  Abordagem Matemática e Computacional
* **Solução da EDO:** O sistema dinâmico governado por $y' = (4te^{-t} - 1)y$[cite: 8] foi resolvido numericamente utilizando o solucionador `lsode` (e sua contraparte `odeint` em Python) para projetar a trajetória da curva no tempo[cite: 8].
* **Integração Numérica:** Com a trajetória mapeada iterativamente, o valor da integral $I = \int_{0}^{5} y(t) dt$ foi extraído construindo um algoritmo manual utilizando a **Regra de Simpson**[cite: 8].
* **Análise de Erro e Convergência:** O algoritmo calibrou dinamicamente a malha de pontos (aumentando o número de subintervalos) para atestar que a aproximação numérica da integral atingisse uma precisão rigorosa de 6 casas decimais[cite: 8], lidando diretamente com a tolerância de erro de ponto flutuante da máquina[cite: 8].

---

##  Documentação e Códigos
Os desenvolvimentos matemáticos, as deduções algébricas e os scripts em Python/Octave estão disponíveis nos arquivos oficiais desta pasta:
👉 **[Ler Relatório: Atividade 7 (PDF)](./Atividade_7_Numerico.pdf)**
👉 **[Ler Relatório: Atividade 8 (PDF)](./Atividade_8_Numerico.pdf)**
