########################################
# Week 3.4: Analyzing Data With Python #
########################################

from sqlalchemy import create_engine
import sqlalchemy
import pandas
import matplotlib.pyplot as plt
import seaborn as sns

# creating a sql table from a DataFrame
engine = create_engine('sqlite://', echo=False)
chicago_socioeconomic_data = pandas.read_csv('https://data.cityofchicago.org/resource/jcxq-k9xf.csv')
chicago_socioeconomic_data.head()

chicago_socioeconomic_data.to_sql('chi_ses_data', con=engine)
engine.execute("SELECT * FROM chi_ses_data").fetchall()

#############
# Problem 1 #
#############

# descriptive stats
print(chicago_socioeconomic_data.describe(include='all'))
# 77 rows in the dataset

#############
# Problem 2 #
#############

# categorical scatterplot
plot = sns.swarmplot(x="community_area_name", y='hardship_index', data = chicago_socioeconomic_data)
plt.setp(plot.get_xticklabels(), rotation = 70)
plt.title('Community Area vs Hardship')
# plt.show()

# high hardship areas
high_hardship = chicago_socioeconomic_data[chicago_socioeconomic_data.hardship_index > 50]
print(high_hardship.describe(include='all'))
print(high_hardship['community_area_name'].describe())
# 38 community areas with high hardship

#############
# Problem 3 #
#############

# highest hardship_index
print(chicago_socioeconomic_data['hardship_index'].describe())
print(chicago_socioeconomic_data['hardship_index'].idxmax())

#############
# Problem 4 #
#############

# area with highest hardship_index
print(chicago_socioeconomic_data.at[53, 'community_area_name'])

#############
# Problem 5 #
#############

# higher income areas
higher_income = chicago_socioeconomic_data[chicago_socioeconomic_data.per_capita_income_ > 60000]
print(higher_income.describe(include='all'))
print(higher_income['community_area_name'].describe())
# 4 community areas with higher income than 60 k

#############
# Problem 6 #
#############

# scatterplot
g = sns.jointplot(x="per_capita_income_", y="hardship_index", data=chicago_socioeconomic_data)
plt.show()
# there is a clear inverse correlation between income and hardship























# in order to display plot within window
# plt.show()
