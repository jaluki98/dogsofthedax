import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import json
import yahoo_fin.stock_info as si
import datetime

plt.style.use('dark_background')

with open('dogs.json') as f:
    dogsjson = json.load(f)

with open('smalldogs.json') as sf:
    smalldogsjson = json.load(sf)

dog0 = dogsjson["dogsofthedax"][0]["dog1_symbol"]
dog1 = dogsjson["dogsofthedax"][1]["dog2_symbol"]
dog2 = dogsjson["dogsofthedax"][2]["dog3_symbol"]
dog3 = dogsjson["dogsofthedax"][3]["dog4_symbol"]
dog4 = dogsjson["dogsofthedax"][4]["dog5_symbol"]
dog5 = dogsjson["dogsofthedax"][5]["dog6_symbol"]
dog6 = dogsjson["dogsofthedax"][6]["dog7_symbol"]
dog7 = dogsjson["dogsofthedax"][7]["dog8_symbol"]
dog8 = dogsjson["dogsofthedax"][8]["dog9_symbol"]
dog9 = dogsjson["dogsofthedax"][9]["dog10_symbol"]
dogsofthedax0 = "Tages-Ø"

dog0quote_table = si.get_quote_table(dog0)
dog0preis = dog0quote_table["Quote Price"]
dog0open = dog0quote_table["Open"]
dog0change = dog0preis - dog0open
dog0changepercent = dog0change / dog0preis
dog0chapercf = round(dog0changepercent *100, 2)

dog1quote_table = si.get_quote_table(dog1)
dog1preis = dog1quote_table["Quote Price"]
dog1open = dog1quote_table["Open"]
dog1change = dog1preis - dog1open
dog1changepercent = dog1change / dog1preis
dog1chapercf = round(dog1changepercent *100, 2)

dog2quote_table = si.get_quote_table(dog2)
dog2preis = dog2quote_table["Quote Price"]
dog2open = dog2quote_table["Open"]
dog2change = dog2preis - dog2open
dog2changepercent = dog2change / dog2preis
dog2chapercf = round(dog2changepercent *100, 2)

dog3quote_table = si.get_quote_table(dog3)
dog3preis = dog3quote_table["Quote Price"]
dog3open = dog3quote_table["Open"]
dog3change = dog3preis - dog3open
dog3changepercent = dog3change / dog3preis
dog3chapercf = round(dog3changepercent *100, 2)

dog4quote_table = si.get_quote_table(dog4)
dog4preis = dog4quote_table["Quote Price"]
dog4open = dog4quote_table["Open"]
dog4change = dog4preis - dog4open
dog4changepercent = dog4change / dog4preis
dog4chapercf = round(dog4changepercent *100, 2)

dog5quote_table = si.get_quote_table(dog5)
dog5preis = dog5quote_table["Quote Price"]
dog5open = dog5quote_table["Open"]
dog5change = dog5preis - dog5open
dog5changepercent = dog5change / dog5preis
dog5chapercf = round(dog5changepercent *100, 2)

dog6quote_table = si.get_quote_table(dog6)
dog6preis = dog6quote_table["Quote Price"]
dog6open = dog6quote_table["Open"]
dog6change = dog6preis - dog6open
dog6changepercent = dog6change / dog6preis
dog6chapercf = round(dog6changepercent *100, 2)

dog7quote_table = si.get_quote_table(dog7)
dog7preis = dog7quote_table["Quote Price"]
dog7open = dog7quote_table["Open"]
dog7change = dog7preis - dog7open
dog7changepercent = dog7change / dog7preis
dog7chapercf = round(dog7changepercent *100, 2)

dog8quote_table = si.get_quote_table(dog8)
dog8preis = dog8quote_table["Quote Price"]
dog8open = dog8quote_table["Open"]
dog8change = dog8preis - dog8open
dog8changepercent = dog8change / dog8preis
dog8chapercf = round(dog8changepercent *100, 2)

dog9quote_table = si.get_quote_table(dog9)
dog9preis = dog9quote_table["Quote Price"]
dog9open = dog9quote_table["Open"]
dog9change = dog9preis - dog9open
dog9changepercent = dog9change / dog9preis
dog9chapercf = round(dog9changepercent *100, 2)

dogsofthedaxchange = (dog0chapercf + dog1chapercf + dog2chapercf + dog3chapercf + dog4chapercf + dog5chapercf + dog6chapercf + dog7chapercf + dog8chapercf + dog9chapercf) / 10

objects = (dog0, dog1, dog2, dog3, dog4, dog5, dog6, dog7, dog8, dog9, dogsofthedax0)
y_pos = np.arange(len(objects))

performance = [dog0chapercf, dog1chapercf, dog2chapercf, dog3chapercf, dog4chapercf, dog5chapercf, dog6chapercf, dog7chapercf, dog8chapercf, dog9chapercf, dogsofthedaxchange]

now = datetime.datetime.now()
now_f = now.strftime("%Y-%m-%d")
copydate = now.strftime("%Y")
now_h = now.strftime("%d.%m.%Y")
now_m = now.strftime("%H:%M Uhr")

col = []
for val in performance:
    if val < 0.0:
        col.append('orangered')
    elif val >= 0.0:
        col.append('lightskyblue')
    else:
        col.append('white')

plt.bar(y_pos, performance, color = col, align='center')
plt.xticks(y_pos, objects)
plt.suptitle("Tages-Performance seit der Opening-Bell (" + now_h + ") bis " + now_m, y=0.905, x=0.1262, horizontalalignment='left', verticalalignment='top', fontsize = 11)
plt.figtext(0.007, 0.015, "(c) " + copydate + " dogsofthedax.com" + " - Für die Richtigkeit der Daten wird keine Haftung übernommen. Sollten Sie sich die Inhalte zu eigen machen oder etwaigen Ratschlägen folgen, so handeln Sie eigenverantwortlich auf eigenes Risiko.", horizontalalignment='left', fontsize=8.1, color='grey')
plt.margins(x=0)
plt.tick_params(left=False, labelleft=False) #remove ticks
plt.box(False)
plt.tick_params(axis='y', which='both', labelleft=False, labelright=True)
plt.gcf().set_size_inches(13, 6.5)
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.65, axis = 'y')

plt.ylabel('Veränderung in %')
plt.title('Dogs Of The DAX Day-Change Chart', fontweight='bold', y=1.05, x=0.00, fontsize = 17, horizontalalignment='left')

imgname = "Barchart_Einzelaktien_Dogs.jpg"

plt.savefig(imgname, format='jpg', dpi=100)
#plt.show()