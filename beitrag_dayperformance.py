from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc import WordPressPost
import datetime
from yahoo_fin import stock_info as si
from yahoo_finance import Share
import json

#json

with open('dogs.json') as f:
    dogsjson = json.load(f)


#-------------------------------------------
###

#+++++++++ USE JSON IN 2022 ++++++++++++++

####
#Stocks
bmwshare = Share('BMW.DE')
bmwpreis = bmwshare.get_price()
bmwebitda = bmwshare.get_ebitda()
bmwdayhigh = bmwshare.get_days_high()
bmwdaylow = bmwshare.get_days_low()
bmwopen = bmwshare.get_open()
bmw50daymovavg = bmwshare.get_50day_moving_avg()
bmw200daymovavg = bmwshare.get_200day_moving_avg()

basshare = Share('BAS.DE')
baspreis = basshare.get_price()
basebitda = basshare.get_ebitda()
basdayhigh = basshare.get_days_high()
basdaylow = basshare.get_days_low()
basopen = basshare.get_open()
bas50daymovavg = basshare.get_50day_moving_avg()
bas200daymovavg = basshare.get_200day_moving_avg()
basveraenderung = baspreis - basopen

baynshare = Share('BAYN.DE')
baynpreis = baynshare.get_price()
baynebitda = baynshare.get_ebitda()
bayndayhigh = baynshare.get_days_high()
bayndaylow = baynshare.get_days_low()
baynopen = baynshare.get_open()
bayn50daymovavg = baynshare.get_50day_moving_avg()
bayn200daymovavg = baynshare.get_200day_moving_avg()

eoanshare = Share('EOAN.DE')
eoanpreis = eoanshare.get_price()
eoanebitda = eoanshare.get_ebitda()
eoandayhigh = eoanshare.get_days_high()
eoandaylow = eoanshare.get_days_low()
eoanopen = eoanshare.get_open()
eoan50daymovavg = eoanshare.get_50day_moving_avg()
eoan200daymovavg = eoanshare.get_200day_moving_avg()

alvshare = Share('ALV.DE')
alvpreis = alvshare.get_price()
alvebitda = alvshare.get_ebitda()
alvdayhigh = alvshare.get_days_high()
alvdaylow = alvshare.get_days_low()
alvopen = alvshare.get_open()
alv50daymovavg = alvshare.get_50day_moving_avg()
alv200daymovavg = alvshare.get_200day_moving_avg()

muv2share = Share('MUV2.DE')
muv2preis = muv2share.get_price()
muv2ebitda = muv2share.get_ebitda()
muv2dayhigh = muv2share.get_days_high()
muv2daylow = muv2share.get_days_low()
muv2open = muv2share.get_open()
muv250daymovavg = muv2share.get_50day_moving_avg()
muv2200daymovavg = muv2share.get_200day_moving_avg()

dteshare = Share('DTE.DE')
dtepreis = dteshare.get_price()
dteebitda = dteshare.get_ebitda()
dtedayhigh = dteshare.get_days_high()
dtedaylow = dteshare.get_days_low()
dteopen = dteshare.get_open()
dte50daymovavg = dteshare.get_50day_moving_avg()
dte200daymovavg = dteshare.get_200day_moving_avg()

sieshare = Share('SIE.DE')
siepreis = sieshare.get_price()
sieebitda = sieshare.get_ebitda()
siedayhigh = sieshare.get_days_high()
siedaylow = sieshare.get_days_low()
sieopen = sieshare.get_open()
sie50daymovavg = sieshare.get_50day_moving_avg()
sie200daymovavg = sieshare.get_200day_moving_avg()
siedif = siepreis - sieopen

vow3share = Share('VOW3.DE')
vow3preis = vow3share.get_price()
vow3ebitda = vow3share.get_ebitda()
vow3dayhigh = vow3share.get_days_high()
vow3daylow = vow3share.get_days_low()
vow3open = vow3share.get_open()
vow350daymovavg = vow3share.get_50day_moving_avg()
vow3200daymovavg = vow3share.get_200day_moving_avg()

