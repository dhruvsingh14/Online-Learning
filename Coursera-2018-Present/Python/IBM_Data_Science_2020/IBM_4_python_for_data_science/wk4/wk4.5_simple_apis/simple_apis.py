###############
# simple apis #
###############

# function to be used
def one_dict(list_dict):
    keys = list_dict[0].keys()
    out_dict={key: [] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict
# API: Application Programming Interface

# importing libraries
import pandas as pd
import matplotlib.pyplot as plt

# creating data dictionary
dict_={'a':[11,21,31], 'b':[12,22,32]}

# checking dataframe type
df=pd.DataFrame(dict_)
type(df)

# printing dataframe head, and mean of object
df.head()
df.mean()

#############
# rest apis #
#############

# importing libraries
from nba_api.stats.static import teams
import matplotlib.pyplot as plot

# fetching unique ids for teams
nba_teams = teams.get_teams()

# slicing
nba_teams[0:3]

# converting list to dictionary using one_dict function
dict_nba_team = one_dict(nba_teams)

# converting dictionary to dataframe
df_teams=pd.DataFrame(dict_nba_team)
df_teams.head()

# here we got the row that contains the dubs
df_warriors=df_teams[df_teams['nickname']=='Warriors']
df_warriors

# extracting warriors id
id_warriors=df_warriors[['id']].values[0][0]
id_warriors

# using another aspect of the nba_api
from nba_api.stats.endpoints import leaguegamefinder

# requesting the json file underlying nba api/ warriors
gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)
# print(gamefinder.get_json())

# building on prev chunk - extracting df for warriors
games = gamefinder.get_data_frames()[0]
games.head()

# this wget code doesn't run as is - the % sign throws an error
#import wget
#! wget https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl

# manually downloading and working with pkl files
file_name = "Golden_State.pkl"
games = pd.read_pickle(file_name)
games.head()

# analyzing away and home games for warriors vs raptors
games_home = games [games ['MATCHUP']=='GSW vs. TOR']
games_away = games [games ['MATCHUP']=='GSW @ TOR']

# calculating mean for home and away games
games_home.mean()['PLUS_MINUS']
games_away.mean()['PLUS_MINUS']

# really nice plot here, line graph
fig, ax = plt.subplots()

games_away.plot(x='GAME_DATE', y='PLUS_MINUS', ax = ax)
games_home.plot(x='GAME_DATE', y='PLUS_MINUS', ax = ax)
ax.legend(["away", "home"])
plt.show()























# in order to display plot within window
# plt.show()
