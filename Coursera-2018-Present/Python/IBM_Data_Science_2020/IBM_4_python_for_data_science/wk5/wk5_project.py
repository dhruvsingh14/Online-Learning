##############
# numpy prep #
##############

# importing libraries
import pandas as pd
from bokeh.plotting import figure, output_file, show, output_notebook
output_notebook

##############################
# writing dashboard function #
##############################

def make_dashboard(x, gdp_change, unemployment, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend="% unemployed")
    show(p)

# setting links using dictionary

links = {'GDP': 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',\
    'unemployment': 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}

###############
# Question 1: #
###############
# Create a dataframe that contains the GDP data and
# display the first five rows of the dataframe.

# pulling data from online platform
x = pd.read_csv(links["GDP"])
print(x.head())

###############
# Question 2: #
###############
# Create a dataframe that contains the unemployment data.
# Display the first five rows of the dataframe.
x2 = pd.read_csv(links["unemployment"])
print(x2.head())

###############
# Question 3: #
###############
# Display a dataframe where unemployment was greater than 8.5%.
print(x2[x2.unemployment > 8.5])

###############
# Question 4: #
###############
# Use the function make_dashboard to make a dashboard

# Create a dataframe with column date
x_copy = x
x = x.date

# Create a dataframe with column change-current
# rename change-current to changecurrent
x_copy.rename(columns={'change-current': 'changecurrent'}, inplace=True)
gdp_change = x_copy.changecurrent

# Create a dataframe with column unemployment
unemployment = x2.unemployment

# Give your dashboard a string title
title = "US Economy Present Status"

file_name = "US_Economy.html"

# Fill up the parameters in the following function:
make_dashboard(x=x, gdp_change=gdp_change, unemployment=unemployment,
            title=title, file_name=file_name)
















# in order to display plot within window
# plt.show()