dpwshare = Share('DPW.DE')
dpwpreis = dpwshare.get_price()
dpwebitda = dpwshare.get_ebitda()
dpwdayhigh = dpwshare.get_days_high()
dpwdaylow = dpwshare.get_days_low()
dpwopen = dpwshare.get_open()
dpw50daymovavg = dpwshare.get_50day_moving_avg()
dpw200daymovavg = dpwshare.get_200day_moving_avg()

daxshare = Share('^GDAXI')
daxpreis = daxshare.get_price()
daxdayhigh = daxshare.get_days_high()
daxdaylow = daxshare.get_days_low()
daxopen = daxshare.get_open()
daxveraenderung = daxpeis - daxopen
daxschwankung = daxdayhigh - daxdaylow

if daxveraenderung >= 0:
	daxfarbe = 'grünen'
	stimmung = 'positive'

else:
	daxfarbe = 'roten'
	stimmung = 'negative'

#-------------------------------------------
#Zeit

today_date = datetime.date.today()
now = today_date.strftime("%d/%m/%Y")
nowslug = today_date.strftime("%d_%m_%y")
uhrzeit = datetime.now()
uhrzeitjz = uhrzeit.strftime("%H:%M:%S")

#Wochentag

wochentag = date.weekday()

if wochentag == 0:
	weekday = 'Montag'

elif wochentag == 1:
	weekday = 'Dienstag'

elif wochentag == 2:
	weekday = 'Mittwoch'

elif wochentag == 3:
	weekday = 'Donnerstag'

elif wochentag == 4:
	weekday = 'Freitag'

#-------------------------------------------
#Wordpress

your_blog = Client('http:dogsofthedax.com', 'janlukaskiermeyer', 'Ginf3j98-grh834-3fh934n')

myposts=your_blog.call(posts.GetPosts())

