## 1 - Data understanding

### 1.1 - Awards Players Data

#### Relevant columns:
- Player ID
- Award
- Year

#### Colums to remove:
- Lg ID

#### Notes about columns:
- Lg ID is always WNBA

Awards rank and description:
1) Most Valuable Player (MVP): The MVP award is typically considered the most prestigious individual honor in women's basketball, recognizing the player who has had the greatest impact on her team's success during the season.
2) Defensive Player of the Year: This award acknowledges a player's exceptional defensive skills and contributions to her team's defensive success, making it one of the highly respected awards.
3) Coach of the Year: The Coach of the Year award recognizes the head coach who has demonstrated outstanding leadership and coaching skills, leading her team to success during the season.
4) Rookie of the Year: This award goes to the best-performing first-year player in the league, highlighting emerging talent and potential for the future.
5) WNBA Finals Most Valuable Player: This award is given to the player who performs exceptionally well during the WNBA Finals, making a significant impact on her team's championship run.
6) Sixth Woman of the Year: This award acknowledges the best player who primarily comes off the bench as a substitute, recognizing her valuable contributions in a reserve role.
7) Most Improved Player: The Most Improved Player award highlights a player who has made significant progress and improvement in her performance compared to previous seasons.
8) Kim Perrot Sportsmanship Award: This award recognizes a player's sportsmanship, character, and integrity on and off the court.
9) All-Star Game Most Valuable Player: While it's an honor to be named the All-Star Game MVP, it's generally not as highly regarded as some of the other awards on this list, as it's a single-game accolade.
10) WNBA All Decade Team: Being named to the WNBA All Decade Team is a significant recognition of a player's impact over a decade, but it's not an annual award.
11) WNBA All Decade Team Honorable Mention: This is a recognition of a player's contributions over a decade but falls below being named to the actual All-Decade Team in terms of prestige.

### 1.2 - Coaches Data

#### Relevant columns:
- Coach ID
- Year
- Tm ID (Team)
- Won
- Lost
- Post_wins
- Post_losses

#### Colums to remove:
- Lg ID (is always WNBA)
- Stint

#### Notes about columns:
- Stint refers to the period of time that a coach serves in a particular coaching position or role during a determined season or over the course of their coaching career.

### 1.3 - Players Teams

#### Relevant columns

- playerID
- year
- tmID - team ID

- points
- oRebounds - offensive rebounds
- dRebounds - defensive rebounds
- assists
- steals
- blocks
- turnovers
- PF
- dq

- fgAttempted - field goal attemps
- fgMade - field goal
- ftAttempted - free throw attemps
- ftMade - free throw
- threeAttempted - tree point attemps
- threeMade - tree point

- PostPoints
- PostoRebounds
- PostdRebounds
- PostAssists
- PostSteals
- PostBlocks
- PostTurnovers

- PostfgAttempted
- PostfgMade
- PostftAttempted
- PostftMade
- PostthreeAttempted
- PostthreeMade
- PostPF
- PostDQ


#### Columns to remove
- GP - games played (a player with more GP will have more relevant stats)
- minutes (same as the GP)
- GS - games started, so GP >= GS always
- rebounds = oRebounds + dRebounds
- stint - time periods in game
- lgID - same value
- PostGP
- PostMinutes
- PostGS
- PostRebounds = PostoRebounds + PostdRebounds


#### Notes about columns

- Some columns are being removed because are neither relevant or could be measured with other values

### 1.4 - Players Data

#### Relevant columns:
- Bio ID
- Pos

#### Columns to remove
- Firstseason (always 0)
- Lastseason (always 0)
- Height (irrelevant to the purpose)
- Weight (irrelevant to the purpose)
- Birth Date (irrelevant to the purpose)
- Death Date (irrelevant to the purpose)
- College (irrelevant to the purpose)
- College Other (irrelevant to the purpose)

#### Notes about columns:
Description of each position (Pos):
- __Centers (C):__ 
    - Centers are often responsible for scoring in the paint, blocking shots, and grabbing rebounds. Assign higher weights to points (especially close-range), blocks, and rebounds.
- __Forwards (F):__
    - Forwards are versatile players who contribute both inside and outside. Assign balanced weights to points, rebounds, assists, and defensive stats.
- __Guards (G):__ 
    - Guards are responsible for ball handling, playmaking, and perimeter scoring. Assign higher weights to assists, steals, and perimeter shooting stats (e.g., three-pointers).
- __F-C (Forward-Center):__
    - This position combines the roles of a forward and a center.
    - Assign relatively balanced weights for scoring (points), both offensive and defensive rebounds, and blocks. These players are typically expected to contribute in both scoring and rebounding, including shot-blocking.
- __F-G (Forward-Guard):__
    - This position combines the roles of a forward and a guard.
    - Assign weights that reflect a balance between scoring, rebounding, assists, and perimeter defense. These players have the versatility to play inside and outside.
- __G-F (Guard-Forward):__
    - Similar to F-G, this position combines the roles of a guard and a forward.
    - Assign weights that reflect a balance between scoring, rebounding, assists, perimeter defense, and ball-handling. These players can handle the ball and play in various positions.
- __C-F (Center-Forward):__
    - This position combines the roles of a center and a forward.
    - Assign weights that emphasize scoring in the paint, rebounding, and shot-blocking, similar to the center position, but with some additional versatility for playing outside.


### 1.5 - Series Post Data

#### Relevant columns:
- Year
- Tm IDWinner
- Tm IDLoser
- W
- L

#### Colums to remove:
- Round
- Series
- Lg IDWinner (always WNBA)
- Lg IDLoser (always WNBA)

### 1.6 Teams Post Data

#### Relevant columns:
- Year
- Tm ID
- W
- L

#### Colums to remove:
- Lg ID (always WNBA)

