import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas_datareader as web
import datetime
import json
import sys
import re

now = datetime.datetime.now()
now_f = now.strftime("%Y-%m-%d")
copydate = now.strftime("%Y")

plt.style.use('dark_background')

#JSON
with open('dogs.json') as f:
    dogsjson = json.load(f)

with open('smalldogs.json') as sf:
    smalldogsjson = json.load(sf)

#Portfolio Inhalt mit Yahoo-Tickers und Gewichtung
tickers = [dogsjson["dogsofthedax"][0]["dog1_symbol"], dogsjson["dogsofthedax"][1]["dog2_symbol"], dogsjson["dogsofthedax"][2]["dog3_symbol"], dogsjson["dogsofthedax"][3]["dog4_symbol"], dogsjson["dogsofthedax"][4]["dog5_symbol"], dogsjson["dogsofthedax"][5]["dog6_symbol"], dogsjson["dogsofthedax"][6]["dog7_symbol"], dogsjson["dogsofthedax"][7]["dog8_symbol"], dogsjson["dogsofthedax"][8]["dog9_symbol"], dogsjson["dogsofthedax"][9]["dog10_symbol"]]
wts = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]

#Download der Yahoo-Finance Daten und anschließendes "behalten" von Adj. Close
price_data = web.get_data_yahoo(tickers,
                                start = '2021-01-03',
                                end = now_f)
price_data = price_data['Adj Close']

#Gewinn- Verlust-Rechnung (täglicher Basis)
ret_data = price_data.pct_change()[1:]

#Portfolio Performance
port_ret = (ret_data * wts).sum(axis = 1)

#Gesamte Gewinne und Verluste
cumulative_ret = (port_ret + 1).cumprod() * 100 - 100
fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])

#Dogs Of The DAX Chart
ax1.plot(cumulative_ret, label="Dogs Of The DAX (ausschüttend)", color="gold", linewidth=1.2)


cumulative_ret.to_csv('kumuliert_dogsofthedax_performance.csv', sep='\t', index=True)

######## SMALL DOGS CHART #########

tickers_sdotd = [smalldogsjson["dogsofthedax"][0]["dog1_symbol"], smalldogsjson["dogsofthedax"][1]["dog2_symbol"], smalldogsjson["dogsofthedax"][2]["dog3_symbol"], smalldogsjson["dogsofthedax"][3]["dog4_symbol"], smalldogsjson["dogsofthedax"][4]["dog5_symbol"]]
wts_sdotd = [0.1,0.1,0.1,0.1,0.1]

price_data_sdotd = web.get_data_yahoo(tickers_sdotd,
                                start = '2021-01-03',
                                end = now_f)
price_data_sdotd = price_data_sdotd['Adj Close']

ret_data_sdotd = price_data_sdotd.pct_change()[1:]

port_ret_sdotd = (ret_data_sdotd * wts_sdotd).sum(axis = 1)

cumulative_ret_sdotd = (port_ret_sdotd + 1).cumprod() * 100 - 100
#fig_sdotd = plt.figure()
#sdotd = fig_sdotd.add_axes([0.1,0.1,0.8,0.8])

cumulative_ret_sdotd.plot(label="Small Dogs Of The DAX (ausschüttend)", color="hotpink", linewidth=1.2)

cumulative_ret_sdotd.to_csv('kumuliert_smalldogsofthedax_performance.csv', sep='\t', index=True)

####### ENDE SMALL DOGS CHART / GRAPH ##################


###### DAX GRAPH ##############
dax = web.get_data_yahoo("^GDAXI",
start = "2021-01-03",
end = now_f)

dax_adj = dax['Adj Close']

ret_dax = dax_adj.pct_change()[1:] * 100

ret_dax.plot(label="DAX (thesaurierend)", color="gainsboro", linewidth=1, linestyle='-')
####### DAX GRAPH ENDE #############

ax1.set_xlabel('')
ax1.yaxis.set_major_formatter(mtick.PercentFormatter())

#Subtitle Quelle: dogsofthedax.com und Yahoo-Finance

now_h = now.strftime("%d.%m.%Y")
plt.suptitle("Dogs Of The DAX Performance Chart", fontweight='bold', x=0.1, fontsize = 17, horizontalalignment='left')
ax1.set_title("Abbildungszeitraum: 03.01.2021 - " + now_h, x=0.001, horizontalalignment='left', verticalalignment='top', fontsize = 11)
plt.figtext(0.007, 0.015, "(c) " + copydate + " dogsofthedax.com" + " - Information: Der Chart basiert auf angepassten Schlusskursen der jeweils in dem oben angegebenen Zeitraum liegenden Handelstagen. Samstage sowie Sonntage sind von der Grafik ausgenommen.", horizontalalignment='left', fontsize=8.1, color='grey')
plt.figtext(0.938, 0.92, "Rendite", horizontalalignment='right')
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.55, axis = 'both')

plt.margins(x=0)
ax1.spines['top'].set_visible(False)
ax1.spines['left'].set_visible(False)

ax1.yaxis.set_label_position("right")
ax1.yaxis.tick_right()

nows = now.strftime("%Y%m%d")
imgname = 'dogs_of_the_dax_chart' + 'twitterupdate' + '.jpg'

plt.xticks(rotation = 0)
plt.legend(fancybox = "False",loc="upper left", facecolor="black", edgecolor="black" )

plt.draw()
fig.set_size_inches(13.0,6.5)
plt.savefig(imgname, format='jpg', dpi=100)
#plt.show();
