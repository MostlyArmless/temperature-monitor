from pandas import read_csv
import matplotlib.pyplot as plt
import os

dirname = os.path.dirname(__file__)

logFile = os.path.join(dirname, 'weatherstats_calgary_hourly.csv')
dfCalgary = read_csv(logFile, header=0, index_col=0,
                     parse_dates=True, squeeze=True)

logFile = os.path.join(dirname, 'dht11_log.csv')
dfGarage = read_csv(logFile, header=0, index_col=0,
                    parse_dates=True, squeeze=True)

tCalgary = dfCalgary['temperature']
tGarage = dfGarage['Temperature (C)']

hCalgary = dfCalgary['relative_humidity']
hGarage = dfGarage['Humidity (%)']

ax1 = plt.subplot(211)
ax1.plot(tCalgary)
ax1.plot(tGarage)

ax2 = plt.subplot(212)
ax2.plot(hCalgary, sharex=ax1)
ax2.plot(hGarage, sharex=ax1)

plt.show()
print("Done")
