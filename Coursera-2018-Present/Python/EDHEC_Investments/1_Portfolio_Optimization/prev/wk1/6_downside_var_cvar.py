##########################################
# 1.6 Downside: SemiDeviation, VaR, CVaR #
##########################################
import pandas as pd
import edhec_risk_kit_106 as erk
import matplotlib.pyplot as plt

# definition: semideviation is the volatility for negative returns
bank = erk.get_bank_returns()
print(bank.head())

#################
# Semideviation #
#################
# returns semideviation using two methods
erk.semideviation(bank)
bank[bank<0].std(ddof=0)

erk.semideviation(bank).sort_values()
# citibank has the highest semi deviation, wells fargo the lowest

# comparing with ffme portfolios
ffme = erk.get_ffme_returns()
print(erk.semideviation(ffme))
# running erk.semideviation([1,2,3,4]) will not work

#######
# VaR #
#######
# value at risk, or var, used to calculate risk exposure
# either for portfolios or positions, and to estimate potential losses

################
# Historic VaR #
################
import numpy as np
#np.percentile(bank, a= )

# this means 1% of returns have a volatility below returned value
print(erk.var_historic(bank, level=1))

##################################
# Conditional VaR aka Beyond VaR #
##################################
# accounts for tail risk
print(erk.cvar_historic(bank, level=1).sort_values)

# comparing with ffme portfolio
print(erk.cvar_historic(ffme))

###########################
# Parametric Gaussian VaR #
###########################
# estimates var by assuming normality
# then adding normalized, z-score at given percentile level * std deviation + to the mean
from scipy.stats import norm
norm.ppf(.5)
norm.ppf(.16)

# printing parametric gaussian var
print(erk.var_gaussian(bank))

# comparing with historic var method
print(erk.var_historic(bank))

###############################
# Cornish-Fisher Modification #
###############################
# done to adjust z-scores for non-normally distributed input variables

# comparing different methods side by side in a graph

var_table = [erk.var_gaussian(bank),
            erk.var_gaussian(bank, modified=True),
            erk.var_historic(bank)]
comparison = pd.concat(var_table, axis=1)
comparison.columns=['Gaussian', 'Cornish-Fisher', 'Historic']
comparison.plot.bar(title="4 Major Bank Returns: VaR at 5%")
plt.show()

print(erk.skewness(bank).sort_values(ascending=False))
# citibank and jp morgan are negatively skewed
# whereas bank of america and wells fargo are positively skewed












# plt.show() to display plots
