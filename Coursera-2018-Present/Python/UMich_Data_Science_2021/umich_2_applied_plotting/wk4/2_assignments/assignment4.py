#######################################
# Assignment 4: Visualization Project #
#######################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import re

#plt.style.use('seaborn-colorblind')

# reading in data
df1 = pd.read_csv('Largest_MktCap.csv')
print(df1.head())
df2 = pd.read_csv('GDP_2019.csv')
print(df2.head())

# adding column to df1
df1['Country'] = df1.Company.str.extract('(\(.*\))')
df1['Country'] = df1['Country'].str.replace('\(|\)', '')
df1['Country'] = df1['Country'].str.lstrip()
df1['Country'] = df1['Country'].str.rstrip()
df1['Company'] = df1['Company'].str.replace('(\(.*\))', '')
print(df1.head())
df1.to_csv(r'C:\Dhruv\Data\1_umich_ds_2_applied_plotting\wk4\2_assignments\df.csv', index=False, header=True)

df2['Country'] = df2['Country'].str.replace('(\[.*\])', '')
df2['Country'] = df2['Country'].str.lstrip()
df2['Country'] = df2['Country'].str.rstrip()
df2 = df2.set_index('Country')
print(df2.head())

df3 = df1
df3 = df3.groupby("Country").agg({"Market Cap (US$Billion)":(np.nansum)})
print(df3)


df4 = pd.merge(df2, df3, how='inner', left_index=True, right_index=True)
df4 = df4.reset_index()
print(df4)


# creating plot
plt.figure()
plt.bar(df4['Country'], df4['GDP (US$Billion)'], alpha=0.85, label='GDP');
plt.bar(df4['Country'], df4['Market Cap (US$Billion)'], alpha=0.85, label='Market Cap');
plt.legend();
plt.title('Largest Market Caps proportional to HQ country\'s GDP');
plt.xlabel('Country')
plt.ylabel('USD (billions)')
plt.xticks(rotation=30, fontsize=9);

plt.show()































# plt.show() to display plots
