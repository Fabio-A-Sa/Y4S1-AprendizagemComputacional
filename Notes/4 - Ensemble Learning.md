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

De Bootstrap AGGregatING. É um método robusto a ruído. O dataset é dividido em outros menores para traininig. Se o classificador for instável ou com propenso a overfitting, é combatido com outro modelo ao lado que estabiliza o resultado global. 

### 