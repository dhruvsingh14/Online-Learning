#######################
# 1.9 Module Creation #
#######################
import pandas as pd
import numpy as np

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


def get_phrma_returns():
    """
    pharma stocks combined data
    """
    phrma = pd.read_csv("data/Stock_data_6.csv", header=0,
                        index_col=0, parse_dates=True)
    phrma = phrma.pct_change()
    phrma = phrma.dropna()
    phrma.index = phrma.index.to_period('M')
    return phrma

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


def semideviation(r):
    """
    returns semideviation
    takes series or dataframe as input
    """
    is_negative = r < 0
    return r[is_negative].std(ddof=0)

def var_historic(r, level=5):
    """
    returns var at x percentile level
    such that x percentile of fall below outputted value
    """
    if isinstance(r, pd.DataFrame):
        return r.aggregate(var_historic, level=level)
    elif isinstance(r, pd.Series):
        return -np.percentile(r, level)
    else:
        raise TypeError("Expected r to be a Series or a DataFrame")

def cvar_historic(r, level=5):
    """
    conditional variance of series or dataframe
    """
    if isinstance(r, pd.Series):
        is_beyond = r <= -var_historic(r, level=level)
        return -r[is_beyond].mean()
    elif isinstance(r, pd.DataFrame):
        return r.aggregate(cvar_historic, level=level)
    else:
        raise TypeError("Expected r to be a Series or a DataFrame")


from scipy.stats import norm
def var_gaussian(r, level=5, modified=False):
    """
    returns parametric gaussian var
    implements conditional logic for modification
    """
    # compute z score, assuming gaussian
    z = norm.ppf(level/100)
    if modified:
        # modifying z score based on 3rd and 4th moments
        s = skewness(r)
        k = kurtosis(r)
        z = (z +
                (z**2 - 1)*s/6 +
                (z**3 - 3*z)*(k-3)/24 -
                (2*z**3 - 5*z)*(s**2)/36
        )

    return -(r.mean() + z*r.std(ddof=0))

#############################
# 1.7: Efficient Frontier I #
#############################
# adding functions for returns, volatility, sharpe ratio

def annualize_rets(r, periods_per_year):
    """
    annualizes a set of returns
    """
    compound_growth = (1+r).prod()
    n_periods = r.shape[0]
    return compound_growth**(periods_per_year/n_periods)-1

def annualize_vol(r, periods_per_year):
    """
    annualizes volatility of a set of returns
    """
    return r.std()*(periods_per_year**0.5)

def sharpe_ratio(r, riskfree_rate, periods_per_year):
    """
    computes sharpe ratio
    """
    rf_per_period = (1+riskfree_rate)**(1/periods_per_year) - 1
    excess_ret = r - rf_per_period
    ann_ex_ret = annualize_rets(excess_ret, periods_per_year)
    ann_vol = annualize_vol(r, periods_per_year)
    return ann_ex_ret/ann_vol

##############################
# 1.8: Efficient Frontier II #
##############################
# weights are an Nx1 matrix
# covariance matrix is NxN matrix

def portfolio_return(weights, returns):
    """
    returns on a portfolio and weights multiplied in
    """
    return weights.T @ returns


def portfolio_vol(weights, covmat):
    """
    volatility of a portfolio from covariance matrix and weights multiplied in
    """
    return (weights.T @ covmat @ weights)**0.5

# function for plotting frontier
def plot_ef2(n_points, er, cov):
    """
    plots the 2 asset efficient frontier
    """
    if er.shape[0] != 2 or er.shape[0] !=2:
        raise ValueError("plot_ef2 can only plot 2-asset frontiers")
    weights = [np.array([w,1-w]) for w in np.linspace(0,1,n_points)]
    rets = [portfolio_return(w, er) for w in weights]
    vols = [portfolio_vol(w, cov) for w in weights]
    ef = pd.DataFrame({
        "Returns": rets,
        "Volatility": vols
    })
    return ef.plot.line(x="Volatility", y="Returns", style=".-")

###############################
# 1.9: Efficient Frontier III #
###############################

from scipy.optimize import minimize

def minimize_vol(target_return, er, cov):
    """
    return optimal weights for target return
    given expected returns and covariance matrix
    """
    n = er.shape[0]
    init_guess = np.repeat(1/n, n)
    bounds = ((0.0, 1.0),) * n # N-dim of 2 tuples
    #constraints
    weights_sum_to_1 = {'type': 'eq',
                        'fun': lambda weights: np.sum(weights) - 1
    }
    return_is_target = {'type': 'eq',
                        'args': (er,),
                        'fun': lambda weights, er: target_return - portfolio_return(weights, er)
    }
    weights = minimize(portfolio_vol, init_guess,
                        args=(cov,), method='SLSQP',
                        options={'disp': False},
                        constraints=(weights_sum_to_1, return_is_target),
                        bounds=bounds)
    return weights.x

# function for returning weights
def optimal_weights(n_points, er, cov):
    """
    """
    target_rs = np.linspace(er.min(), er.max(), n_points)
    weights = [minimize_vol(target_return, er, cov) for target_return in target_rs]
    return weights

# function for plotting
def plot_ef(n_points, er, cov):
    """
    plotting efficient frontier
    """
    weights = optimal_weights(n_points, er, cov)
    rets = [portfolio_return(w, er) for w in weights]
    vols = [portfolio_vol(w, cov) for w in weights]
    ef = pd.DataFrame({
            "Returns": rets,
            "Volatility": vols
    })
    return ef.plot.line(x="Volatility", y="Returns", style=".-")




































# plt.show() to display plots
