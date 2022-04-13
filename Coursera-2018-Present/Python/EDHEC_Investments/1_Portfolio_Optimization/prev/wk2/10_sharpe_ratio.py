#####################
# 1.10 Sharpe Ratio #
#####################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import edhec_risk_kit_110 as erk

# importing pharma data
cnsmr = erk.get_cnsmr_returns()
er = erk.annualize_rets(cnsmr["1996":"2000"], 12)
cov = cnsmr["1996":"2000"].cov()

# now, instead of assigning weights given target rate of return
# we maximize weights given the risk free rate of return

ax = erk.plot_ef(20, er, cov)
plt.show()
print(ax.set_xlim(left = 0))

# plotting efficient frontier, with added tangent line
ax = erk.plot_ef(20, er, cov)
ax.set_xlim(left = 0)

# getting max sharpe ratio
rf = 0.1 # setting risk free rate of return to 10%
w_msr = erk.msr(rf, er, cov)
r_msr = erk.portfolio_return(w_msr, er)
vol_msr = erk.portfolio_vol(w_msr, cov)

# add CML
cml_x = [0, vol_msr]
cml_y = [rf, r_msr]
ax.plot(cml_x, cml_y, color='green', marker='o', linestyle='dashed', linewidth=2, markersize=12)
plt.show()


# weights of msr maximizing portfolio
print(w_msr)

# printing returns and volatility of msr maximizing porforlio
print(r_msr, vol_msr)


erk.plot_ef(20, er, cov, style='-', show_cml=True, riskfree_rate=0.1)
plt.show()

# note consider spending some trying to interpret this before moving on to the next lab














# plt.show() to display plots
