###########################
# 1.2 Volatility and Risk #
###########################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# reading in close price feb 2020 - feb 2021
prices = pd.read_csv("data\Stock_data_2.csv")
prices = prices.set_index('Date')

# expressing as % change
returns = prices.pct_change()
returns

# dropping nas from first row of % change
returns = returns.dropna()
returns

#####################################################
# calculating population standard deviation by hand #
#####################################################
deviations = returns - returns.mean()
squared_deviations = deviations**2
mean_squared_deviations = squared_deviations.mean()

# ATT is slightly more volatile than Verizon
volatility = np.sqrt(mean_squared_deviations)
volatility

##########################################################
# calculating standard deviation using in-built function #
##########################################################
# the in-built function calculates sample std by default
returns.std()

#################################################
# calculating sample standard deviation by hand #
#################################################
# printing and extracting dim
returns.shape
number_of_obs = returns.shape[0]

# calculating sample std by hand
mean_squared_deviations = squared_deviations.sum()/(number_of_obs - 1)
volatility = np.sqrt(mean_squared_deviations)
volatility

# checking against function output
returns.std()
# matches up now

##########################
# annualizing volatility #
##########################
# annualizing volatility of a daily series
annualized_vol = returns.std()*(252**0.5)
annualized_vol

# annualized returns reflects a smaller gap
# but great volatility in ATT than Verizon

#########################
# risk adjusted returns #
#########################
# plotting percent changes in both stocks
returns.plot()
# plt.show()
# att while moving in tandem with verizon
# swings wildly outside of the range of verizon

# same as before
annualized_vol = returns.std()*np.sqrt(252)
annualized_vol

# interersting to see verizon daily net over this period is great than att
n_days = returns.shape[0]
return_per_day = (returns+1).prod()**(1/n_days) - 1
return_per_day

# verizons annualized retruns over this period is greater than att's
annualized_return = (return_per_day + 1)**252-1
annualized_return = (returns+1).prod()**(252/n_days) - 1
annualized_return

# adjusting returns by risk
annualized_return/annualized_vol

# setting hypothetical riskfree rate of return to 3 %
riskfree_rate = 0.03
excess_return = annualized_return - riskfree_rate
sharpe_ratio = excess_return / annualized_vol
print(sharpe_ratio)









































# plt.show() to display plots
