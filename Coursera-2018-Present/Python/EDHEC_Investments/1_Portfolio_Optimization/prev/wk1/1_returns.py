###############
# 1.1 Returns #
###############
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

prices = pd.read_csv("data\Stock_data.csv")
prices = prices.set_index('Date')
prices.head()

#################################
# Calculating Returns: Indexing #
#################################

# single stock returns
prices_a = prices['AAPL']
returns_a = (prices_a[1:].values/prices_a[:-1]) - 1

# likely going to be less than 1% changes from day to day
returns_a

# printing values excluding first row
prices.iloc[1:]

# printing values excluding last row
prices.iloc[:-1]

# calculating returns for both etfs
prices.iloc[1:].values/prices.iloc[:-1] - 1
prices.iloc[1:]/prices.iloc[:-1].values - 1
# calling values ensures that the dataframe doesn't automatically align rows

##############################
# Calculating Returns: Shift #
##############################
# shift moves yesterday's values one day forward
# that way we can divide directly today's value, by yesterday's
returns = prices/prices.shift(1) - 1
returns

#####################################
# Calculating % Returns: Pct Change #
#####################################
# percent change using a function across subsequent rows
returns = prices.pct_change()
print(returns)

# returns for apple are slightly higher than microsoft
print(returns.mean())

# volatility for apple is slightly higher than microsoft
print(returns.std())

# slightly crowded plot
returns.plot.bar()

# despite different price points, apple performs better over time
prices.plot()

#######################
# Compounding Returns #
#######################
# 1 + R format
print(returns + 1)

# multiplying returns to compute compund return
print(np.prod(returns + 1))

# alternate method of multiplying
print((returns + 1).prod())

# back into regular percent format
print((((returns + 1).prod() - 1)*100).round(2))
# apple is growing far more aggressively than microsoft

#######################
# Annualizing Returns #
#######################
# compunds the mean daily return for the entire year
rd_aapl = 0.002701
rd_msft = 0.001897

print((1 + rd_aapl) ** 252 - 1)
print((1 + rd_msft) ** 252 - 1)

# similary for monthly returns, we raise to the power of 30
# and for quarterly returns, to the power of 90









# plt.show() to display graphs














# plt.show() to display plots
