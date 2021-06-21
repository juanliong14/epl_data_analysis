# epl_data_analysis
Data Analysis on how English Premier League (EPL) team perform before and after covid-19

## Introduction
The objective is to analyze English Premier League (EPL) match data from 2018/2019 to 2020/2021 season and make comparison of match statistics for period before and after covid-19. Each match data and statistics were scrapped from **[premierleague.com](https://www.premierleague.com/)**.

Preliminary research information : 
* 2018 / 2019 season —> match ID 38308 to 38687
* 2019 / 2020 season —> match ID 46605 to 46984
* 2020 / 2021 season —> match ID 58897 to 59275
* last match before covid-19 suspension = Leicester vs Aston Villa 10 March 2020 (match ID 46889)
* first match before covid-19 suspension = Aston Villa vs Sheffield United 18 June 2020 (match ID 46875)

## Data required for analysis
* Match Date
* Home Team Name
* Away Team Name
* Home/Away FT Score
* Home/Away Possession
* Home/Away Shots On Target
* Home/Away Shots
* Home/Away Points

## Questions for analysis
* Due to covid-19, how home crowd absence have impacted EPL match stats? Did the absence of the crowd in the stadium affect team performance (in decline or incline) when playing at home? (May have neglected effect of VAR introduction)
    * Home/Away Possession
    * Home/Away Shots on Target
    * Home/Away Shots
    * Home/Away Goals Scored per Game
    * Home/Away Win Rate
    * Home/Away Points per Game

* Performance Metrics Definition :
    * Shot on Target % = Shots on Target / Shots (Home/Away)
    * Quantity Conversion Rate = Goals / Shots (Home/Away)
    * Quality Conversion Rate  = Goals / Shots on Target (Home/Away)
    * Win Rate = No. of win / No. of games (Home/Away)
    * Points per game (Ppg) = Average points/game (Home / Away)

* Relation of Ball Possession % vs Goal Conversion Rate
* Made an similar analysis starting from 2019/2020 season (the introduction of VAR) but the sample size is too small and possible for imbalance data sampling.
* Compare the performance metrics between "big-6" and "non big-6" teams before and after covid-19. (note : Big-6 = "Manchester United", "Manchester City", "Liverpool", "Arsenal", "Chelsea", "Tottenham Hotspurs")
