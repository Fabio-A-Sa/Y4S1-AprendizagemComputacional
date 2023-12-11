# Data Preparation - creation of datasets for training and testing

This file describes the content added to our finals datasets used for the modeling part.

## Data of Pre-Season:

### Teams
- tmID
- year
- confID
- playoff -> attribute to guess

### Players_Teams:
- playerID
- tmID
- year

### Coaches:
- coachID
- year
- tmID

## Data of last Season:

### Teams

- season_wins - last season wins
- season_losses - last season losses
- matches - total number of matches
- win_rate - total number of wins relatively to the total number of matches
- post_matches - total number of post matches
- post_win_rate - total number of post wins relatively to the total number of post matches
- total_championships - total number of championships won by the team until the year of the dataset
- players_nrAwards - total number of players awards received on season before
- ``team_stats``

### Team_stats (mean of each attribute for the number of games played)
- o_pts
- o_oreb
- o_dreb
- o_asts
- o_stl
- o_to
- o_blk
- o_pf
- offensive_accuracy
- d_pts
- d_oreb
- d_dreb
- d_asts
- d_stl
- d_to
- d_blk
- d_pf
- deffensive_accuracy

### Players_Teams: (of each player)
- points
- oRebounds
- dRebounds
- assists
- steals
- blocks
- turnovers
- PF
- dq
- PostPoints
- PostoRebounds
- PostdRebounds
- PostAssists
- PostSteals
- PostBlocks
- PostTurnovers
- PostPF
- PostDQ
- accuracy
- PostAccuracy

>__IMPORTANT:__ When creating the dataset we joined this values by the tmID and did its sum when grouping. After that, for every attribute we made the mean of that value per number of players. We did this approach because we do not have every player information of the previous year (could be a new player) and it's not fair that a team has better stats just because we do not have all the players information and that could mislead the model.

### Coaches:
- coach_total_nrAwards - total number of awards of that coach until the year of the dataset
- coach_matches - total number of matches of a coach
- coach_win_rate - total number of wins relatively to the total number of matches of a coach
