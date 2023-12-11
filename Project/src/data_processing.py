import pandas as pd
import matplotlib.pyplot as plt

# Award Players data
def case_awards():
    awards_players_data = pd.read_csv("../data/raw/awards_players.csv")
    
    awards_players_data = awards_players_data.drop(["lgID"], axis=1)

    # Calculate the number of awards of each player per year
    awards_players_data['nrAwards'] = 1
    awards_players_data = awards_players_data.groupby(['playerID', 'year']).agg({
        'nrAwards': 'sum',
    }).reset_index()

    return awards_players_data

# Coaches data
def case_coaches():
    coaches_data = pd.read_csv("../data/raw/coaches.csv")

    coaches_data = coaches_data.drop(["lgID", "stint"], axis=1)

    # Make the numbers cumulative over the years
    def coach_data_apply(row: pd.Series) -> pd.Series:
        past_years_sum = coaches_data.loc[(coaches_data["coachID"] == row["coachID"]) & (coaches_data["year"] <= row["year"])].sum()
        row["current_season_wins"] = row["won"]
        row["current_season_losses"] = row["lost"]
        row["won"] = past_years_sum["won"]
        row["lost"] = past_years_sum["lost"]
        row["post_wins"] = past_years_sum["post_wins"]
        row["post_losses"] = past_years_sum["post_losses"]
        return row
    
    coaches_data = coaches_data.apply(coach_data_apply, axis=1)

    # Calculate stats
    coaches_data["current_season_matches"] = coaches_data["current_season_wins"] + coaches_data["current_season_losses"]
    coaches_data["current_season_win_rate"] = coaches_data["current_season_wins"] / coaches_data["current_season_matches"]
    coaches_data["current_season_win_rate"] = coaches_data["current_season_win_rate"].fillna(0.0)

    coaches_data["matches"] = coaches_data["won"] + coaches_data["lost"]
    coaches_data["win_rate"] = coaches_data["won"] / coaches_data["matches"]
    coaches_data["win_rate"] = coaches_data["win_rate"].fillna(0.0)

    coaches_data["post_matches"] = coaches_data["post_wins"] + coaches_data["post_losses"]
    coaches_data["post_win_rate"] = coaches_data["post_wins"] / coaches_data["post_matches"]
    coaches_data["post_win_rate"] = coaches_data["post_win_rate"].fillna(0.0)

    coaches_data = coaches_data.drop(["won", "lost", "post_wins", "post_losses", "current_season_wins", "current_season_losses"], axis=1)
    return coaches_data

# Players_Teams data
def case_players_teams():
    players_teams_data = pd.read_csv("../data/raw/players_teams.csv")

    duplicates = players_teams_data[players_teams_data.duplicated(subset=['playerID', 'year'], keep=False)]
    #print(duplicates)

    selected_columns_p_t = [
        "playerID",
        "year",
        "tmID",
        "points",
        "oRebounds",
        "dRebounds",
        "assists",
        "steals",
        "blocks",
        "turnovers",
        "PF",
        "dq",
        "fgAttempted","fgMade","ftAttempted","ftMade","threeAttempted","threeMade",
        "PostPoints",
        "PostoRebounds",
        "PostdRebounds",
        "PostAssists",
        "PostSteals",
        "PostBlocks",
        "PostTurnovers",
        "PostPF",
        "PostDQ",
        "PostfgAttempted","PostfgMade","PostftAttempted","PostftMade","PostthreeAttempted","PostthreeMade"
    ]

    players_teams_data = players_teams_data[selected_columns_p_t]
    
    return players_teams_data

# Players data
def case_players():
    players_data = pd.read_csv("../data/raw/players.csv")

    selected_columns = [
        "bioID",
        "pos",
    ]

    players_data = players_data[selected_columns]
    players_data.dropna(subset=['pos'], inplace=True)
    players_data = players_data.rename(columns={'bioID': 'playerID'})

    return players_data

# Series_Post data
def case_series_post():
    series_post_data = pd.read_csv("../data/raw/series_post.csv")
    series_post_data = series_post_data.drop(["lgIDWinner", "lgIDLoser"], axis=1)

# Teams_Post data
def case_teams_post():
    teams_post_data = pd.read_csv("../data/raw/teams_post.csv")

    teams_post_data = teams_post_data.drop(["lgID"], axis=1)
    teams_post_data.rename(columns={'W': 'postW', 'L': 'postL'}, inplace=True)

    return teams_post_data

# Teams data
def case_teams():
    teams_data = pd.read_csv("../data/raw/teams.csv")

    selected_columns = [
        "year", "tmID", "confID", "rank", "playoff", "finals", 
        "o_pts", "o_oreb", "o_dreb", "o_asts", "o_stl", "o_to", "o_blk", 
        "o_pf", "o_fgm", "o_fga", "o_ftm", "o_fta", "o_3pm", "o_3pa",
        "d_pts", "d_oreb", "d_dreb", "d_asts", "d_stl", "d_to", "d_blk",
        "d_pf", "d_fgm", "d_fga", "d_ftm", "d_fta", "d_3pm", "d_3pa",
        "won", "lost", "GP"
    ]

    teams_data = teams_data[selected_columns]

    return teams_data

