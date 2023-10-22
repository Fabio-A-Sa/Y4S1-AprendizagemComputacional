# 3 - Data Classification

## Decision Tree

Um método simples de classificação, binária ou não. Existe subdivisão de valores segundo atributos variados. As principais dificuldades são:
- Que atributos escolher para fazer a divisão?
- Quando parar a divisão, para que a classificação não faça **overfitting**?

## Avaliação

- Através de `matrizes de confusão`, que apresenta os (falsos|verdadeiros) (positivos|negativos). Há algumas fórmulas a saber:

![Confusion Matrix Formulas](../Images/ConfusionMatrix.png)

- `Curva ROC` (*Receiver Operating Characteristic*), para visualização da proporção de true positives por false positives.

![ROC Curve Construction](../Images/ROC.png)