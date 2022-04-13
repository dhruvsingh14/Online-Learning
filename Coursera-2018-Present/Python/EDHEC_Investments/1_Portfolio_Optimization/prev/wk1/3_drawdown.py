################
# 1.3 Drawdown #
################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# definition: drawdown measures delta from a stock's peak
# typically in % format

# reading in close price feb 2020 - feb 2021
me_m = pd.read_csv("data\Stock_data_3.csv")
me_m = me_m.set_index('Date')

# expressing as % change
rets = me_m.pct_change()
rets

# dropping nas from first row of % change
rets = rets.dropna()
rets

# plotting returns variation
rets.plot.line()
# plt.show()

####################
# Formatting Index #
####################
# formatting index
rets.index = pd.to_datetime(rets.index)
rets.index

# checking monthly returns in 2008
rets["2008"]

# converting date format to monthly
rets.index = rets.index.to_period('M')
rets.head()

rets.info()
rets.describe()

#######################
# Computing Drawdowns #
#######################
# plotting only coca cola as an example
wealth_index = 1000*(1+rets["KO"]).cumprod()
wealth_index.plot()
plt.xticks(rets.index)
# plt.show()

# show max growth b/w 1980 and 1990
# plateau from 1990 to 2015
# and subsequent growth
previous_peaks = wealth_index.cummax()
previous_peaks.plot()
# plt.show()

# shows real dips and declines in performance of coca cola
# especially around the 2004 to 2009 era
drawdown = (wealth_index - previous_peaks)/previous_peaks
drawdown.plot()
# plt.show()

# checking global min
drawdown.min()

# arbitrary spot check
drawdown["1995"].plot()
# plt.show()

drawdown["1995"].min()

################################
# Creating a Drawdown Function #
################################

# creating a function to measure drawdown given time series data of returns
def drawdown(return_series: pd.Series):
    # computes columns using time series data on returns
    wealth_index = 1000*(1+return_series).cumprod()
    previous_peaks = wealth_index.cummax()
    drawdowns = (wealth_index - previous_peaks)/previous_peaks
    # relabelling
    return pd.DataFrame({"Wealth": wealth_index,
                        "Previous Peak": previous_peaks,
                        "Drawdown": drawdowns})

drawdown(rets["KO"]).head()

#################################
# Printing Max and Min Drawdown #
#################################

# printing lowest values for each of key metrics
print(drawdown(rets["KO"]).min())
print(drawdown(rets["PEP"]).min())

# printing period of lowest drawdown metrics
print(drawdown(rets["KO"])["Drawdown"].idxmin())
print(drawdown(rets["PEP"])["Drawdown"].idxmin())

# printing period of lowest drawdown for stated period
print(drawdown(rets["KO"]["1995":])["Drawdown"].idxmin())
print(drawdown(rets["PEP"]["1995":])["Drawdown"].idxmin())

# printing lowest drawdown for pepsi in stated period
print(drawdown(rets["PEP"]["1995":])["Drawdown"].min())





























# plt.show() to display plots
