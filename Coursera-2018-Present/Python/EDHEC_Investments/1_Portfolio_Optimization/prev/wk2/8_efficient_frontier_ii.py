###################################
# 1.8 Efficient Frontier: Part II #
###################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import edhec_risk_kit_108 as erk

# importing pharma data
phrma = erk.get_phrma_returns()
er = erk.annualize_rets(phrma["1996":"2000"], 12)
cov = phrma["1996":"2000"].cov()

l = ["MRK", "ABT", "LLY", "AMGN"]

# running subsets of expected returns and covariance matrices
er[l]
cov.loc[l,l]

# generating weights
ew = np.repeat(0.25, 4)

# printing risk-returns
print(erk.portfolio_return(ew, er[l]))
print(erk.portfolio_vol(ew, cov.loc[l,l]))
# return of 25%, volatility of 5%

####################
# The 2-Asset Case #
####################
# taking a simplified, 'special case' version of the model
# generating weights using list comprehension
n_points = 20
weights = [np.array([w,1-w]) for w in np.linspace(0,1,n_points)]

# printing specs
print(type(weights))
print(len(weights))

print(weights[0])
print(weights[4])
print(weights[19])
# shows complementary weights

# testing
l = ["AMGN", "MRK"]

rets = [erk.portfolio_return(w, er[l]) for w in weights]
vols = [erk.portfolio_vol(w, cov.loc[l,l]) for w in weights]
ef = pd.DataFrame({"R": rets, "V": vols})
ef.plot.scatter(x="V", y="R")
plt.show()

# calling plotting function
l = ["BMY", "ABT"]
erk.plot_ef2(25, er[l].values, cov.loc[l,l])
plt.show()



































# plt.show() to display plots
