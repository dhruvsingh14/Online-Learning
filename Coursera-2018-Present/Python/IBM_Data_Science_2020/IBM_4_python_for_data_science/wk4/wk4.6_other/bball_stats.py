# pip install nba_api

from nba_api.stats.static import teams
nba_teams = teams.get_teams()
nba_teams[:5]

print(nba_teams)
