# importing pandas
import pandas as pd

################
# pandas intro #
################

# importing data
csv_path = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.csv"
df = pd.read_csv(csv_path)

# printing top few rows
df.head()

# now reading an excel file of same data directly from the web
xlsx_path = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx"

# assigning and printing artist database
df = pd.read_excel(xlsx_path)
df.head()

# now, fetching a column and assigning it to a new data frame
x = df[['Length']]
x

###############################
# viewing and accessing data  #
###############################
# assigning a column as a series instead of a dataframe
x = df['Length']
x

# assigning column as dataframe, pulled using colname
x = type(df[['Artist']])
x

# grabbing multiple columns by name
y = df[['Artist', 'Length', 'Genre']]
y

# pulling values and numbers using indices
df.iloc[0,0]
df.iloc[1,0]
df.iloc[0,2]

# likewise, using loc function to pull values by colname
df.loc[0, 'Artist']
df.loc[1, 'Artist']
df.loc[0, 'Released']
df.loc[1, 'Released']

# slicing aka subsetting, using colons as shorthand for series or array
df.iloc[0:2, 0:3]
df.loc[0:2, 'Artist':'Released']

#########
# quiz  #
#########
y = df[['Artist', 'Length', 'Genre']]
y

# ix function: throws error
# df.ix[1,0]

# pandas series
x = df['Length']
x
