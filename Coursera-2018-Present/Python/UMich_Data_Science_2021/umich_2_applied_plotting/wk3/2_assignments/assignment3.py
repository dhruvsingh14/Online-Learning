######################################
# Assignment 3: Visualization Design #
######################################
# creating simulated data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(12345)
# arguments: mean, std dev, # samples
df = pd.DataFrame([np.random.normal(32000,200000,3650),
                   np.random.normal(43000,100000,3650),
                   np.random.normal(43500,140000,3650),
                   np.random.normal(48000,70000,3650)],
                  index=[1992,1993,1994,1995])
np.random.seed(12345)

print(df)

##################
# Easiest option #
##################
# since the only columns are the samples, we can take the mean of all

df['mean'] = df.iloc[:, 0:3649].mean(axis=1)
df['stdev'] = df.iloc[:,0:3649].std(axis=1)

error92 = 1.96*(df.iloc[0, 3651]/np.sqrt(3650))
error93 = 1.96*(df.iloc[1, 3651]/np.sqrt(3650))
error94 = 1.96*(df.iloc[2, 3651]/np.sqrt(3650))
error95 = 1.96*(df.iloc[3, 3651]/np.sqrt(3650))

error = [error92, error93, error94, error95]

ci92_u = df.iloc[0, 3650] + 1.96*df.iloc[0, 3651]
ci92_l = df.iloc[0, 3650] - 1.96*df.iloc[0, 3651]
print(ci92_u, ci92_l)

ci93_u = df.iloc[1, 3650] + 1.96*df.iloc[1, 3651]
ci93_l = df.iloc[1, 3650] - 1.96*df.iloc[1, 3651]
print(ci93_u, ci93_l)

df = df.reset_index()
print(df)

bars = ('1992', '1993', '1994', '1995')


#plt.figure(figsize=(10,20))
plt.bar(df['index'], df['mean'], # width=1,
            color = ['darkblue', 'coral', 'lightblue', 'maroon'],
            #edgecolor='black')
            yerr = error, edgecolor='black') # std
plt.xticks(df['index'], bars)


#set_xticks =

plt.show()



































# plt.show() to display graphics in matplotlib
