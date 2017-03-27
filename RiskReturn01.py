# import library
import numpy as np
import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#load data
symbols = ['BANPU.BK', 'SCCC.BK', 'TOP.BK', 'AKR.BK', 'PTT.BK']
stocks = pd.DataFrame()
for x in symbols:
    stocks[x] = web.DataReader(x, data_source='yahoo')['Adj Close']

#plot raw data
stocks[['BANPU.BK', 'SCCC.BK', 'TOP.BK', 'AKR.BK', 'PTT.BK']].plot(figsize=(15, 10))
#normalize data
normStocks = (stocks / stocks.ix[0] * 100)
#plot again
normStocks[['BANPU.BK', 'SCCC.BK', 'TOP.BK', 'AKR.BK', 'PTT.BK']].plot(figsize=(15, 10))

#calculate log return
log_return = np.log(normStocks / normStocks.shift(1))
rets = log_return.dropna()

#plot banpu
stocks['BANPU.BK'].plot()
#histogram plot
sns.distplot(rets['BANPU.BK'], bins=50, color='blue')

#banpu downside 95%
sns.distplot(rets['BANPU.BK'], bins=50, color='blue')
p=np.percentile(rets['BANPU.BK'],5)
plt.title("BANPU Return")
plt.axvline(x=p, linewidth=3, color='r')
plt.figtext(0.45, 0.6, "percentile (0.95): %.4f" % p + "%",fontsize=20)

#banpu downside 90%
sns.distplot(rets['BANPU.BK'], bins=50, color='blue')
p=np.percentile(rets['BANPU.BK'],10)
plt.title("BANPU Return")
plt.axvline(x=p, linewidth=3, color='r')
percent = p*100
plt.figtext(0.45, 0.6, "percentile (0.90): %.4f" % percent  + "%",fontsize=20)


#banpu upside
sns.distplot(rets['BANPU.BK'], bins=50, color='blue')
p=np.percentile(rets['BANPU.BK'],95)
plt.title("BANPU Return")
plt.axvline(x=p, linewidth=3, color='r')
percent = p*100
plt.figtext(0.45, 0.6, "percentile (0.95): %.4f" % percent  + "%",fontsize=20)


#plot SCCC stock
sns.distplot(rets['SCCC.BK'], bins=50, color='blue')
p=np.percentile(rets['SCCC.BK'],5)
plt.title("SCCC Return")
plt.axvline(x=p, linewidth=3, color='r')
percent = p*100
plt.figtext(0.45, 0.6, "percentile (0.05): %.4f" % percent  + "%",fontsize=20)

#plot TOP stock
sns.distplot(rets['TOP.BK'], bins=50, color='blue')
p=np.percentile(rets['TOP.BK'],5)
plt.title("TOP Return")
plt.axvline(x=p, linewidth=3, color='r')
percent = p*100
plt.figtext(0.45, 0.6, "percentile (0.05): %.4f" % percent  + "%",fontsize=20)

#plot AKR stock
sns.distplot(rets['AKR.BK'], bins=50, color='blue')
p=np.percentile(rets['AKR.BK'],5)
plt.title("AKR Return")
plt.axvline(x=p, linewidth=3, color='r')
percent = p*100
plt.figtext(0.45, 0.6, "percentile (0.05): %.4f" % percent  + "%",fontsize=20)

#plot PTT stock
sns.distplot(rets['PTT.BK'], bins=50, color='blue')
p=np.percentile(rets['PTT.BK'],5)
plt.title("PTT Return")
plt.axvline(x=p, linewidth=3, color='r')
percent = p*100
plt.figtext(0.45, 0.6, "percentile (0.05): %.4f" % percent  + "%",fontsize=20)

