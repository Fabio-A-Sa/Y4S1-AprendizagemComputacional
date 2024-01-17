# 4 - Ensemble Learning

Constituído por diversos modelos, cada um obtido a partir do aprendizado com diferentes partes dos dados. Ao combinar as partes e as previsões parciais de cada modelo obtém-se uma única previsão. O sistema pode ser homogéneo ou heterogéneo de acordo com a diversidade dos algoritmos utilizados.

#### Prós

- Maior accuracy, dá para compensa alguns erros de previsão de determinadas partes;
- A diversidade é importante para que diferentes modelos se especializem em diferentes áreas do dataset;

#### Contras

- É uma forma mais complexa de previsão;
- A função de merge dos resultados parciais pode não ser simples de obter;

## Modelos

### Bagging

De Bootstrap AGGregatING. É um método robusto a ruído. O dataset é dividido em outros menores para traininig. Se o classificador for instável ou com propenso a overfitting, é combatido com outro modelo ao lado que estabiliza o resultado global. Se o classificador for mesmo instável, podemos usar abordagens de aprendizado como decision trees ou neural networks. Usa `independent sampling` e `uniform aggregation`.

Usado para classificação e regressão.

### Boosting

Inicialmente todos as partes de treino têm o mesmo peso. As partes de treino a partir de K ficam com mais peso nas features onde os modelos até K não conseguiram avaliar bem. No final, ao agregar os dados, o peso de cada classificador é proporcional à sua accuracy. Usa `error dependent sampling` e `weighted aggregation`.

O Boosting tem tendências a encontrar melhores resultados do que o Bagging, mas corre mais riscos de overfitting.

Usado para classificação.

### Random Forest

Em cada iteração seleciona aleatoriamente algumas features para prever o resultado. O resultado final resulta da sobreposição dos resultados das várias árvores. É mais robusto a erros e outliers, insensível ao número de atributos em cada split e mais rápido.

Usado para classificação e regressão.

### Negative Correlation

Em cada iteração tenta minimizar o erro através de uma função que dá penalidade de acordo com o erro médio dos modelos já treinados e avaliados. São usados apenas para modelos de regressão (porque são indicados para maximizar ou minimizar uma função objectivo), como por exemplo em `neural networks` ou `support vector regressions`. Também são usados em modelos com uma correlação negativa do erro médio dos modelos treinados na fase anterior.

Usado para regressão.

## Base Models

- Para `classificação`, os modelos base devem ter a máxima accuracy possível, mas com isso podem ter diversos erros.

- Para `regressão`, os modelos base devem ser capazes de minimizar o erro conjunto, para minimizar assim também o overfitting e a variação dos resultados obtidos.

Hoje em dia há um foco grande em `homogeneous assembles`, mas os processos também são aplicáveis a `heterogeneous assembles`.