# Data Modeling - models used and evaluation

The models used were Random Forest Classifier and the Support Vector Machine. 

For both of the models we started by mapping the playoff value into boolean values, 0 as 'N' and 1 as 'Y'. After the model application we applied the following approach:
- As we are predicting the playoffs and not the ranking, we needed a way to only select 8 teams to the playoffs phase, 4 of each conference (East and West).
    - So we sorted the teams by their probabilities of the model and then we chose the 4 teams with highest probabilities of each conference.

For each model we created 2 different functions. One that only predicts with the previous year as training data and the other function using all previous years as training data.  

## Random Forest Classifier (RFC)

This model had a good accuracy overall. We can see improvement over the years with both functions. However for the last 2/3 seasons, the accuracy went down due to the fact that new teams appeared and the model had less information to evaluate those. 

(Maybe with new approach for players stats we can see better results or with some weights on the attributes)

## Support Vector Machine (SVM)

This model had a bad performance mainly with only the last year as training data. It improved significantly with all previous years as training data, but still worst than the RFC model.