import pandas as pd
import numpy as np  
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_score, recall_score, roc_curve
from sklearn.model_selection import cross_val_score, learning_curve
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.svm import SVC

def plot_false_predictions(false_predictions_ea, false_predictions_we, path):
    # Plotting the results
    x_values = list(range(3, 11))
    y_values = list(range(0, 5))

    # Plotting the lines
    plt.plot(x_values, false_predictions_ea, label='EA Conference', marker='o')
    plt.plot(x_values, false_predictions_we, label='WE Conference', marker='o')

    # Setting up plot details
    plt.xlabel('Years')
    plt.ylabel('Number of False Positives')
    plt.title('Fail Predictions for Each Conference')
    plt.xticks(x_values)
    plt.yticks(y_values)
    plt.legend()

    # Save the plot
    plt.savefig(path)
    plt.close()

# Function for RFC model with only the year before
def RFCmodel_last_year(year):
    # Data Preparation
    train_data = pd.read_csv(f"../data/datasets/dataset{year - 1}.csv")
    test_data = pd.read_csv(f"../data/datasets/dataset{year}.csv")

    playoff_mapping = {'N': 0, 'Y': 1}

    train_data['playoff'] = train_data['playoff'].map(playoff_mapping)
    if(year != 11):
        test_data['playoff'] = test_data['playoff'].map(playoff_mapping)

    # Data Splitting
    X_train = train_data.drop(columns=['tmID', 'playoff', 'confID'])
    y_train = train_data['playoff']
    X_test = test_data.drop(columns=['tmID', 'playoff', 'confID'])
    y_test = test_data['playoff']

    # Model Selection and Training
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Model Evaluation
    y_pred = model.predict(X_test)
    probabilities = model.predict_proba(X_test)[:, 1]

    # Sort teams by their predicted probabilities in descending order
    sorted_teams = sorted(range(len(probabilities)), key=lambda i: probabilities[i], reverse=True)

    # Select the top 8 teams based on their predicted probabilities
    top_8_teams = [0] * len(probabilities)
    ea_count, we_count = 0, 0
    for i in sorted_teams:
        if ea_count < 4 and test_data.at[i, 'confID'] == 'EA':
            top_8_teams[i] = 1
            ea_count += 1
        elif we_count < 4 and test_data.at[i, 'confID'] == 'WE':
            top_8_teams[i] = 1
            we_count += 1

    if(year != 11):
        # Metrics Calculation
        accuracy = accuracy_score(y_test, top_8_teams)
        precision = precision_score(y_test, top_8_teams)
        recall = recall_score(y_test, top_8_teams)
        report = classification_report(y_test, top_8_teams)

        # Confusion Matrix
        cm = confusion_matrix(y_test, top_8_teams)
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['No Playoff', 'Playoff'],
                    yticklabels=['No Playoff', 'Playoff'])
        plt.xlabel('Predicted')
        plt.ylabel('Actual')
        plt.title(f'Confusion Matrix - Year {year}')
        plt.savefig(f'../data/plots/rfc_last_year/cm_{year}.png')
        plt.close()

        # False Positives and False Negatives
        false_positives = cm[0, 1]
        false_negatives = cm[1, 0]
        #print(f"False Positives: {false_positives}")
        #print(f"False Negatives: {false_negatives}")

        false_positives_ea = 0
        false_positives_we = 0
        
        # Append results to lists
        for i in range(test_data.shape[0]):
            if((test_data['confID'][i] == 'EA') & (top_8_teams[i] == 1) & (y_test[i] == 0)):
                false_positives_ea += 1
            elif ((test_data['confID'][i] == 'WE') & (top_8_teams[i] == 1) & (y_test[i] == 0)):
                false_positives_we += 1
        
        #print(false_positives_ea)
        #print(false_positives_we)

        false_predictions_ea.append(false_positives_ea)
        false_predictions_we.append(false_positives_we)

        # Feature Importances
        feature_importances = model.feature_importances_
        feature_names = X_train.columns
        feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': feature_importances})
        feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

        # Plot Feature Importances
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Importance', y='Feature', data=feature_importance_df)
        plt.title('Feature Importances')
        plt.savefig(f'../data/plots/rfc_last_year/feature_importance_{year}.png')
        plt.close()

        # ROC Curve
        fpr, tpr, thresholds = roc_curve(y_test, probabilities)
        plt.plot(fpr, tpr, label='ROC Curve')
        plt.plot([0, 1], [0, 1], linestyle='--', label='Random')
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title(f'ROC Curve of Year {year}')
        plt.legend()
        plt.savefig(f'../data/plots/rfc_last_year/roc_{year}.png')
        plt.close()

        # Learning Curve
        train_sizes, train_scores, test_scores = learning_curve(model, X_train, y_train, cv=5, scoring='accuracy', train_sizes=[0.1, 0.25, 0.5, 0.75, 1])
        plt.plot(train_sizes, np.mean(train_scores, axis=1), label='Training Score')
        plt.plot(train_sizes, np.mean(test_scores, axis=1), label='Cross-Validation Score')
        plt.xlabel('Training Set Size')
        plt.ylabel('Accuracy Score')
        plt.title(f'Learning Curve of Year {year}')
        plt.legend()
        plt.savefig(f'../data/plots/rfc_last_year/learning_curve_{year}.png')
        plt.close()

        # Cross-validation Score
        cross_val = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
        #print(f"Cross-validation Scores: {cross_val}")

        # Print Metrics
        #print(f"Accuracy: {accuracy:.2f}")
        #print(f"Precision: {precision:.2f}")
        #print(f"Recall: {recall:.2f}")
        #print("Classification Report:\n", report)

    # Save results to CSV     
    result = test_data[['tmID']].copy()
    if(year == 11):
        result['playoff'] = top_8_teams
        result.sort_values(by='tmID', inplace=True)
        result.to_csv(f"../data/predictions/year_11/rfc/last_year_{year}.csv", index=False)
    else:
        result['playoff'] = y_test
        result['prediction'] = top_8_teams
        result.to_csv(f"../data/predictions/rfc/last_year_{year}.csv", index=False)