### 1.7 Teams Data

#### Columns Description:
- "year": The year in which the data corresponds to, typically the season year.
- "lgID": League identifier, which specifies the league to which the team belongs.
- "tmID": Team identifier, a unique code or abbreviation representing each team.
- "franchID": Franchise identifier, indicating the franchise to which the team belongs.
- "confID": Conference identifier, denoting the conference to which the team is affiliated.
- "divID": Division identifier, indicating the division to which the team is assigned.
- "rank": The team's ranking at the end of the season.
- "playoff": Indicates whether the team made it to the playoffs (1 for yes, 0 for no).
- "seeded": If the team made it to the playoffs, this column may specify the playoff seed.
- "firstRound": Indicates whether the team advanced to the first round of the playoffs (1 for yes, 0 for no).
- "semis": Indicates whether the team advanced to the semifinals of the playoffs (1 for - yes, 0 for no).
- "finals": Indicates whether the team advanced to the finals of the playoffs (1 for yes, 0 for no).
- "name": The name of the basketball team.
- "o_fgm": Offensive field goals made.
- "o_fga": Offensive field goals attempted.
- "o_ftm": Offensive free throws made.
- "o_fta": Offensive free throws attempted.
- "o_3pm": Offensive three-pointers made.
- "o_3pa": Offensive three-pointers attempted.
- "o_oreb": Offensive rebounds.
- "o_dreb": Defensive rebounds.
- "o_reb": Total rebounds.
- "o_asts": Assists.
- "o_pf": Personal fouls committed.
- "o_stl": Steals.
- "o_to": Turnovers.
- "o_blk": Blocks.
- "o_pts": Total points scored by the team's offense.
- "d_fgm": Defensive field goals made against the team.
- "d_fga": Defensive field goals attempted against the team.
- "d_ftm": Defensive free throws made against the team.
- "d_fta": Defensive free throws attempted against the team.
- "d_3pm": Defensive three-pointers made against the team.
- "d_3pa": Defensive three-pointers attempted against the team.
- "d_oreb": Defensive rebounds collected against the team.
- "d_dreb": Defensive rebounds allowed by the team.
- "d_reb": Total rebounds allowed by the team.
- "d_asts": Assists allowed by the team's defense.
- "d_pf": Personal fouls committed by the team's defense.
- "d_stl": Steals by the team's defense.
- "d_to": Turnovers by the team's defense.
- "d_blk": Blocks by the team's defense.
- "d_pts": Total points scored by the team's opponents.
- "tmORB": Total team offensive rebounds.
- "tmDRB": Total team defensive rebounds.
- "tmTRB": Total team rebounds.
- "opptmORB": Total offensive rebounds by the opposing teams.
- "opptmDRB": Total defensive rebounds by the opposing teams.
- "opptmTRB": Total rebounds by the opposing teams.
- "won": The number of games won by the team in the season.
- "lost": The number of games lost by the team in the season.
- "GP": Total games played by the team in the season.
- "homeW": The number of home games won by the team.
- "homeL": The number of home games lost by the team.
- "awayW": The number of away games won by the team.
- "awayL": The number of away games lost by the team.
- "confW": The number of conference games won by the team.
- "confL": The number of conference games lost by the team.
- "min": Total minutes played by the team in the season.
- "attend": Average attendance at the team's games.
- "arena": The name of the arena where the team plays its home games.

#### Relevant columns:
- Year
- Tm ID
- Conf ID
- Rank
- Playoff
- Finals
- __OFFENSIVE__
    - O_oreb: Offensive rebounds.
    - O_dreb: Defensive rebounds.
    - O_asts.
    - O_to: Turnovers.
    - O_blk: Blocks.
    - O_stl.
    - O_pts: Total points scored by the team's offense.
    - O_pf: Personal fouls committed.
    - O_fgm: Offensive field goals made.
    - O_fga: Offensive field goals attempted.
    - O_ftm: Offensive free throws made.
    - O_fta: Offensive free throws attempted.
    - O_3pm: Offensive three-pointers made.
    - O_3pa: Offensive three-pointers attempted.
- __DEFENSIVE__
    - D_dreb: Defensive rebounds allowed by the team.
    - D_oreb: Total rebounds allowed by the team.
    - D_asts.
    - D_to: Turnovers by the team's defense.
    - D_blk: Blocks by the team's defense.
    - D_stl.
    - D_pf: Personal fouls committed by the team's defense.
    - D_pts: Total points scored by the team's opponents.
    - D_fgm: Defensive field goals made against the team.
    - D_fga: Defensive field goals attempted against the team.
    - D_ftm: Defensive free throws made against the team.
    - D_fta: Defensive free throws attempted against the team.
    - D_3pm: Defensive three-pointers made against the team.
    - D_3pa: Defensive three-pointers attempted against the team.
- Won
- Lost

#### Colums to remove:
- Lg ID - always wnba
- Franch ID - equals to Tm ID
- Div ID - empty
- Seeded - always 0
- Name - same identifier as Tm ID
- ... (rest of offensive and defensive)
- Tm ORB - always 0
- Tm DRB - always 0
- Tm TRB - always 0
- Opptm ORB - always 0
- Opptm DRB - always 0
- Opptm TRB - always 0
- Home W
- Home L
- Away W
- Away L
- GP - games played can be calculated with Won and Lost
- Conf W 
- Conf L
- Min - almost the same for every team
- Arena - arena seems irrelevant to the purpose
- First Round
- Semis

#### Notes about columns:
- Tm ID - there is teams that didnt participate in the last years of wnba -> (CHA)
- First Round / Semis / Finals = empty -> team didn't make it there
- Sometimes there is a Win on the 'First Round' and no data on the 'Semis' and 'Final' colums - firstly that's assume a Lost there. 