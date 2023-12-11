# Notes of the problems

> ## Problems of year 10:
> - ATL on season 9 only won 4 games and lost 30 and on year 10 went to the playoffs
>   - This team only played on season 9 and 10
 
> ## Problem of year 4:
> - There is 2 new teams with no previous information

> ## General problems
> - Teams could have a huge difference on performance between years
>   - even with players information, the model gets confused (e.g year -> CLE was rank 1 year 2 && rank 7 year 3)
> - Some players have no information on previous seasons:
>   - even doing the mean performance of team's new players (where this new player(s) witout information doesn't count for the mean value)
>   - this player(s) could make a difference on the games 
>   - (e.g. catchta01 first year == 3, made a great performance, got an award and yet there was no information for her that year)
>       - that year, was the first year of IND at the playoffs and the model failed