# Iterate through years for RFC model
false_predictions_ea = []
false_predictions_we = []
print("RFC Model with only Last Year!")
for i in range(3, 12):
    RFCmodel_last_year(i)

plot_false_predictions(false_predictions_ea, false_predictions_we, "../data/plots/rfc_last_year/false_predictions.png")


# Function for RFC model with all years before
def RFCmodel_all_years(year):
    # Step 1: Data Preparation
    all_train_data = pd.DataFrame()

    for y in range(2, year):
        train_data = pd.read_csv(f"../data/datasets/dataset{y}.csv")
        playoff_mapping = {'N': 0, 'Y': 1}
        train_data['playoff'] = train_data['playoff'].map(playoff_mapping)
        all_train_data = pd.concat([all_train_data, train_data], axis=0)

    test_data = pd.read_csv(f"../data/datasets/dataset{year}.csv")
    playoff_mapping = {'N': 0, 'Y': 1}
    if(year != 11):
        test_data['playoff'] = test_data['playoff'].map(playoff_mapping)

    # Step 2: Data Splitting
    X_train = all_train_data.drop(columns=['tmID', 'playoff', 'confID'])
    y_train = all_train_data['playoff']
    X_test = test_data.drop(columns=['tmID', 'playoff', 'confID'])
    y_test = test_data['playoff']

    # Step 3: Model Selection and Training
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Step 4: Model Evaluation
    y_pred = model.predict(X_test)
    probabilities = model.predict_proba(X_test)[:, 1]
    sorted_teams = sorted(range(len(probabilities)), key=lambda i: probabilities[i], reverse=True)

    # Select the top 8 teams based on their predicted probabilities
    top_8_teams = [0] * len(probabilities)
    ea_count, we_count = 0, 0
    for i in sorted_teams:
        if ea_count < 4 and test_data.at[i, 'confID'] == 'EA':
            top_8_teams[i] = 1
            ea_count += 1
        elif we_count < 4 and test_data.at[i, 'confID'] == 'WE':
            top_8_teams[i] = 1
            we_count += 1

    if(year != 11):
        # Metrics Calculation
        accuracy = accuracy_score(y_test, top_8_teams)
        precision = precision_score(y_test, top_8_teams)
        recall = recall_score(y_test, top_8_teams)
        report = classification_report(y_test, top_8_teams)

        # Confusion Matrix
        cm = confusion_matrix(y_test, top_8_teams)
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['No Playoff', 'Playoff'],
                    yticklabels=['No Playoff', 'Playoff'])
        plt.xlabel('Predicted')
        plt.ylabel('Actual')
        plt.title(f'Confusion Matrix - Year {year}')
        plt.savefig(f'../data/plots/rfc_all_years/cm_{year}.png')
        plt.close()

        # False Positives and False Negatives
        false_positives = cm[0, 1]
        false_negatives = cm[1, 0]
        #print(f"False Positives: {false_positives}")
        #print(f"False Negatives: {false_negatives}")
        
        false_positives_ea = 0
        false_positives_we = 0
        
        # Append results to lists
        for i in range(test_data.shape[0]):
            if((test_data['confID'][i] == 'EA') & (top_8_teams[i] == 1) & (y_test[i] == 0)):
                false_positives_ea += 1
            elif ((test_data['confID'][i] == 'WE') & (top_8_teams[i] == 1) & (y_test[i] == 0)):
                false_positives_we += 1
        
        #print(false_positives_ea)
        #print(false_positives_we)

        false_predictions_ea.append(false_positives_ea)
        false_predictions_we.append(false_positives_we)
        
        # Feature Importances
        feature_importances = model.feature_importances_
        feature_names = X_train.columns
        feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': feature_importances})
        feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

        # Plot Feature Importances
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Importance', y='Feature', data=feature_importance_df)
        plt.title('Feature Importances')
        plt.savefig(f'../data/plots/rfc_all_years/feature_importance_{year}.png')
        plt.close()

        # ROC Curve
        fpr, tpr, thresholds = roc_curve(y_test, probabilities)
        plt.plot(fpr, tpr, label='ROC Curve')
        plt.plot([0, 1], [0, 1], linestyle='--', label='Random')
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title(f'ROC Curve of Year {year}')
        plt.legend()
        plt.savefig(f'../data/plots/rfc_all_years/roc_{year}.png')
        plt.close()

        # Learning Curve
        train_sizes, train_scores, test_scores = learning_curve(model, X_train, y_train, cv=5, scoring='accuracy', train_sizes=[0.1, 0.25, 0.5, 0.75, 1])
        plt.plot(train_sizes, np.mean(train_scores, axis=1), label='Training Score')
        plt.plot(train_sizes, np.mean(test_scores, axis=1), label='Cross-Validation Score')
        plt.xlabel('Training Set Size')
        plt.ylabel('Accuracy Score')
        plt.title(f'Learning Curve of Year {year}')
        plt.legend()
        plt.savefig(f'../data/plots/rfc_all_years/learning_curve_{year}.png')
        plt.close()

        # Cross-validation Score
        cross_val = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
        #print(f"Cross-validation Scores: {cross_val}")

        # Print Metrics
        #print(f"Accuracy: {accuracy:.2f}")
        #print(f"Precision: {precision:.2f}")
        #print(f"Recall: {recall:.2f}")
        #print("Classification Report:\n", report)

    # Save results to CSV
    # Save results to CSV     
    result = test_data[['tmID']].copy()
    if(year == 11):
        result['playoff'] = top_8_teams
        result.sort_values(by='tmID', inplace=True)
        result.to_csv(f"../data/predictions/year_11/rfc/all_years_{year}.csv", index=False)
    else:
        result['playoff'] = y_test
        result['prediction'] = top_8_teams
        result.to_csv(f"../data/predictions/rfc/all_years_{year}.csv", index=False)

