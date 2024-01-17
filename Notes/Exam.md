# Exam preparation

## Topics

- [1. Data Mining Process](#data-mining-process)
- [2. Data Quality and Preparation](#data-quality-and-preparation)
- [3. Clustering](#clustering)

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

- 