# AC Project

Basketball tournaments are usually split in two parts. First, all teams play each other aiming to achieve the greatest number of wins possible. Then, at the end of the first part of the season, a pre determined number of teams which were able to win the most games are qualified to the playoff season, where they play series of knock-out matches for the trophy.

For the 10 years, data from players, teams, coaches, games and several other metrics were gathered and arranged on this dataset. The goal is to use this data to predict which teams will qualify for the playoffs in the next season.

### Data Description

The data about the players, teams and coaches consist of following relations:

- relation `awards_players` (96 objects) - each record describes awards and prizes received by players across 10 seasons,
- relation `coaches` (163 objects) - each record describes all coaches who've managed the teams during the time period,
- relation `players` (894 objects) - each record contains details of all players,
- relation `players_teams` (1877 objects) - each record describes the performance of each player for each team they played,
- relation `series_post` (71 objects) - each record describes the series' results,
- relation `teams` (143 objects) - each record describes the performance of the teams for each season,
- relation `teams_post` (81 objects) - each record describes the results of each team at the post-season.

![database](/img/database.png)

### Run

```bash
$ git clone https://github.com/iamaccosta/AC_Project.git
$ cd src/
$ make
```

### Year 11 Results

Results of Year 11 can be found [here](./data/predictions/year_11/), being the best results inside of the folder [rfc](./data/predictions/year_11/rfc/all_years_11.csv) with all years approach.

### Report and Presentation

- [Here](https://docs.google.com/presentation/d/14UmIh1qYh3DtgEQ_hWkun7svLKL1jTvGoPtgYhGLV4I/edit#slide=id.p)

### Members:

- André Costa - up201905916@fe.up.pt
- Diogo Fonte - up202004175@fe.up.pt
- Fabio Sá - up202007658@fe.up.pt
- Joaquim Monteiro - up201905257@fe.up.pt

#### G53, 2023/24