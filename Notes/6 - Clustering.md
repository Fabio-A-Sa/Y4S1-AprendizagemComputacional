# Clustering

Problema da descoberta da similaridade entre objectos, dadas as suas features.

- Quando os atributos são quantitativos é uma tarefa mais simples;
- Várias distâncias podem ser usadas, como a manhattan, a distância de edição, distância entre píxeis em imagens, entre outras;

## Clustering Techniques

- `Partitional` 

Cada objecto dentro do cluster está mais próximo de qualquer outro objecto do cluster do que o objecto mais próximo mas fora deste cluster.

- `Prototype-based`

Cada objecto do cluster está próximo de um protótipo que representa o cluster do que o protótipo que representa outro cluster.

Dentro de cada cluster podemos ter:
- Centroid, a média dos valores do cluster;
- Medoid, o objecto mais próximo da média dos valores do cluster;

## K-Means

Usa apenas seis iterações. Por um lado é eficiente e encontra bons resultados. Por outro pode ficar bloqueado num *local-optima*, pode necessitar de várias runs e não performa bem quando há ruído e outliers.

## DBSCAN

Define automaticamente o número de clusters, permitindo encontrá-los em qualquer formato. É robusto a outliers, por outro lado é computacionalmente mais complexo e é difícil de definir hyper-parameters.

## Agglomerative Hierarchical Clustering