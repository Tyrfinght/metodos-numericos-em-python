# Otimização e Sistemas Não-Lineares: Análise de Convergência

## O Projeto
Encontrar raízes e pontos de mínimo em funções não-lineares complexas é o núcleo do treinamento de algoritmos de *Machine Learning*. O objetivo deste projeto foi implementar computacionalmente e comparar a eficiência, o custo e a taxa de convergência de diferentes métodos numéricos iterativos.

## Métodos Analisados
Foram implementados algoritmos clássicos para a resolução de equações e sistemas não-lineares:
* **Método de Newton (Newton-Raphson):** Utiliza derivadas (e a matriz Jacobiana/Hessiana em múltiplas variáveis) para guiar a direção da convergência.
* **Método da Secante:** Uma alternativa computacionalmente mais barata que aproxima a derivada usando pontos iterativos anteriores.
* **Gradiente Descendente:** O padrão-ouro moderno para otimização de Redes Neurais, utilizando passos proporcionais ao gradiente negativo da função.
* **Método de Gauss-Seidel Adaptado:** Testado especificamente para a resolução iterativa de sistemas de equações não-lineares interligadas.

## Teste de Estresse 
Para estressar os algoritmos e testar suas vulnerabilidades a mínimos locais e pontos de sela, o modelo foi testado em funções matemáticas rigorosas de otimização multivariável:
1. **Função Quadrática** (Convergência base)
2. **Função de Rosenbrock** (Problema do "Vale", testando a robustez da convergência)
3. **Função de Rastrigin** (Altamente multimodal)
4. **Função de Styblinski-Tang**

## Resultados e Conclusão
A análise empírica evidenciou os *trade-offs* matemáticos de cada abordagem:
* O **Método de Newton** mostrou-se imbatível em velocidade de convergência (poucas iterações) quando o ponto inicial é adequado e a Hessiana/Derivada pode ser calculada, brilhando na função de Rosenbrock.
* O **Método da Secante** apresentou instabilidade dependendo fortemente dos dois pontos iniciais ("chutes"), oscilando entre alta eficiência e não convergência.
* O **Gradiente Descendente** penalizou o custo computacional com um avanço iterativo muito lento, sendo severamente impactado pelo aumento da dimensionalidade e da precisão exigida.

O estudo prova que aumentar a precisão flutuante (ex: de `1e-7` para `1e-14`) não apenas aumenta o custo linearmente, mas pode inviabilizar métodos que dependem de aproximações sem um *Learning Rate* dinâmico.

## 📄 Relatórios 
As equações, análises de log e gráficos das funções de estresse estão documentados nos relatórios oficiais do projeto:
👉 **[Ler Relatório 1: Otimização Numérica (MS629)](./Projeto_Computacional_MS629.pdf)**
👉 **[Ler Relatório 2: Sistemas Não-Lineares (Newton vs Gauss-Seidel)](./Atividade_4_numericos.pdf)**