# Players_Teams processed data
def players_teams_processed(awards_data, players_data, players_teams_data):
    players_teams_merged = pd.merge(players_teams_data, awards_data, on=['playerID', 'year'], how="left")
    # Merge between players_teams_data and players_data
    players_teams_merged = pd.merge(players_teams_merged, players_data, on='playerID', how='left')

    # checking for players that have played in the same year for different teams
    duplicates = players_teams_merged[players_teams_merged.duplicated(subset=['playerID', 'year'], keep=False)]
    #print(duplicates)

    players_teams_merged = players_teams_merged.groupby(['playerID', 'year']).agg({
        "tmID": "first",
        "pos": "first",
        "nrAwards": "first",
        "points": "sum",
        "oRebounds": "sum",
        "dRebounds": "sum",
        "assists": "sum",
        "steals": "sum",
        "blocks": "sum",
        "turnovers": "sum",
        "PF": "sum",
        "dq": "sum",
        "fgAttempted": "sum",
        "fgMade": "sum",
        "ftAttempted": "sum",
        "ftMade": "sum",
        "threeAttempted": "sum",
        "threeMade": "sum",
        "PostPoints": "sum",
        "PostoRebounds": "sum",
        "PostdRebounds": "sum",
        "PostAssists": "sum",
        "PostSteals": "sum",
        "PostBlocks": "sum",
        "PostTurnovers": "sum",
        "PostPF": "sum",
        "PostDQ": "sum",
        "PostfgAttempted": "sum",
        "PostfgMade": "sum",
        "PostftAttempted": "sum",
        "PostftMade": "sum",
        "PostthreeAttempted": "sum",
        "PostthreeMade": "sum",
    }).reset_index()

    players_teams_merged["nrAwards"] = players_teams_merged["nrAwards"].fillna(0)

    players_teams_merged.to_csv('../data/processed/players_teams_processed.csv', index=False)

# Teams processed data
def teams_processed(teams_data, teams_post_data):
    teams_post_data.rename(columns={'W': 'postW', 'L': 'postL'}, inplace=True)
    teams_merged = pd.merge(teams_data, teams_post_data, on=['tmID', 'year'], how='left')
    teams_merged["postW"] = teams_merged["postW"].fillna(0)
    teams_merged["postL"] = teams_merged["postL"].fillna(0)

    teams_merged['championship'] = teams_merged['finals'].apply(lambda x: 1 if x == 'W' else 0)
    teams_merged.drop(columns=['finals'], inplace=True)
    
    def team_data_apply(row: pd.Series) -> pd.Series:
        past_years_sum = teams_merged.loc[(teams_merged["tmID"] == row["tmID"]) & (teams_merged["year"] <= row["year"])].sum()
        row["season_wins"] = row["won"]
        row["season_losses"] = row["lost"]
        row["won"] = past_years_sum["won"]
        row["lost"] = past_years_sum["lost"]
        row["postW"] = past_years_sum["postW"]
        row["postL"] = past_years_sum["postL"]
        return row
    
    teams_merged = teams_merged.apply(team_data_apply, axis=1)
    teams_merged["matches"] = teams_merged["won"] + teams_merged["lost"]
    teams_merged["win_rate"] = teams_merged["won"] / teams_merged["matches"]
    teams_merged["win_rate"] = teams_merged["win_rate"].fillna(0.0)
    teams_merged["post_matches"] = teams_merged["postW"] + teams_merged["postL"]
    teams_merged["post_win_rate"] = teams_merged["postW"] / teams_merged["post_matches"]
    teams_merged["post_win_rate"] = teams_merged["post_win_rate"].fillna(0.0)
    
    # mean of attributes per game
    teams_merged["o_pts"] = teams_merged["o_pts"] / teams_merged["GP"]
    teams_merged["o_oreb"] = teams_merged["o_oreb"] / teams_merged["GP"]
    teams_merged["o_dreb"] = teams_merged["o_dreb"] / teams_merged["GP"]
    teams_merged["o_asts"] = teams_merged["o_asts"] / teams_merged["GP"]
    teams_merged["o_stl"] = teams_merged["o_stl"] / teams_merged["GP"]
    teams_merged["o_to"] = teams_merged["o_to"] / teams_merged["GP"]
    teams_merged["o_blk"] = teams_merged["o_blk"] / teams_merged["GP"]
    teams_merged["o_pf"] = teams_merged["o_pf"] / teams_merged["GP"]
    teams_merged["d_pts"] = teams_merged["d_pts"] / teams_merged["GP"]
    teams_merged["d_oreb"] = teams_merged["d_oreb"] / teams_merged["GP"]
    teams_merged["d_dreb"] = teams_merged["d_dreb"] / teams_merged["GP"]
    teams_merged["d_asts"] = teams_merged["d_asts"] / teams_merged["GP"]
    teams_merged["d_stl"] = teams_merged["d_stl"] / teams_merged["GP"]
    teams_merged["d_to"] = teams_merged["d_to"] / teams_merged["GP"]
    teams_merged["d_blk"] = teams_merged["d_blk"] / teams_merged["GP"]
    teams_merged["d_pf"] = teams_merged["d_pf"] / teams_merged["GP"]

    teams_merged['offensive_accuracy'] = (((teams_merged['o_fgm'] / teams_merged['o_fga']) / 3) + ((teams_merged['o_ftm'] / teams_merged['o_fta']) / 3) + ((teams_merged['o_3pm'] / teams_merged['o_3pa']) / 3)) * 100

    teams_merged['deffensive_accuracy'] = (((teams_merged['d_fgm'] / teams_merged['d_fga']) / 3) + ((teams_merged['d_ftm'] / teams_merged['d_fta']) / 3) + ((teams_merged['d_3pm'] / teams_merged['d_3pa']) / 3)) * 100

    # add to selected_columns this extra attributes
    selected_columns = [
        "year", "tmID", "confID", "playoff", "championship", "season_wins", "season_losses", "matches", "win_rate", "post_matches", "post_win_rate",
        "o_pts", "o_oreb", "o_dreb", "o_asts", "o_stl", "o_to", "o_blk", "o_pf", "offensive_accuracy",
        "d_pts", "d_oreb", "d_dreb", "d_asts", "d_stl", "d_to", "d_blk", "d_pf", "deffensive_accuracy"
    ]

    teams_merged = teams_merged[selected_columns]
    teams_merged.to_csv('../data/processed/teams_processed.csv', index=False)

