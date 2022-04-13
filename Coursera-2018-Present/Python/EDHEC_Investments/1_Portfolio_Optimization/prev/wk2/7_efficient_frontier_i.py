##################################
# 1.7 Efficient Frontier: Part I #
##################################
import pandas as pd
import matplotlib.pyplot as plt
import edhec_risk_kit_107 as erk

# importing pharma data
phrma = pd.read_csv("data/Stock_data_6.csv", header=0,
                    index_col=0, parse_dates=True)

# changing metrics units
phrma = phrma.pct_change()
phrma = phrma.dropna()

# cleaning up index
phrma.index = phrma.index.to_period('M')

# checking columns and dimension
phrma.columns
# use phrma.columns.str.strip() to strip leading or trailing spaces
phrma.shape

# as expected Pfizer is furthest from its peak in '09, but also in '94, and '89
erk.drawdown(phrma["PFE"])["Drawdown"].plot.line()
plt.show()

erk.var_gaussian(phrma[["MRK", "ABT", "LLY"]], modified=True)
# MRK has the highest value at risk of these 3 above

# shows value at risk for big 7 pharma companies
erk.var_gaussian(phrma).sort_values().plot.bar()
plt.show()

###############################
# Sharpe Ratios of Big Pharma #
###############################
# danaher has the highest returns in excess of the risk free rate of return
print(erk.sharpe_ratio(phrma, 0.03, 12).sort_values())

# plotting sharpe ratios
erk.sharpe_ratio(phrma, 0.03, 12).sort_values().plot.bar(title="Pharma Sharpe Ratios 1985-2021")
plt.show()

# plotting sharpe ratios: since 2000
erk.sharpe_ratio(phrma["2000":], 0.03, 12).sort_values().plot.bar(title="Pharma Sharpe Ratios Since 2000")
plt.show()

################################
# Expected Returns, Covariance #
################################
# generating expected returns

# amgen has the highest expected returns for this period: 1995 to 2000
er = erk.annualize_rets(phrma["1995":"2000"], 12)
er.sort_values().plot.bar()
plt.show()

# storing covariance matrix
cov = phrma["1995":"2000"].cov()
print(cov.shape)




























# plt.show() to display plots
