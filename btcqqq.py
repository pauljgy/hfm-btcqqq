from matplotlib import pyplot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from scipy import stats

btcData = pd.read_csv("BTC-USD.csv")
qqqData = pd.read_csv("^IXIC.csv")
validDates = list(qqqData['Date'])

invalidDates = list()

for one in range(0, len(btcData)):
    if (btcData.iat[one,  0] not in validDates):
        invalidDates.append(one)

btcData.drop(index=invalidDates, axis = 0, inplace = True)
btcData.reset_index(drop=True, inplace=True)

x = btcData['Close']
y = qqqData['Close']
corr = stats.pearsonr(x, y)
print(corr)

plt.scatter(x, y)
plt.show()