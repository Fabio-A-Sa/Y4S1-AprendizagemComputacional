from cmath import nan
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import warnings
import seaborn as sns

DATASETS_PATH = "../data/raw/"
PLOTS_PATH = "../data/plots/analysis/"
ABS_MIN_CORRELATION_FEATURES = 0.9
ABS_MIN_CORRELATION_TARGET = 0.15

DATASETS = [
    ('awards_players', pd.read_csv(f"{DATASETS_PATH}awards_players.csv")),
    ('coaches', pd.read_csv(f"{DATASETS_PATH}coaches.csv")),
    ('players_teams', pd.read_csv(f"{DATASETS_PATH}players_teams.csv")),
    ('players', pd.read_csv(f"{DATASETS_PATH}players.csv")),
    ('series_post', pd.read_csv(f"{DATASETS_PATH}series_post.csv")),
    ('teams_post', pd.read_csv(f"{DATASETS_PATH}teams_post.csv")),
    ('teams', pd.read_csv(f"{DATASETS_PATH}teams.csv"))
]

def compute_correlation(data: pd, column1: str, column2: str) -> tuple | None:

    if data[column1].isna().any() or data[column2].isna().any() or data[column1].eq(None).any() or data[column2].eq(None).any():
        return None

    data[column1] = LabelEncoder().fit_transform(data[column1])
    data[column2] = LabelEncoder().fit_transform(data[column2])

    try:
        correlation = data[column1].corr(data[column2])
    except Exception as _:
        return None

    if not pd.isna(correlation):
        return (column1, column2, round(correlation, 2))
    return None

def compute_correlations(data: pd, base: float, excluded: list):
    
    info = []
    columns = data.columns
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    
    for i in range(len(columns)):
        for j in range(i + 1, len(columns)):
            
            if columns[i] not in excluded and columns[j] not in excluded:
                result = compute_correlation(data, columns[i], columns[j])
                if result != None:
                    info.append(result) 
    
    return [(col1, col2, value) for (col1, col2, value) in info if abs(value) >= base]

def compute_plot(dataset: str, data: pd.DataFrame, column1: str, column2: str, line: str = True) -> None:

    plt.figure(figsize=(8, 6))

    if line:
        (_, _, value) = compute_correlation(data, column1, column2)
        sns.regplot(data=data, x=column1, y=column2)
        plt.title(f"Correlation between '{column1}' and '{column2}' is {value} in {dataset}")

    else:
        plt.scatter(data[column1], data[column2])
        plt.title(f"Scatter plot of '{column1}' and '{column2}' in {dataset}")


    path = f"{PLOTS_PATH}{dataset}_{column1}_{column2}_correlation.png"
    print(f"\n#### Correlation between '{column1}' and '{column2}' - {dataset} dataset")
    print(f"\n![]({path})")

    plt.savefig(path)
    plt.close()

def find_same_valued_cols(data: pd) -> list:
    return [col for col in data.columns if data[col].nunique() == 1]

def automatic_correlations():

    print("# Data Analysis")
    print("\n## Find same valued cols:\n")
    excluded = []
    for (dataset, data) in DATASETS.copy():
        result = find_same_valued_cols(data.copy())
        print(f"- `{dataset}`: {', '.join(result)}")
        excluded.append((dataset, data, result))

    print(f"\n## Find some correlations between features\n### Min correlation = {ABS_MIN_CORRELATION_FEATURES}")
    for (dataset, data, excluded_columns) in excluded:
        correlations = compute_correlations(data.copy(), ABS_MIN_CORRELATION_FEATURES, excluded_columns)
        if len(correlations):
            print(f"\n#### Dataset: {dataset}\n")
            for (col1, col2, value) in correlations:
                print(f"- `{col1}`:`{col2}` = {value}")

def manual_correlations():
    
    plots = [            

        # players_teams
        [DATASETS[2][0], DATASETS[2][1], 'GP', 'points'],
        [DATASETS[2][0], DATASETS[2][1], 'GP', 'assists'],
        [DATASETS[2][0], DATASETS[2][1], 'GP', 'steals'],
        [DATASETS[2][0], DATASETS[2][1], 'GP', 'blocks'],
        [DATASETS[2][0], DATASETS[2][1], 'GP', 'turnovers'],
        [DATASETS[2][0], DATASETS[2][1], 'GP', 'minutes'],
    ]

    for [dataset, data, col1, col2] in plots:
        compute_plot(dataset, data, col1, col2)

    # Manual - correlation between datasets

    players_data = DATASETS[3][1]
    players_teams_data = DATASETS[2][1]

    # players vs. players_teams
    players_data = players_data.rename(columns={'bioID': 'playerID'})
    players_total = pd.merge(players_data, players_teams_data, on=['playerID'], how="inner")

    compute_plot("(players_join_players_team)", players_total, 'pos', 'points', False)
    compute_plot("(players_join_players_team)", players_total, 'pos', 'assists', False)
    compute_plot("(players_join_players_team)", players_total, 'pos', 'steals', False)
    compute_plot("(players_join_players_team)", players_total, 'pos', 'blocks', False)
    compute_plot("(players_join_players_team)", players_total, 'pos', 'turnovers', False)

def target_correlations():
   
    teams_data = DATASETS[6][1]

    # Boolean target variable
    teams_data['playoff'] = teams_data['playoff'].map({'N': 0, 'Y': 1})

    # Compute correlations between numeric features and target variable
    teams_data = teams_data.select_dtypes(include=['number'])
    correlations = teams_data.corr()
    target_correlation = correlations['playoff'].sort_values(ascending=False) * 100
    
    # Select features with important correlation values
    selected_features = target_correlation[abs(target_correlation) > ABS_MIN_CORRELATION_TARGET * 100].drop('playoff').index

    # Compute plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x=selected_features, y=target_correlation[selected_features].values)
    plt.title("Correlations between team's features and target variable (playoff)")
    plt.xlabel('Features')
    plt.ylabel('Correlation value (%)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    path = f"{PLOTS_PATH}target_correlations.png"
    plt.savefig(path)
    plt.close()

    # Save progress in markdown as well
    print(f"\n### Correlations between team's features and target variable (playoff)")
    print(f"\n![]({path})")

if __name__ == '__main__':
    automatic_correlations()
    manual_correlations()
    target_correlations()