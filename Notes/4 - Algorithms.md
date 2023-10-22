# 4 - Algorithms

Os algoritmos de Machine Learning podem ter vários comportamentos, de entre os quais:

`LD` - Vector de D dimensões que separa os dados em duas classes;
`DT` - Subdivisão dos dados de forma geométrica, em várias classes;

## Some Algorithms

### Simple Linear Classifier

Método `LD` que julga duas classes estarem separadas por uma única linha. É simples de configurar e interpretar, mas não é possível usá-lo em dados qualitativos e é sensível a outliers.

### Nearest Neighbors Classifier

Dado um objecto, este partilha a classe com o valor vizinho mais próximo. O algoritmo `KNN` é uma generalização deste, com K sendo normalmente um número ímpar, em que se escolhe a classe da maioria dos K vizinhos mais próximos. <br>
No entanto este algoritmo é sensível a atributos irrelevantes e sensível também a classificações efetuadas apenas tendo em conta um subset de features.

