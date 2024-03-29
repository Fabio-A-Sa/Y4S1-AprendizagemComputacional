# 2 - Data Quality and Preparation

Assegurar que os dados estão limpos, integrados e reduzidos mas sem comprometer o seu significado é uma das principais etapas do CRISP-DM. O sentido de qualidade pode ser interpretado de várias maneiras:

- É correcta? Por vezes os resultados que lá aparecem não são os melhores;
- É completa? Pode haver falta de dados em determinadas colunas;
- É consistente? Os formatos apresentados podem não estar uniformes;
- É atualizada regularmente? 
- É interpretável? Pode ter demasiado ruído ou informação descartável;

### Missing Data

- Ignorar completamente: quando o target está em falta ou a percentagem de falhas de dados importantes é significativa;
- Preencher manualmente;
- Preencher automaticamente: com uma constante global, pela média ou pelo valor mais provável;

### Noising

- `Binning`: organização dos dados com base em valores semelhantes;
- `Regressão`: ajuste dos dados, para suavisar eventuais divergências;
- `Clustering`: para detectar e eliminar outliers;
- `Manualmente`;
- `Não fazer nada`, porque vários algoritmos são robustos quanto ao ruído;

### Integration

Durante a integração de dados de várias fontes é importante não ocorrer `redundância`, removendo sinónimos e dados derivados. <br>
A `inconsistência` também é outro problema: vários atributos para a mesma entidade em vários datasources. É causado por diferentes interpretações e representações.

### Reduction

Quando existe muito volume de dados é importante criar um sampling dos mesmos, mas a redução não pode levar a que o significado global mude. Os resultados analíticos devem ser os mesmos. <br>
Há várias abordagens, mas as recorrentes são: eliminação de dados sem significado, agregação de atributos com `feature selection`.

`PCA` - Principal Component Analysis - usado para remover a redundância através da combinação de atributos originais em novos (*principal components*). PC não são linearmente correlacionados e cada um é uma combinação linear dos originais.

`ICA` - Independent Component Analysis - assume que os atributos originais são de facto independentes,  não faz rank dos componentes e ao contrário do PCA não tenta reduzir a covariância entre os atributos;

### Transformation

`Feature selection` encaixa-se aqui também, assim como a normalização dos dados, agregação e discretização.