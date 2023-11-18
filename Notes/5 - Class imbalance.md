# Class Imbalance

Os modelos de Machine Learning estão preparados para minimizar os Falsos Positivos e os Falsos Negativos, e quando os dados de treino possuem uma grande disparidade entre classes positivas e negativas, o modelo poderá escolher tudo de uma só classe. De facto, não prevê nada e poderá colocar em causa o estudo em si.

![Evaluation Measures](../Images/ConfusionMatrix.png)

Por isso, a classe de interesse deve ser sempre:
- a que não é positiva, dado o contexto;
- a que é menos frequente;

Além disso, deve haver um pré-processamento que garanta um balanceamento artificial das duas classes em problemas de classificação:
- recolher mais dados para o dataset em análise, se possível;
- eliminar dados da classe com mais samples;
- duplicar os dados da classe minoritária;
- criar dados sintéticos a partir dos preexistentes;
- escolher os algoritmos certos dado o contexto do imbalance;

