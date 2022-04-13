###########################
# assignment 2: NOAA Data #
###########################
import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd

# mplleaflet plot

'''
def leaflet_plot_stations(binsize, hashid):

    df = pd.read_csv('data/C2A2_data/BinSize_d{}.csv'.format(binsize))

    station_locations_by_hash = df[df['hash'] == hashid]

    lons = station_locations_by_hash['LONGITUDE'].tolist()
    lats = station_locations_by_hash['LATITUDE'].tolist()

    plt.figure(figsize=(8,8))

    plt.scatter(lons, lats, c='r', alpha=0.7, s=200)

    return mplleaflet.show()

leaflet_plot_stations(400, 'fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89')
'''

# part 1
# original data
df0 = pd.read_csv('data\C2A2_data\BinnedCsvs_d400\\fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')
df0 = df0.sort_values(by=['Date'])
df0['Date'] = pd.to_datetime(df0['Date'])

# cleaning dataset copy
df = df0
df['Year'] = df['Date'].dt.year
df = df[df['Year'] < 2015]

print(df.head())
print(df.tail())


print(df.shape)
print(df.dtypes)

'''
# scratch syntax
df1 = df[df['Element'] == 'TMAX']
print(df1.head())
print(df1.shape)

df2 = df[df['Element'] == 'TMIN']
print(df2.head())
print(df2.shape)


plt.figure()
plt.plot(df1['Date'], df1['Data_Value'], df2['Date'], df2['Data_Value'], lw=0.25)
plt.show()
'''


import numpy as np

# grouping by date
df3 = df
df3['Date'] = df3['Date'].dt.strftime('%m-%d')
print(df3.head())

df3 = df3.groupby("Date").agg({"Data_Value": (np.nanmin, np.nanmax)})

df3 = df3.rename(columns={'nanmin': '2005-2014_min',
                          'nanmax': '2005-2014_max'})


# dropping nested header, top row
df3.columns = df3.columns.droplevel(0)

df3 = df3.reset_index()

# import datetime

df3 = df3.reset_index()

df3 = df3.set_index('Date')

print(df3.head())
print(df3.tail())

# part 1 answer
position = np.arange(1, 365, 31)
labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
plt.xticks(position, labels)

plt.plot(df3['index'], df3['2005-2014_min'], df3['index'], df3['2005-2014_max'])
plt.xlabel('Date')
plt.ylabel('Temperature')

plt.gca().fill_between(range(len(df3['2005-2014_min'])),
                        df3['2005-2014_min'], df3['2005-2014_max'],
                        facecolor='blue',
                        alpha=0.25)

# part 2
df4 = df0
df4['Year'] = df4['Date'].dt.year
df4 = df4[df4['Year'] == 2015]

df4['Date'] = df4['Date'].dt.strftime('%m-%d')
df4 = df4.groupby("Date").agg({"Data_Value": (np.nanmin, np.nanmax)})

# dropping nested header, top row
df4.columns = df4.columns.droplevel(0)


df4 = df4.rename(columns={'nanmin': '2015_min',
                          'nanmax': '2015_max'})

print(df4.head())
print(df4.tail())

df5 = pd.merge(df3, df4, how='inner', left_index=True, right_index=True)

df5['new_record_high'] = np.where(df5['2015_max'] > df5['2005-2014_max'], 1, 0)
df5['new_record_low'] = np.where(df5['2015_min'] < df5['2005-2014_min'], 1, 0)

print(df5.head())
print(df5.tail())

df6 = df5[df5['new_record_high'] == 1]
df7 = df5[df5['new_record_low'] == 1]

print(df6.head())
print(df6.tail())

print(df7.head())
print(df7.tail())

plt.plot(df6['index'], df6['new_record_high'], '.')
plt.plot(df7['index'], df7['new_record_low'], '.')

plt.legend(['Record Lows', 'Record Highs', 'New Record Highs', 'New Record Lows'])

plt.show()















# use plt.show() to display plots
