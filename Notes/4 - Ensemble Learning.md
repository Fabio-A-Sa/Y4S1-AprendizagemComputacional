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

De Bootstrap AGGregatING. É um método robusto a ruído. O dataset é dividido em outros menores para traininig. Se o classificador for instável ou com propenso a overfitting, é combatido com outro modelo ao lado que estabiliza o resultado global. Se o classificador for mesmo instável, podemos usar abordagens de aprendizado como decision trees ou neural networks. Usa `independent sampliing` e `uniform aggregation`.

### Boosting

Inicialmente todos as partes de treino têm o mesmo peso. As partes de treino a partir de K ficam com mais peso nas features onde os modelos até K não conseguiram avaliar bem. No final, ao agregar os dados, o peso de cada classificador é proporcional à sua accuracy. Usa `error dependent sampling` e `weighted aggregation`.

O Boosting tem tendências a encontrar melhores resultados do que o Bagging, mas corre mais riscos de overfitting.

### Random Forest




### Negative Correlation