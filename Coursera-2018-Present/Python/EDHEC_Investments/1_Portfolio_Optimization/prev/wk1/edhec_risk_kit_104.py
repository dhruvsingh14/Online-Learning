#######################
# 1.4 Module Creation #
#######################
# import hello as h
# print(h.message)

import pandas as pd

def drawdown(return_series: pd.Series):
    # computes columns using time series data on returns
    wealth_index = 1000*(1+return_series).cumprod()
    previous_peaks = wealth_index.cummax()
    drawdowns = (wealth_index - previous_peaks)/previous_peaks
    # relabelling
    return pd.DataFrame({"Wealth": wealth_index,
                        "Previous Peak": previous_peaks,
                        "Drawdown": drawdowns})


def get_ffme_returns():
    # working to read in and analyze famma french data
    me_m = pd.read_csv("data/Portfolios_Formed_on_ME_monthly_EW.csv",
                        header=0, index_col=0, na_values=-99.99)
    rets = me_m[['Lo 10', 'Hi 10']]
    rets.columns = ['Smallcap', 'Largecap']
    rets = rets/100
    rets.index = pd.to_datetime(rets.index, format="%Y%m").to_period('M')
    return rets
































# plt.show() to display plots