post = WordPressPost()
post.title = '{now}: Dogs of The Dax Performance Update'
post.slug='{nowslug}_dogs_of_the_dax_performance_update'
post.content = 'Nach Börsenschluss ergeben sich rückblickend auf den Handelstag folgende Stellungnahmen:\nDer DAX beendet den heutigen Handelstag mit {daxfarbe} Zahlen, und einem Endstand von {daxpreis} Punkten. Am Morgen stand er bei {daxopen} Zählern. Über den Tagesverlauf gab es eine Veränderung von {daxveraenderung} Punkten. Der Höchststand betrug {daxdayhigh}, im Vergleich zu einem Tiefpunkt von {daxdaylow}, was einer Differenz von {daxschwankung} entspricht.\nIm Verlauf des heutigen {weekday}s ({now}) haben die zehn Dogs Of The Dax die {stimmung} des deutschen Leitindexes wie folgt genutzt:\nAngefangen bei dem Pharmagiganten Bayer AG (XFRA:BAYN) beträgt der Kurs nun {baynpreis} EUR. In den Tag startete die Aktie mit {baynopen} EUR. Das Tageshoch betrug {bayndayhigh} EUR gegenüber einem Tief von {bayndaylow} EUR. Zum jetzigen Zeitpunkt beträgt der 50-Tage-Durchschnitt beträgt {bayn50daymovavg} EUR zusammen mit einem 200-Tage-Durchschnitt von {bayn200daymovavg} EUR. Das EBITDA von Bayer beträgt {baynebitda}. Das Unternehmen zählt zu den Dogs Of The Dax und Small Dogs Of The Dax.\nDas Wertpapier des Chemie-Unternehmen BASF (XFRA:BAS) ist nach Börsenschluss mit {baspreis} EUR notiert. Am Morgen stand das Papier bei {basopen} EUR, und hat sich somit um {basveraenderung} EUR über den Tag verändert. Über den Tagesverlauf schwankte die Aktie zwischen {basdayhigh} EUR (High) und {basdaylow} EUR (Low). Im 50-Tage-Durchschnitt war das Papier mit {bas50daymovavg} EUR notiert. Der 200-Tage-Durschnitt liegt bei {bas200daymovavg}. Aus den aktuellen Fundamentaldaten ergibt sich ein EBITDA von {basebitda}. BASF SE (XFRA:BAS) zählt 2021 zu den Dogs Of The Dax und Small Dogs Of The Dax.\nE.ON hat den Tag mit einem Aktienpreis von {eoanpreis} EUR beendet. Dem zugrunde liegt ein Tageshoch am heutigen Handelstag von {eoandayhigh} EUR, mit einem Tief von {eoandaylow} EUR. In den Handel gestartet ist das Wertpapier mit einem Wert von {eoanopen} EUR. Aus den Kennzahlen errechnet sich momentan ein EBITDA von {eoanebitda}. Der Durchschnittswert des Papieres liegt im 50-Tage-Trend bei {eoan50daymovavg} EUR, im 200-Tage-Trend bei {eoan200daymovavg}. E.ON SE (XFRA:EOAN) befindet sich in den Small Dogs Of The Dax, wie auch in den diesjährigen regulären Dogs Of The Dax.\nDie Allianz, mit dem Symbol ALV (XFRA) steht momentan bei {alvpreis} EUR. Zu Beginn des Handels notierte die Aktie {alvopen} EUR. Unter Berücksichtigung von den Unternehmenskennzahlen liegt das EBITDA bei {alvebitda}. Das Tageshoch verzeichnete die Aktie bei {alvdayhigh} EUR, wobei sie zwischendurch auf {alvdaylow} EUR sank. Die Tagesdurchschnitte liegen bei {alv50daymovavg} EUR in den vergangenen 50 Tagen, und {alv200daymovavg} EUR über 200 Tage. Das Versicherungsunternehmen zählt zu den regulären Dogs Of The Dax und nicht zu den Small Dogs Of The Dax.\nDie Muenchener Rückvers. AG (XFRA:MUV2) notierte nach der Opening-Bell {muv2preis} EUR. Über den Tag schwankte die Aktie zwischen {muv2daylow} EUR, und {muv2dayhigh} EUR. Die 50- und 200-Tage-Historie zeigen einen Kurswert von {muv250daymovavg} EUR, und {muv2200daymovavg} EUR. Das EBITDA liegt bei {muv2ebitda}. Nach Börsenschluss notierte das Unternehmen {muv2preis} EUR. Die Aktie mit dem Ticker-Symbol XFRA:MUV2 zählt zu den Dogs Of The Dax.\nDas Telekommunikationsunternehmen Deutsche Telekom AG, steht nachbörslich bei einem Wert von {dtepreis} EUR. Heute Morgen, bei Handelsbeginn lag das Papier bei {dteopen} EUR. Im Tagesverlauf gab es einen Höchststand von {dtedayhigh} EUR. Zum günstigsten Zeitpunkt stand die Aktie heute bei {dtedaylow} EUR. Das EBITDA beträgt {dteebitda}. Die Kurshistorie verzeichnet einen 50-Tage-Durschnitt von {dte50daymovavg} EUR, und einen 200-Tage-Durchschnitt von {dte200daymovavg} EUR. Das Unternehmen mit Hauptfirmensitz in Bonn, Nordrhein-Westfalen fällt unter die Kategorien Dogs Of The Dax, und Small Dogs Of The Dax.\nDer Automobilhersteller BMW notiert {bmwpreis} EUR zum momentanen Zeitpunkt der Veröffentlichung dieses Artikels. Mit der exakten Bezeichnung Bayerische Motoren Werke AG (XFRA:BMW) schwankte das Wertpapier am heutigen {weekday} zwischen einem {bmwdaylow} EUR Tiefstand, und {bmwdayhigh} EUR (High). Unter Berücksichtigung der Kennzahlen liegt das EBITDA von BMW bei {bmwebitda}. In den Handel startete die Aktie heute mit {bmwopen} EUR. Der 50-Tage-Durschnitt beträgt {bmw50daymovavg} EUR. Der 200-Tage.Durschnitt liegt bei {bmw50daymovavg} EUR. Das Werpapier zählt zu den Dogs Of The Dax, sowie den Small Dogs Of The Dax als teuerstes Wertpapier in dieser Kategorie.\nSiemens AG (XFRA:SIE) lag bei einem Preis von {sieopen} EUR bei Handelsbeginn. Über den Tag ergab sich ein Höchstwert von {siedayhigh} EUR. Das Low betrug {siedaylow} EUR. Zurückblickend gibt es einen 50-Tage-Durchschnitt von {sie50daymovavg} EUR. Der 200-Day-Moving-Average steht bei {sie200daymovavg} EUR. Das EBITDA liegt nach aktuellen Kennzahlen bei {sieebitda}. Nach dem Handelstag (stand jetzt) liegt das Papier bei {siepreis} EUR, was einer Differnz von {siedif} EUR entspricht.\nVolkswagen notiert zum aktuellen Zeitpunkt {vow3preis} EUR. Mit {vow3open} EUR startete die Aktie des Automobilherstellers heute Morgen in den Handel. Die Tagesschwankungen betrugen: {vow3dayhigh} EUR beim Höchststand, und {vow3daylow} EUR als geringster Tagespreis. Das EBITDA liegt nach aktuellen Zahlen bei {vow3ebitda}. {vow350daymovavg} EUR beträgt der 50-Tage-Durchschnitt. Der 200-Tage-Durschnitt liegt bei {vow3200daymovavg} EUR. Das Unternehmen zählt zu den Dogs Of The Dax.\nDogs Of The Dax wird komplettiert von der Deutschen Post AG (XFRA:DPW). Hier wurde mit {dpwopen} EUR heute Morgen der Handel begonnen. Das Tageshoch verzeichnete die Aktie bei {dpwdayhigh} EUR. Der Tiefstand betrug {dpwdaylow} EUR. Das EBITDA des Unternehmens liegt bei {dpwebitda}. Die Tagesdurchschnitte über 50- und 200-Tage verzeichnen jeweils {dpw50daymovavg} EUR und {dpw50daymovavg}. Jetzt liegt die Aktie bei {dpwpreis}. Die Deutsche Post AG zählt zu den regulären Dogs Of The Dax.\nDieser Artikel wurde automatisch erstellt. Dafür werden Daten von Yahoo Finance analysiert und in einem Börsenbericht ausgewertet. Die Kursdaten können zeitverzögert sein. Alle Texte sowie die Hinweise und Informationen stellen keine Anlageberatung oder Empfehlung zum Kauf oder Verkauf von Wertpapieren dar (§ 85 WpHG). Sie dienen lediglich der persönlichen Information und geben ausschließlich die Meinung des Autors wieder. Es wird keine Empfehlung für eine bestimmte Anlagestrategie abgegeben. Die Inhalte von dogsofthedax.com richten sich ausschließlich an natürliche Personen mit Wohnsitz in der Bundesrepublik Deutschland.\nDie veröffentlichten Artikel, Analysen, Daten, Tools und Prognosen sind mit größter Sorgfalt und nach bestem Wissen und Gewissen recherchiert und erstellt. Die Quellen wurden als vertrauenswürdig erachtet. Eine Garantie, Gewährleistung oder Haftung für die Richtigkeit, Vollständigkeit und Aktualität der zur Verfügung gestellten Inhalte und Informationen kann nicht übernommen werden.\nStand: {weekday}, {now}, {uhrzeitjz}'
post.id = your_blog.call(posts.NewPost(post))
post.post_status = 'draft'
your_blog.call(posts.EditPost(post.id, post))