# Iterate through years for RFC model
false_predictions_ea = []
false_predictions_we = []
print("RFC Model with all Years until this one!")
for i in range(3, 12):
    RFCmodel_all_years(i)

plot_false_predictions(false_predictions_ea, false_predictions_we, "../data/plots/rfc_all_years/false_predictions.png")


# Function for SVM model with only the year before
def SVMmodel_last_year(year):
    # Step 1: Data Preparation
    train_data = pd.read_csv(f"../data/datasets/dataset{year - 1}.csv")
    test_data = pd.read_csv(f"../data/datasets/dataset{year}.csv")

    playoff_mapping = {'N': 0, 'Y': 1}
    train_data['playoff'] = train_data['playoff'].map(playoff_mapping)
    if(year != 11):
        test_data['playoff'] = test_data['playoff'].map(playoff_mapping)

    # Step 2: Data Splitting
    X_train = train_data.drop(columns=['tmID', 'playoff', 'confID'])
    y_train = train_data['playoff']
    X_test = test_data.drop(columns=['tmID', 'playoff', 'confID'])
    y_test = test_data['playoff']

    # Step 3: Model Selection and Training
    model = SVC(probability=True)
    model.fit(X_train, y_train)

    # Model Evaluation
    y_pred = model.predict(X_test)
    probabilities = model.predict_proba(X_test)[:, 1]

    # Sort teams by their predicted probabilities in descending order
    sorted_teams = sorted(range(len(probabilities)), key=lambda i: probabilities[i], reverse=True)

    # Select the top 8 teams based on their predicted probabilities
    top_8_teams = [0] * len(probabilities)
    ea_count, we_count = 0, 0
    for i in sorted_teams:
        if ea_count < 4 and test_data.at[i, 'confID'] == 'EA':
            top_8_teams[i] = 1
            ea_count += 1
        elif we_count < 4 and test_data.at[i, 'confID'] == 'WE':
            top_8_teams[i] = 1
            we_count += 1

    if(year != 11):
        # Metrics Calculation
        accuracy = accuracy_score(y_test, top_8_teams)
        precision = precision_score(y_test, top_8_teams)
        recall = recall_score(y_test, top_8_teams)
        report = classification_report(y_test, top_8_teams)

        # Confusion Matrix
        cm = confusion_matrix(y_test, top_8_teams)
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['No Playoff', 'Playoff'],
                    yticklabels=['No Playoff', 'Playoff'])
        plt.xlabel('Predicted')
        plt.ylabel('Actual')
        plt.title(f'Confusion Matrix - Year {year}')
        plt.savefig(f'../data/plots/svm_last_year/cm_{year}.png')
        plt.close()

        # False Positives and False Negatives
        false_positives = cm[0, 1]
        false_negatives = cm[1, 0]
        #print(f"False Positives: {false_positives}")
        #print(f"False Negatives: {false_negatives}")

        false_positives_ea = 0
        false_positives_we = 0
        
        # Append results to lists
        for i in range(test_data.shape[0]):
            if((test_data['confID'][i] == 'EA') & (top_8_teams[i] == 1) & (y_test[i] == 0)):
                false_positives_ea += 1
            elif ((test_data['confID'][i] == 'WE') & (top_8_teams[i] == 1) & (y_test[i] == 0)):
                false_positives_we += 1
        
        #print(false_positives_ea)
        #print(false_positives_we)

        false_predictions_ea.append(false_positives_ea)
        false_predictions_we.append(false_positives_we)

        # ROC Curve
        fpr, tpr, thresholds = roc_curve(y_test, probabilities)
        plt.plot(fpr, tpr, label='ROC Curve')
        plt.plot([0, 1], [0, 1], linestyle='--', label='Random')
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title(f'ROC Curve of Year {year}')
        plt.legend()
        plt.savefig(f'../data/plots/svm_last_year/roc_{year}.png')
        plt.close()

        # Learning Curve
        train_sizes, train_scores, test_scores = learning_curve(model, X_train, y_train, cv=5, scoring='accuracy', train_sizes=[0.1, 0.25, 0.5, 0.75, 1])
        plt.plot(train_sizes, np.mean(train_scores, axis=1), label='Training Score')
        plt.plot(train_sizes, np.mean(test_scores, axis=1), label='Cross-Validation Score')
        plt.xlabel('Training Set Size')
        plt.ylabel('Accuracy Score')
        plt.title(f'Learning Curve of Year {year}')
        plt.legend()
        plt.savefig(f'../data/plots/svm_last_year/learning_curve_{year}.png')
        plt.close()

        # Cross-validation Score
        cross_val = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
        #print(f"Cross-validation Scores: {cross_val}")

        # Print Metrics
        #print(f"Accuracy: {accuracy:.2f}")
        #print(f"Precision: {precision:.2f}")
        #print(f"Recall: {recall:.2f}")
        #print("Classification Report:\n", report)

    # Save results to CSV
    # Save results to CSV     
    result = test_data[['tmID']].copy()
    if(year == 11):
        result['playoff'] = top_8_teams
        result.sort_values(by='tmID', inplace=True)
        result.to_csv(f"../data/predictions/year_11/svm/last_year_{year}.csv", index=False)
    else:
        result['playoff'] = y_test
        result['prediction'] = top_8_teams
        result.to_csv(f"../data/predictions/svm/last_year_{year}.csv", index=False)

