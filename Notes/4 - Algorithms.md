# 4 - Algorithms

Os algoritmos de Machine Learning podem ter vários comportamentos, de entre os quais:

`LD` - Vector de D dimensões que separa os dados em duas classes. Linear Regression; <br>
`DT` - Subdivisão dos dados de forma geométrica, em várias classes. Decision Treee;

## Classifiers

### Simple Linear

Método `LD` que julga duas classes estarem separadas por uma única linha. É simples de configurar e interpretar, mas não é possível usá-lo em dados qualitativos e é sensível a outliers.

### Nearest Neighbors

Dado um objecto, este partilha a classe com o valor vizinho mais próximo. O algoritmo `KNN` é uma generalização deste, com K sendo normalmente um número ímpar, em que se escolhe a classe da maioria dos K vizinhos mais próximos. <br>
No entanto este algoritmo é sensível a atributos irrelevantes e sensível também a classificações efetuadas apenas tendo em conta um subset de features. Além disso, apesar de ser simples de implementar, é difícil de interpretar e é um classificador lento para grandes volumes de dados.

### Decisison Tree

É um método simples de implementar mas é fácil de ocorrer `overfitting` e difícil de escolher os atributos que fazem a divergência de classes. É robusto a anomalias nos dados (outliers, missing values, correlated attributes, irrelevant attributes, scale).

### Naive Bayes

P (c | d) = [P (d | c) * P(c)] / P (d)

> P (c | d) - Probabilidade de d estar na classe c <br>
> P (d | c) - Probabilidade de gerar a instância d dado a classe c <br>
> P (c) - Probabilidade de ocorrência da classe c <br>
> P (d) - Probabilidade de ocorrência da instância d <br>

É robusta a variáveis irrelevantes, rápido a treinar e implementar. Por outro lado assume indendência entre features e não é aplicável a features numéricas.

### Neural Networks

É universal, versátil, online, robusta, rápida quando já se tem o modelo treinado e pode ser produzida em paralelo. Por outro lado é lenta em fase de treino, difícil de interpretar e pouca adaptativa a novas realidades.

### Support Vector Machines (SVM)

Quanto **maior é a margem**, menos risco de overfitting do modelo. Pelo lado positivo, estes métodos são muito maturados, os resultados são independentes das condições iniciais e do número de atributos a testar, e dá para encontrar a *local minima*. Pode-se usar `funções não-lineares` se der para discriminar.