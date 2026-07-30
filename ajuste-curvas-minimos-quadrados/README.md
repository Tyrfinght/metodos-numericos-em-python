# Ajuste de Curvas: Método dos Mínimos Quadrados

## O Projeto
A capacidade de traçar tendências a partir de dados dispersos é o núcleo da estatística preditiva e do Machine Learning. Neste projeto, explorei a fundamentação matemática do **Ajuste de Curvas pelo Método dos Mínimos Quadrados**.

O objetivo foi modelar uma série temporal de consumo de energia elétrica residencial (KWh) ao longo de 12 meses, construindo e avaliando diferentes combinações lineares de funções base para encontrar a curva que melhor representasse o padrão dos dados.

##  Abordagem Matemática
Em vez de utilizar bibliotecas de regressão prontas, o problema foi resolvido matricialmente. Construí funções base da forma:
`p(x) = c1*φ1(x) + c2*φ2(x) + c3*φ3(x)`

Para avaliar a melhor aderência aos dados reais, testei múltiplas famílias de funções:
1. **Polinomiais:** Testes variando graus (ex: `x`, `x^2`, `x^3`, `x^4`) para capturar curvaturas.
2. **Senoidais:** Hipótese baseada na sazonalidade natural do consumo de energia ao longo das estações do ano.
3. **Exponenciais:** Para modelar variações agressivas de consumo.

A qualidade de cada modelo foi validada rigorosamente através do cálculo das normas dos resíduos quadráticos.

## Resultados e Análise
A hipótese inicial assumia que a função senoidal teria a melhor performance, dada a lógica periódica das contas de luz. Contudo, a análise de resíduos quadráticos contrariou a intuição inicial: o ajuste exponencial obteve a menor taxa de erro (`4603.2`), superando os modelos polinomiais de alta ordem e o modelo senoidal.

Este resultado evidenciou que a dispersão dos dados da amostra não possuía uma sazonalidade perfeitamente contínua, favorecendo um modelo de crescimento amortecido. O projeto valida a eficácia do cálculo de matrizes para generalizar curvas, sendo a espinha dorsal de algoritmos modernos de regressão.

## Documentação e Códigos
As equações completas, a matriz de resultados e os gráficos de dispersão plotados estão documentados no Whitepaper do projeto.
👉 **[Ler o Relatório (PDF)](./Atividade_6_Numerico.pdf)**
