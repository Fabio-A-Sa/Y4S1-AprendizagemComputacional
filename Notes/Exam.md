# Exam preparation

## Topics

- [1. Data Mining Process](#data-mining-process)
- [2. Data Quality and Preparation](#data-quality-and-preparation)
- [3. Clustering](#clustering)
- [4. Association Rules](#association-rules)

## Data Mining Process

- KDD: cleaning, integration, selection, transformation, data mining, evaluation, presentation;
- SEMMA: sample, explore, modify, model, access;
- CRISP-DM: business understanding, data understanding, data preparation, modeling, evaluation, deployment;
- SCRUM-DM:  business understanding, sprint, deployment;

## Data Quality and Preparation

- Binnig para noise e descobrir outliers, agrupar em intervalos (bins) dados contínuos;
- Data reduction: para os dados ficarem com o mesmo significado, o número de objectos tem de aumentar exponencialmente com o número de atributos (curse of dimensionality);
- PCA: admite que os atributos tem correlação e relaciona-os linearmente em novos (principal components), diminui a covariância entre eles e tem rank entre componentes. Os componentes não ficam combinados linearmente. 
- ICA: admite que os atributos originais são independentes mas existe na mesma combinação linear dos mesmos, não tenta diminuir a covariância entre estes nem faz ranking de componentes;
- MDS (multidimensional scalling): calcula a distância entre pares de objectos para extrair features relevantes;
- Attribute selection: filters (relação simples, como covariância), wrappers (usando modelos ML), embedded (de acordo com a sua contribuição aquando do treino);
- Existe attribute selection com forward and backward approaches;
- Master Data Management (MDM), para criar key business entities using a master repository;
- Z-Score Normalization para quando a média é 0 e deviation é 1, smoth normalization para reduzir noise e representation by patterns, log transformation para dados não lineares ou skewed distribution;

## Clustering

- Distance: manhattan, euclidean, hamming (diferença de strings de igual comprimento), Levenshtein ou distância de edição, between strings (bag of words), mine warping (edit distance mas com tempo), between images (by pixel or by feature);
- Clustering: partitional (objectos próximos a objectos), prototype-based (objectos próximos a protótipos), graph-based, density-based;
- K-Means: 6 iterations, centroid and menoid, preso no local optima, não é bom quando há outliers nem quando há formas não-convexas;
- DBSCAN: define o número de clusters, sensível a densidade, encontra qualquer figura, dificil de definir hyper-parameters mas fica no global optima;
- AHC (Agglomerative Hierarchical Clustering): graph-based com ligações (single, complete, average), hyper-parameters são simples de criar, mas torna-se difícil quando os datasets são grandes e pode ficar preso no local optima;
- Evaluation de clusters através de silhouetas (1, -1, 0) ou de JACCARD (se os objectos tiverem labels);

## Association Rules

- Suporte (A): quantidade de A / quantidade total;
- Confiança (A -> B): suporte (A -> B) / suporte (A);
- Lift: P(A && B) / (P (A) * P(B));
- Priority proprety in APRIORI algorithm: itemset mining, encontrar frequentes itemsets, BFS algorithm, mau para a eficiência temporal;