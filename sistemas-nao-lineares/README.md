# Sistemas Não-Lineares: Newton vs Gauss-Seidel Adaptado

## O Projeto
Resolução de sistemas de equações não-lineares avaliando a diferença de performance entre o rigor das derivadas e as aproximações iterativas.

## Métodos Analisados
* **Método de Newton para Sistemas:** Exige a construção e inversão da Matriz Jacobiana a cada iteração. Apresenta convergência rápida, mas alto custo computacional por passo.
* **Método de Gauss-Seidel Adaptado:** Resolve iterativamente cada equação do sistema isoladamente (utilizando `fsolve`), usando o resultado de uma variável para atualizar a próxima.

## Resultados
O Método de Newton convergiu para uma tolerância de `1e-14` em apenas 8 iterações, enquanto o Gauss-Seidel adaptado exigiu 13 iterações. Contudo, o Método de Newton perde aplicabilidade em sistemas onde a Matriz Jacobiana não pode ser definida analiticamente.

**[Relatório (PDF)](./Atividade_4_numericos.pdf)**
