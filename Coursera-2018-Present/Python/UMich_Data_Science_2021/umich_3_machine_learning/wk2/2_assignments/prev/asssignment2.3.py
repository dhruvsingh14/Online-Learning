#############################################
# Assignment 2: Part 1, Regression Analysis #
#############################################

# importing libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# creating simulated data
np.random.seed(0)
n = 15
x = np.linspace(0,10,n) + np.random.randn(n)/5
y = np.sin(x)+x/6 + np.random.randn(n)/10

# test train split
X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=0)

#################################################
# Question 2: Polynomial Regression Models: R^2 #
#################################################
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

d1 = {}
d2 = {}

# reshaping x train to transform into x train poly
X_train = X_train.reshape(-1, 1)
# reshaping x test to transform into x test poly
X_test = X_test.reshape(-1, 1)

for k in range(0,10,1):
    # transforming x train to obtain x train poly
    poly = PolynomialFeatures(degree=k)
    x_train_poly = poly.fit_transform(X_train)

    # transforming x test to obtain x test poly
    x_test_poly = poly.fit_transform(X_test)

    # fitting model to training data
    model = LinearRegression()
    model.fit(x_train_poly, y_train)

    # predicting y values using training data
    y_train_poly_pred = model.predict(x_train_poly)
    # scoring model for training data
    r2_score(y_train, y_train_poly_pred)
    # scoring model for training data, using r2 scores # and storing in containers
    d1["r2_train_deg_{}".format(k)] = r2_score(y_train, y_train_poly_pred)

    # predicting y values using test data
    y_test_poly_pred = model.predict(x_test_poly)
    # scoring model for test data
    r2_score(y_test, y_test_poly_pred)
    # scoring model for test data, using r2 scores # and storing in containers
    d2["r2_test_deg_{}".format(k)] = r2_score(y_test, y_test_poly_pred)

# converting training score dictionary to an array
data1 = list(d1.items())
train_score_array = np.array(data1)
# storing train score column
r2_train = train_score_array[0:10,1]

# converting test score dictionary to an array
data2 = list(d2.items())
test_score_array = np.array(data2)
# storing test score column
r2_test = test_score_array[0:10,1]

# combining scores in tuple
r2_score_tuple = (r2_train, r2_test)
print(r2_score_tuple)

############################
## Q3: plotting r2 scores ##
############################

x = np.linspace(0, 9, 10)
print(x)

y = np.linspace(-1, 1, 21)
print(y)

# plotting r scores for each degree
# comparing model performance on training and test data


df = pd.DataFrame(np.column_stack(r2_score_tuple), columns =['r2_train', 'r2_test'])
print(df.dtypes)

df = df.apply(pd.to_numeric)
print(df)
print(df.dtypes)

#df2 = df.round(decimals=2)



plt.plot(df['r2_train'], '-o')
plt.plot(df['r2_test'], '-o')
plt.legend(['train', 'test'])
plt.show()


# degree 4 through 7 seems to be the sweet spot, esp 6-7
# 8-9, where train performs well, but test drops off is an example of overfitting
# and 0 - 3 is an example of underfitting, with degree 1 exhibiting the largest gap

















# plt.show() to display plots
