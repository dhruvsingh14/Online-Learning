#################################
# 1.5 Deviations from Normality #
#################################
import pandas as pd
import edhec_risk_kit_105_2 as erk

tech_stocks = erk.get_tech_stocks_returns()
tech_stocks.head()

############
# Skewness #
############
# printing mean vs. median to get a sense of dispersion
pd.concat([tech_stocks.mean(), tech_stocks.mean(), tech_stocks.median() > tech_stocks.median()], axis=1)

# mean > median implies positive skew
def skewness(r):
    """
    Alternate to scipy.stats.skew()
    Computing skewness of Series or DataFrame
    Returns float or series
    """
    demeaned_r = r - r.mean()
    # using the pop std. dev, ie setting dof=0
    sigma_r = r.std(ddof=0)
    exp = (demeaned_r**3).mean()
    return exp/sigma_r**3

# printing skewness of columns
skewness(tech_stocks).sort_values()
# all the tech stocks here are positively skewed

# checking if this aligns with scipy's inbuilt function
import scipy.stats

scipy.stats.skew(tech_stocks)
tech_stocks.shape
# adobe is more heavily positively skewed than it's two competitors

# testing skewness for randomly generated normal sequence of same length
import numpy as np
normal_rets = np.random.normal(0, 0.15, (373, 1))

# skewness something in the vicinity of |+/- 0.1|
normal_rets.mean(), normal_rets.std()
erk.skewness(normal_rets)


############
# Kurtosis #
############
# same formula as skewness, 4th power instead of 3rd
print(erk.kurtosis(tech_stocks))
# adobe has fatter tails, in distribution, so more outliers
# cisco and oracle, are relatively tamer stocks

# testing against scipy inbuilt function
print(scipy.stats.kurtosis(tech_stocks))
# these are lower by 3, since the scipy function returns excess kurtosis

# testing kurtosis for randomly generated series
print(scipy.stats.kurtosis(normal_rets))
print(erk.kurtosis(normal_rets))
# something in the vicinity of |+/- 3.0| is considered normal kurtosis

##################################
# Jarque-Bera Test for Normality #
##################################
# using scipy on randomly generated series
print(scipy.stats.jarque_bera(normal_rets))

# running on dataframe doesn't work
print(scipy.stats.jarque_bera(tech_stocks))

# using function to rerun normality test
print(erk.is_normal(normal_rets))
print(tech_stocks.aggregate(erk.is_normal))

# testing normality in tech_stocks and in random series
import pandas as pd
print(isinstance(tech_stocks, pd.DataFrame))
print(erk.is_normal(normal_rets))






































# plt.show() to display plots
