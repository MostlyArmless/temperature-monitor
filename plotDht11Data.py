from pandas import read_csv
from matplotlib import pyplot
import os
dirname = os.path.dirname(__file__)
logFile = os.path.join(dirname, 'dht11_log.csv')
print(logFile)
# logFile = 'dht11_log.txt'

series = read_csv(logFile, header=0, index_col=0,
                  parse_dates=True, squeeze=True)
print(series.head())

series.plot()
series.hist()
pyplot.show()
