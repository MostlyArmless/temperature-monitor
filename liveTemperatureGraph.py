import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
from pandas import read_csv
from datetime import date

fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)
logFile = 'E:\\Users\\mikej\\Desktop\\temperature_logs\\{}.csv'.format(
    date.today())


def animate(i):
    dfGarage = read_csv(logFile, header=0, index_col=0,
                        parse_dates=True, squeeze=True)

    # tCalgary = dfCalgary['temperature']
    tGarage = dfGarage['Temperature (C)']
    # hCalgary = dfCalgary['relative_humidity']
    hGarage = dfGarage['Humidity (%)']

    ax1.clear()
    # ax1 = plt.subplot(211)
    # ax1.plot(tCalgary)
    ax1.plot(tGarage)

    ax2.clear()
    # ax2 = plt.subplot(212)
    # ax2.plot(hCalgary, sharex=ax1)
    ax2.plot(hGarage)


ani = animation.FuncAnimation(fig, animate, interval=4000)
plt.show()