# Iterate through years for RFC model
false_predictions_ea = []
false_predictions_we = []
print("SVM Model with only Last Year!")
for i in range(3, 12):
    SVMmodel_last_year(i)

plot_false_predictions(false_predictions_ea, false_predictions_we, "../data/plots/svm_last_year/false_predictions.png")


# Function for SVM model with all years before
def SVMmodel_all_years(year):
    # Step 1: Data Preparation
    all_train_data = pd.DataFrame()

    for y in range(2, year):
        train_data = pd.read_csv(f"../data/datasets/dataset{y}.csv")
        playoff_mapping = {'N': 0, 'Y': 1}
        train_data['playoff'] = train_data['playoff'].map(playoff_mapping)
        all_train_data = pd.concat([all_train_data, train_data], axis=0)

    test_data = pd.read_csv(f"../data/datasets/dataset{year}.csv")
    playoff_mapping = {'N': 0, 'Y': 1}
    if(year != 11):
        test_data['playoff'] = test_data['playoff'].map(playoff_mapping)

    # Step 2: Data Splitting
    X_train = all_train_data.drop(columns=['tmID', 'playoff', 'confID'])
    y_train = all_train_data['playoff']
    X_test = test_data.drop(columns=['tmID', 'playoff', 'confID'])
    y_test = test_data['playoff']

    # Step 3: Model Selection and Training
    model = SVC(probability=True)
    model.fit(X_train, y_train)

    # Model Evaluation
    y_pred = model.predict(X_test)
    probabilities = model.predict_proba(X_test)[:, 1]
    sorted_teams = sorted(range(len(probabilities)), key=lambda i: probabilities[i], reverse=True)

    # Select the top 8 teams based on their predicted probabilities
    top_8_teams = [0] * len(probabilities)
    ea_count, we_count = 0, 0
    for i in sorted_teams:
        if ea_count < 4 and test_data.at[i, 'confID'] == 'EA':
            top_8_teams[i] = 1
            ea_count += 1
        elif we_count < 4 and test_data.at[i, 'confID'] == 'WE':
            top_8_teams[i] = 1
            we_count += 1

    if(year != 11):
        # Metrics Calculation
        accuracy = accuracy_score(y_test, top_8_teams)
        precision = precision_score(y_test, top_8_teams)
        recall = recall_score(y_test, top_8_teams)
        report = classification_report(y_test, top_8_teams)

        # Confusion Matrix
        cm = confusion_matrix(y_test, top_8_teams)
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['No Playoff', 'Playoff'],
                    yticklabels=['No Playoff', 'Playoff'])
        plt.xlabel('Predicted')
        plt.ylabel('Actual')
        plt.title(f'Confusion Matrix - Year {year}')
        plt.savefig(f'../data/plots/svm_all_years/cm_{year}.png')
        plt.close()

        # False Positives and False Negatives
        false_positives = cm[0, 1]
        false_negatives = cm[1, 0]
        #print(f"False Positives: {false_positives}")
        #print(f"False Negatives: {false_negatives}")

        false_positives_ea = 0
        false_positives_we = 0
        
        # Append results to lists
        for i in range(test_data.shape[0]):
            if((test_data['confID'][i] == 'EA') & (top_8_teams[i] == 1) & (y_test[i] == 0)):
                false_positives_ea += 1
            elif ((test_data['confID'][i] == 'WE') & (top_8_teams[i] == 1) & (y_test[i] == 0)):
                false_positives_we += 1
        
        #print(false_positives_ea)
        #print(false_positives_we)

        false_predictions_ea.append(false_positives_ea)
        false_predictions_we.append(false_positives_we)

        # ROC Curve
        fpr, tpr, thresholds = roc_curve(y_test, probabilities)
        plt.plot(fpr, tpr, label='ROC Curve')
        plt.plot([0, 1], [0, 1], linestyle='--', label='Random')
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title(f'ROC Curve of Year {year}')
        plt.legend()
        plt.savefig(f'../data/plots/svm_all_years/roc_{year}.png')
        plt.close()

        # Learning Curve
        train_sizes, train_scores, test_scores = learning_curve(model, X_train, y_train, cv=5, scoring='accuracy', train_sizes=[0.1, 0.25, 0.5, 0.75, 1])
        plt.plot(train_sizes, np.mean(train_scores, axis=1), label='Training Score')
        plt.plot(train_sizes, np.mean(test_scores, axis=1), label='Cross-Validation Score')
        plt.xlabel('Training Set Size')
        plt.ylabel('Accuracy Score')
        plt.title(f'Learning Curve of Year {year}')
        plt.legend()
        plt.savefig(f'../data/plots/svm_all_years/leaning_curve_{year}.png')
        plt.close()

        # Cross-validation Score
        cross_val = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
        #print(f"Cross-validation Scores: {cross_val}")

        # Print Metrics
        #print(f"Accuracy: {accuracy:.2f}")
        #print(f"Precision: {precision:.2f}")
        #print(f"Recall: {recall:.2f}")
        #print("Classification Report:\n", report)

    # Save results to CSV
    # Save results to CSV     
    result = test_data[['tmID']].copy()
    if(year == 11):
        result['playoff'] = top_8_teams
        result.sort_values(by='tmID', inplace=True)
        result.to_csv(f"../data/predictions/year_11/svm/all_years_{year}.csv", index=False)
    else:
        result['playoff'] = y_test
        result['prediction'] = top_8_teams
        result.to_csv(f"../data/predictions/svm/all_years_{year}.csv", index=False)

# Iterate through years for RFC model
false_predictions_ea = []
false_predictions_we = []
print("SVM Model with all Years until this one!")
for i in range(3, 12):
    SVMmodel_all_years(i)

plot_false_predictions(false_predictions_ea, false_predictions_we, "../data/plots/svm_all_years/false_predictions.png")

