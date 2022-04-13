#######################
# 1.5 Module Creation #
#######################

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


def get_tech_stocks_returns():
    """
    tech stocks combined data
    """
    tech_stocks = pd.read_csv("data/Stock_data_4.csv", header=0,
                        index_col=0, parse_dates=True)
    tech_stocks = tech_stocks.pct_change()
    tech_stocks = tech_stocks.dropna()
    tech_stocks.index = tech_stocks.index.to_period('M')
    return tech_stocks

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

def kurtosis(r):
    """
    Alternate to scipy.stats.kurtosis()
    Computing kurtosis of Series or DataFrame
    Returns float or series
    """
    demeaned_r = r - r.mean()
    # using the pop std. dev, ie setting dof=0
    sigma_r = r.std(ddof=0)
    exp = (demeaned_r**4).mean()
    return exp/sigma_r**4


import scipy.stats
def is_normal(r, level=0.01):
    """
    Applying Jarque_Bera test to series in a dataframe, to determine normality
    Set to 1% level as default
    Returns true if normal hypothesis passes, otherwise false
    """
    if isinstance(r, pd.DataFrame):
        return r.aggregate(is_normal)
    else:
        statistic, p_value = scipy.stats.jarque_bera(r)
        return p_value > level
























# plt.show() to display plots
