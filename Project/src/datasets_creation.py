import pandas as pd

# Create dataset for training
def create_dataset(year):
    teams = pd.read_csv("../data/processed/teams_processed.csv")
    players = pd.read_csv("../data/processed/players_teams_processed.csv")
    coaches = pd.read_csv("../data/processed/coaches_processed.csv")

    if(year == 11):
        teams_y11 = pd.read_csv("../data/raw/year_11/teams.csv")
        players_y11 = pd.read_csv("../data/raw/year_11/players_teams.csv")
        coaches_y11 = pd.read_csv("../data/raw/year_11/coaches.csv")
    
    # Teams
    if(year == 11):
        dataset_teams = teams_y11[teams_y11['year'] == year][["year", "tmID", "confID"]]
        dataset_teams['playoff'] = ""
    else:
        dataset_teams = teams[teams['year'] == year][["year", "tmID", "confID", "playoff"]]
    previous_year_teams = teams[teams['year'] == (year - 1)].copy()

    teams = teams.sort_values(by=['tmID', 'year'])
    teams['total_championships'] = teams.groupby('tmID')['championship'].cumsum()

    # Filter the teams data for year - 1 and select relevant columns
    championship_info_until_year = teams[teams['year'] == (year - 1)][['tmID', 'total_championships']]  

    previous_year_teams = previous_year_teams.merge(championship_info_until_year, on='tmID', how='left')
    previous_year_teams.drop(columns=['year', 'confID', 'playoff'], inplace=True)
    dataset_teams = dataset_teams.merge(previous_year_teams, on='tmID', how='left')
    dataset_teams["total_championships"] = dataset_teams["total_championships"].fillna(0.0)
    dataset_teams.drop(columns=['championship'], inplace=True)
    ###

    # players_teams
    if(year == 11):
        current_year_players = players_y11[players_y11['year'] == year][['year', 'playerID', 'tmID']]
    else:
        current_year_players = players[players['year'] == year][['year', 'playerID', 'tmID']]
    previous_year_players = players[players['year'] == (year - 1)].copy()
    previous_year_players.drop(columns=['year', 'tmID', 'pos'], inplace=True)

    dataset_players = current_year_players.merge(previous_year_players, on='playerID', how='inner')
    
    dataset = dataset_teams.merge(dataset_players, on=['year', 'tmID'], how='left')
    
    dataset = dataset.groupby(['year', 'tmID', 'playoff']).agg({
        "confID": "first",
        "season_wins": "first",
        "season_losses": "first",
        "matches": "first",
        "win_rate": "first",
        "post_matches": "first",
        "post_win_rate": "first",
        "total_championships": "first",
        "nrAwards": "sum",
        "o_pts": "first",
        "o_oreb": "first",
        "o_dreb": "first",
        "o_asts": "first",
        "o_stl": "first",
        "o_to": "first",
        "o_blk": "first",
        "o_pf": "first",
        "offensive_accuracy": "first",
        "d_pts": "first",
        "d_oreb": "first",
        "d_dreb": "first",
        "d_asts": "first",
        "d_stl": "first",
        "d_to": "first",
        "d_blk": "first",
        "d_pf": "first",
        "deffensive_accuracy": "first",
        "points": "mean",
        "oRebounds": "mean",
        "dRebounds": "mean",
        "assists": "mean",
        "steals": "mean",
        "blocks": "mean",
        "turnovers": "mean",
        "PF": "mean",
        "dq": "mean",
        "fgAttempted": "mean",
        "fgMade": "mean",
        "ftAttempted": "mean",
        "ftMade": "mean",
        "threeAttempted": "mean",
        "threeMade": "mean",
        "PostPoints": "mean",
        "PostoRebounds": "mean",
        "PostdRebounds": "mean",
        "PostAssists": "mean",
        "PostSteals": "mean",
        "PostBlocks": "mean",
        "PostTurnovers": "mean",
        "PostPF": "mean",
        "PostDQ": "mean",
        "PostfgAttempted": "mean",
        "PostfgMade": "mean",
        "PostftAttempted": "mean",
        "PostftMade": "mean",
        "PostthreeAttempted": "mean",
        "PostthreeMade": "mean",
    }).reset_index()
    
    dataset['accuracy'] = (((dataset['fgMade'] / dataset['fgAttempted']) / 3) + ((dataset['ftMade'] / dataset['ftAttempted']) / 3) + ((dataset['threeMade'] / dataset['threeAttempted']) / 3)) * 100
    dataset['PostAccuracy'] = (((dataset['PostfgMade'] / dataset['PostfgAttempted']) / 3) + ((dataset['PostftMade'] / dataset['PostftAttempted']) / 3) + ((dataset['PostthreeMade'] / dataset['PostthreeAttempted']) / 3)) * 100

    dataset.drop(columns=["fgAttempted",
        "fgMade",
        "ftAttempted",
        "ftMade",
        "threeAttempted",
        "threeMade",
        "PostfgAttempted",
        "PostfgMade",
        "PostftAttempted",
        "PostftMade",
        "PostthreeAttempted",
        "PostthreeMade",], inplace=True)
    ###

    # Coaches
    if(year == 11):
        current_year_coaches = coaches_y11[coaches_y11['year'] == year][['year', 'coachID', 'tmID']]
    else:
        current_year_coaches = coaches[coaches['year'] == year][['year', 'coachID', 'tmID']]
    previous_year_coaches = coaches[coaches['year'] == (year - 1)][['coachID', 'matches', 'win_rate']]
    
    dataset_coaches = current_year_coaches.merge(previous_year_coaches, on='coachID', how='inner')

    coaches = coaches.sort_values(by=['coachID', 'year'])

    # Calculate the cumulative sum of awards received by each coach until year - 1
    coaches['coach_total_nrAwards'] = coaches.groupby('coachID')['nrAwards'].cumsum()

    award_info_until_year = coaches[coaches['year'] == (year - 1)][['coachID', 'coach_total_nrAwards']]

    dataset_coaches = dataset_coaches.merge(award_info_until_year, on='coachID', how='left')

    dataset_coaches['coach_matches'] = dataset_coaches['matches']
    dataset_coaches['coach_win_rate'] = dataset_coaches['win_rate']
    dataset_coaches.drop(columns=['coachID', 'matches', 'win_rate'], inplace=True)
    dataset = dataset.merge(dataset_coaches, on=['year', 'tmID'], how="left")

    dataset = dataset.fillna(0.0)
    dataset.rename(columns={'nrAwards': 'players_nrAwards'}, inplace=True)
    #print(dataset)
    
    dataset.to_csv(f'../data/datasets/dataset{year}.csv', index=False)
    

def datasets_creation():
    for i in range(2, 12):
        create_dataset(i)


datasets_creation()