##################################################
# 1.9 Efficient Frontier: Part III, Optimization #
##################################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import edhec_risk_kit_109 as erk

# importing pharma data
phrma = erk.get_phrma_returns()
er = erk.annualize_rets(phrma["1996":"2000"], 12)
cov = phrma["1996":"2000"].cov()

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
                        'fun': lambda weights, er: target_return - erk.portfolio_return(weights, er)
    }
    weights = minimize(erk.portfolio_vol, init_guess,
                        args=(cov,), method='SLSQP',
                        options={'disp': False},
                        constraints=(weights_sum_to_1, return_is_target),
                        bounds=bounds)
    return weights.x

# testing
l = ["LLY", "DHR"]
# for a return of .30,
# the optimal volatility is approx .075

erk.plot_ef2(20, er[l], cov.loc[l,l])
plt.show()

# these weights are the golden egg.
weights_30 = erk.minimize_vol(0.30, er[l], cov.loc[l,l])
print(weights_30)

vol_30 = erk.portfolio_vol(weights_30, cov.loc[l,l])
print(vol_30)
# perfect

# calling plot function

l = ["MRK", "ABT", "LLY", "AMGN"]

erk.plot_ef(50, er[l], cov.loc[l, l])
plt.show()




































# plt.show() to display plots
