##################################################
# Assignment 1: Fundamentals of Machine Learning #
##################################################
import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer

# storing bunch object in scikit learn, similar to a dictionary
cancer = load_breast_cancer()
print(cancer.DESCR)

# printing bunch keys
print(cancer.keys())

##############
# Question 0 #
##############
# function returning dimension size for columns
def answer_zero():
    return len(cancer['feature_names'])

print(answer_zero()) # 30 features

##############
# Question 1 #
##############
# converting bunch to a dataframe
def answer_one():
    # have to concatenate target column, and append target label
    df = pd.DataFrame(np.c_[cancer.data, cancer.target], columns=np.append(cancer.feature_names, ["target"]))
    return df

print(answer_one())
# print(answer_one().shape) # (569,31)

##############
# Question 2 #
##############
# printing series with class distribution
def answer_two():
    cancerdf = answer_one()
    # saving frequency table to a series named target
    target = cancerdf['target'].value_counts()
    # used to strictly relabel axes, does not interfere with data
    target = target.rename({1.0: "benign", 0.0: "malignant"})
    return target

print(answer_two())

##############
# Question 3 #
##############
# creating dataframes for data and labels
def answer_three():
    cancerdf = answer_one()
    # subsetting to predictor columns
    X = cancerdf.drop(['target'], axis=1)
    # creating predicted column
    y = cancerdf[['target']]
    return X, y

print(answer_three())
# print(answer_three()[0].shape, answer_three()[1].shape) # (569, 30), (569, 1)

##############
# Question 4 #
##############
from sklearn.model_selection import train_test_split

# creating train test split for training model
def answer_four():
    X, y = answer_three()
    # train test split, default is 75%/25%
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    return X_train, X_test, y_train, y_test

print(answer_four())
# print(answer_four()[0].shape, answer_four()[1].shape, answer_four()[2].shape, answer_four()[3].shape)
# (426, 30), (143, 30), (426, 1), (143, 1)

##############
# Question 5 #
##############
from sklearn.neighbors import KNeighborsClassifier

# creating classifier object, number of neighbors = 1
def answer_five():
    X_train, X_test, y_train, y_test = answer_four()
    knn = KNeighborsClassifier(n_neighbors = 1)

    return knn.fit(X_train, y_train.values.ravel())

print(answer_five())


##############
# Question 6 #
##############
# class prediction using means of each data column
def answer_six():
    cancerdf = answer_one()
    # getting column means
    means = cancerdf.mean()[:-1].values.reshape(1,-1)

    # calling classifier
    X_train, X_test, y_train, y_test = answer_four()
    knn = answer_five()

    return knn.predict(means)

print(answer_six())
# print(type(answer_six())) # numpy array1

##############
# Question 7 #
##############
# class prediction using test data
def answer_seven():
    # calling classifier
    X_train, X_test, y_train, y_test = answer_four()
    knn = answer_five()

    return knn.predict(X_test)

print(answer_seven())
# print(type(answer_seven())) # numpy array
# print(answer_seven().shape) # (143,)

##############
# Question 8 #
##############
# scoring our model
def answer_eight():
    # calling classifier
    X_train, X_test, y_train, y_test = answer_four()
    knn = answer_five()

    return knn.score(X_test, y_test)

print(answer_eight())








































# plt.show() to display plots