# Coaches processed data
def coaches_processed(coaches_data, awards_coaches_data):
    awards_coaches_data.rename(columns={'playerID': 'coachID'}, inplace=True)

    coaches_data = coaches_data.merge(awards_coaches_data, on=['coachID', 'year'], how='left')
    coaches_data["nrAwards"] = coaches_data["nrAwards"].fillna(0.0)

    coaches_data.to_csv('../data/processed/coaches_processed.csv', index=False)

def performance_per_team():

    # Processing
    selected_player = 'smithka01w'
    players_teams_processed = pd.read_csv('../data/processed/players_teams_processed.csv')
    players_teams_processed = players_teams_processed[(players_teams_processed['playerID'] == selected_player)]
    selected_attributes = ['points', 'oRebounds', 'dRebounds', 'assists', 'steals', 'blocks', 'turnovers', 'PF']
    result = players_teams_processed[players_teams_processed['tmID'].isin(['DET', 'MIN'])].groupby('tmID')[selected_attributes].mean().reset_index()
    
    # Plot results
    labels = selected_attributes
    det_means = result[result['tmID'] == 'DET'][selected_attributes].values[0]
    min_means = result[result['tmID'] == 'MIN'][selected_attributes].values[0]

    x = range(len(labels))
    bar_width = 0.35
    det_positions = [pos - bar_width/2 for pos in x]
    min_positions = [pos + bar_width/2 for pos in x]

    plt.bar(det_positions, det_means, width=bar_width, label='DET', alpha=0.7)
    plt.bar(min_positions, min_means, width=bar_width, label='MIN', alpha=0.7)
    plt.xticks(x, labels, fontsize=7.5)

    plt.xlabel('Attributes')
    plt.ylabel('Mean per year played')
    plt.title(f"Mean performance of '{selected_player}' player")
    plt.legend(loc='upper right')
    plt.savefig("../data/plots/performance_per_team.png")
    plt.close()

def performance_intra_team(year, teams, attribute):
    
    players_teams_processed = pd.read_csv('../data/processed/players_teams_processed.csv')
    y_lim = 600

    for team in teams:
        team_data = players_teams_processed[(players_teams_processed['tmID'] == team) 
                                          & (players_teams_processed['year'] == year)]
        
        plt.bar(range(len(team_data)), team_data[attribute], tick_label='', label=f'Team {team}')
        plt.xlabel('Players')
        plt.ylabel(attribute)
        plt.ylim(0, y_lim)
        median_value = team_data[attribute].median()
        plt.title(f'Team {team} - Year {year} - Median {attribute}: {round(median_value, 1)}')
        plt.axhline(median_value, color='red', linestyle='--', label=f'Median {attribute}')
        plt.savefig(f'../data/plots/{attribute}_{team}_year{year}.png')
        plt.close()

def process_data():
    switch = {
        1: case_awards,
        2: case_coaches,
        3: case_players,
        4: case_players_teams,
        5: case_series_post,
        6: case_teams_post,
        7: case_teams
    }

    awards_players_data = switch.get(1)()
    coaches_data = switch.get(2)()
    players_data = switch.get(3)()
    players_teams_data = switch.get(4)()
    series_post_data = switch.get(5)()
    teams_post_data = switch.get(6)()
    teams_data = switch.get(7)()
    
    players_teams_processed(awards_players_data, players_data, players_teams_data)
    teams_processed(teams_data, teams_post_data)
    coaches_processed(coaches_data, awards_players_data)

    performance_per_team()
    performance_intra_team(year = 6, teams = ['MIN', 'DET'], attribute = 'points')

process_data()
