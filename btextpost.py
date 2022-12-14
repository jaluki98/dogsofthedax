# -*- coding: utf-8 -*-
from time import gmtime, strftime
from datetime import date as dt
from datetime import datetime as datet
from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc import WordPressPost
import yahoo_fin.stock_info as si
from yahoo_finance import Share

#-------------------------------------------
#Stocks
bmwquote_table = si.get_quote_table("BMW.DE")
bmwpreis = round(bmwquote_table["Quote Price"], 2)
bmwkursziel = bmwquote_table["1y Target Est"]
bmwdayrange = bmwquote_table["Day's Range"]
bmwopen = round(bmwquote_table["Open"], 2)
bmw52wrange = bmwquote_table["52 Week Range"]
bmwveraenderung = round(bmwpreis - bmwopen, 2)

basquote_table = si.get_quote_table("BAS.DE")
baspreis = round(basquote_table["Quote Price"], 2)
baskursziel = basquote_table["1y Target Est"]
basdayrange = basquote_table["Day's Range"]
basopen = round(basquote_table["Open"], 2)
bas52wrange = basquote_table["52 Week Range"]
basveraenderung = round(baspreis - basopen, 2)

baynquote_table = si.get_quote_table("BAYN.DE")
baynpreis = round(baynquote_table["Quote Price"], 2)
baynkursziel = baynquote_table["1y Target Est"]
bayndayrange = baynquote_table["Day's Range"]
baynopen = round(baynquote_table["Open"], 2)
bayn52wrange = baynquote_table["52 Week Range"]
baynveraenderung = round(baynpreis - baynopen, 2)

eoanquote_table = si.get_quote_table("EOAN.DE")
eoanpreis = round(eoanquote_table["Quote Price"], 2)
eoankursziel = eoanquote_table["1y Target Est"]
eoandayrange = eoanquote_table["Day's Range"]
eoanopen = round(eoanquote_table["Open"], 2)
eoan52wrange = eoanquote_table["52 Week Range"]
eoanveraenderung = round(eoanpreis - eoanopen, 2)

alvquote_table = si.get_quote_table("ALV.DE")
alvpreis = round(alvquote_table["Quote Price"], 2)
alvkursziel = alvquote_table["1y Target Est"]
alvdayrange = alvquote_table["Day's Range"]
alvopen = round(alvquote_table["Open"], 2)
alv52wrange = alvquote_table["52 Week Range"]
alvveraenderung = round(alvpreis - alvopen, 2)

muv2quote_table = si.get_quote_table("MUV2.DE")
muv2preis = round(muv2quote_table["Quote Price"], 2)
muv2kursziel = muv2quote_table["1y Target Est"]
muv2dayrange = muv2quote_table["Day's Range"]
muv2open = round(muv2quote_table["Open"], 2)
muv252wrange = muv2quote_table["52 Week Range"]
muv2veraenderung = round(muv2preis - muv2open, 2)

dtequote_table = si.get_quote_table("DTE.DE")
dtepreis = round(dtequote_table["Quote Price"], 2)
dtekursziel = dtequote_table["1y Target Est"]
dtedayrange = dtequote_table["Day's Range"]
dteopen = round(dtequote_table["Open"], 2)
dte52wrange = dtequote_table["52 Week Range"]
dteveraenderung = round(dtepreis - dteopen, 2)

siequote_table = si.get_quote_table("SIE.DE")
siepreis = round(siequote_table["Quote Price"], 2)
siekursziel = siequote_table["1y Target Est"]
siedayrange = siequote_table["Day's Range"]
sieopen = round(siequote_table["Open"], 2)
sie52wrange = siequote_table["52 Week Range"]
sieveraenderung = round(siepreis - sieopen, 2)

vow3quote_table = si.get_quote_table("VOW3.DE")
vow3preis = round(vow3quote_table["Quote Price"], 2)
vow3kursziel = vow3quote_table["1y Target Est"]
vow3dayrange = vow3quote_table["Day's Range"]
vow3open = round(vow3quote_table["Open"], 2)
vow352wrange = vow3quote_table["52 Week Range"]
vow3veraenderung = round(vow3preis - vow3open, 2)

dpwquote_table = si.get_quote_table("DPW.DE")
dpwpreis = round(dpwquote_table["Quote Price"], 2)
dpwkursziel = dpwquote_table["1y Target Est"]
dpwdayrange = dpwquote_table["Day's Range"]
dpwopen = round(dpwquote_table["Open"], 2)
dpw52wrange = dpwquote_table["52 Week Range"]
dpwveraenderung = round(dpwpreis - dpwopen, 2)

daxquote_table = si.get_quote_table('^GDAXI')
daxpreis = round(daxquote_table["Quote Price"], 2)
daxdayrange = daxquote_table["Day's Range"]
daxopen = round(daxquote_table["Open"], 2)
dax52wrange = daxquote_table["52 Week Range"]
daxveraenderung = round(daxpreis - daxopen, 2)


if daxveraenderung >= 0:
	daxfarbe = 'gr??nen'
	stimmung = 'positive'

else:
	daxfarbe = 'roten'
	stimmung = 'negative'

#-------------------------------------------
#Zeit

today_date = dt.today()
now = today_date.strftime("%d/%m/%Y")
nowslug = today_date.strftime("%d_%m_%y")
uhrzeitjz = strftime("%Y-%m-%d %H:%M:%S", gmtime())

#Wochentag

zeitwochentag = datet.now()
wochentag = zeitwochentag.weekday()

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
def posttitel():
	return f'Die Dogs Of The DAX am heutigen {weekday} - R??ckblick auf den Handelstag ({nowslug})'
#print(f'Das ist ein Test. BMW kostet {bmwpreis} EUR.')
def postinhalt():
	return f'Nach B??rsenschluss ergeben sich r??ckblickend auf den Handelstag folgende Stellungnahmen:\n\nDer DAX beendet den heutigen Handelstag mit {daxfarbe} Zahlen und, einem Endstand von {daxpreis} Punkten. Am Morgen stand er bei {daxopen} Z??hlern. ??ber den Tagesverlauf gab es eine Ver??nderung von {daxveraenderung} Punkten. Die Tagesh??chst- und Niedrigwerte betrugen {daxdayrange}.\n\nIm Verlauf des heutigen {weekday}s ({now}) haben die zehn Dogs Of The DAX die {stimmung} Stimmung des deutschen Leitindexes wie folgt genutzt:\n\nAngefangen bei dem Pharmagiganten Bayer AG (XFRA:BAYN) betr??gt der Kurs nun {baynpreis} EUR. In den Tag startete die Aktie mit {baynopen} EUR. Das Hoch und Tief wurde heute jeweils bei {bayndayrange} EUR notiert. Zum jetzigen Zeitpunkt betr??gt die 52-Week-Range {bayn52wrange} EUR. Das Kursziel von Bayer liegt bei {baynkursziel} EUR. Das Unternehmen z??hlt zu den Dogs Of The DAX und Small Dogs Of The DAX.\n\n\n\nDas Wertpapier des Chemie-Unternehmen BASF (XFRA:BAS) ist nach B??rsenschluss mit {baspreis} EUR notiert. Am Morgen stand das Papier bei {basopen} EUR, und hat sich somit um {basveraenderung} EUR ??ber den Tag ver??ndert. ??ber den Tagesverlauf schwankte die Aktie zwischen {basdayrange} EUR. Im 52-Wochen-Verlauf ist das Papier mit {bas52wrange} EUR notiert. BASF SE (XFRA:BAS) z??hlt 2021 zu den Dogs Of The DAX und Small Dogs Of The DAX.\n\nE.ON hat den Tag mit einem Aktienpreis von {eoanpreis} EUR beendet. Dem zugrunde liegen Schwankungen ??ber {eoandayrange} EUR. In den Handel gestartet ist das Wertpapier mit einem Wert von {eoanopen} EUR. Das Kursziel von E.ON liegt bei {eoankursziel}. Die Schwankungen in den letzten 52 Wochen betragen {eoan52wrange} EUR. E.ON SE (XFRA:EOAN) befindet sich in den Small Dogs Of The DAX, wie auch in den diesj??hrigen regul??ren Dogs Of The DAX.\n\nAllianz, mit dem Symbol ALV (XFRA) steht momentan bei {alvpreis} EUR. Zu Beginn des Handelstags notierte die Aktie {alvopen} EUR. Im direkten Vergleich ist das eine Ver??nderung von {alvveraenderung} EUR ??ber den Tag. Das Kursziel mit 12-Monats-Ausblick liegt bei {alvkursziel} EUR. ??ber den Tag ergaben sich folgende Kursschwankungen: {alvdayrange} EUR. \n\nDas Versicherungsunternehmen z??hlt zu den regul??ren Dogs Of The DAX und nicht zu den Small Dogs Of The DAX.\n\nDie Muenchener R??ckvers. AG (XFRA:MUV2) notierte nach der Closing-Bell {muv2preis} EUR. ??ber den Tag schwankte die Aktie zwischen {muv2dayrange} EUR. Der Preis zum Handelsstart heute morgen Betrug {muv2open} EUR. Das Kursziel des Versicherungsunternehmen liegt bei {muv2kursziel} EUR. ??ber die letzten 52-Wochen gab die nachfolgenden Schwankungen: {muv252wrange} EUR. Die Aktie mit dem Ticker-Symbol XFRA:MUV2 z??hlt zu den Dogs Of The DAX.\n\nDas Telekommunikationsunternehmen Deutsche Telekom AG, steht nachb??rslich bei einem Wert von {dtepreis} EUR. Heute Morgen, bei Handelsbeginn lag das Papier bei {dteopen} EUR. Die Schwankungen im Tagesverlauf sehen wie folgt aus: {dtedayrange} EUR. Das Kursziel betr??gt {dtekursziel}. Die Kurshistorie verzeichnet in den letzten 52-Wochen eine Bewegung von {dte52wrange} EUR. Das Unternehmen mit Hauptfirmensitz in Bonn, Nordrhein-Westfalen f??llt unter die Kategorien Dogs Of The DAX, und Small Dogs Of The DAX.\n\nDer Automobilhersteller BMW notiert {bmwpreis} EUR zum momentanen Zeitpunkt der Ver??ffentlichung dieses Artikels. Mit der exakten Bezeichnung Bayerische Motoren Werke AG (XFRA:BMW) schwankte das Wertpapier am heutigen {weekday} zwischen {bmwdayrange} EUR. Das aktuelle Kursziel von BMW liegt bei {bmwkursziel} EUR. In den Handel startete die Aktie heute mit {bmwopen} EUR. ??ber den Tag ver??nderte sich die Aktie um {bmwveraenderung} EUR. Die 52-Wochen Historie zeigt: {bmw52wrange} EUR. Das Wertpapier z??hlt zu den Dogs Of The DAX, sowie den Small Dogs Of The DAX als teuerstes Wertpapier in dieser Kategorie.\n\nDie Siemens AG (XFRA:SIE) lag heute Morgen zu Handelsbeginn bei einem Preis von {sieopen} EUR. ??ber den Tag entwickelten sich Schwankungen zwischen {siedayrange} EUR. Die 52-Wochen-Historie zeigt ein Tief und Hoch von {sie52wrange} EUR. Nach dem Handelstag (stand jetzt) liegt das Papier bei {siepreis} EUR, was einer Differnz von {sieveraenderung} EUR zu heute Morgen entspricht.\n\nVolkswagen notiert zum aktuellen Zeitpunkt {vow3preis} EUR. Mit {vow3open} EUR startete die Aktie des Automobilherstellers heute Morgen in den Handel. Die Tagesschwankungen betrugen: {vow3dayrange} EUR. Das Kursziel der VW Aktie liegt nach aktuellem Stand bei {vow3kursziel} EUR. {vow352wrange} EUR betr??gt die 52-Week-Range. Das Unternehmen z??hlt zu den Dogs Of The DAX.\n\nDie 2021 Dogs Of The DAX werden komplettiert von der Deutschen Post AG (XFRA:DPW). Hier wurde der Handel heute Morgen mit {dpwopen} EUR eingel??utet. Das Tageshoch und Tagestief wurde verzeichnet bei {dpwdayrange} EUR. Das Kursziel der Aktie / des Unternehmens liegt bei {dpwkursziel} EUR. Der Verlauf der letzten 52-Wochen zeigt einen Niedrig- und H??chststand von {dpw52wrange} EUR. Nach B??rsenschluss liegt die Aktie bei {dpwpreis} EUR. Die Deutsche Post AG z??hlt zu den regul??ren Dogs Of The DAX.\n\n\n\nDieser Artikel wurde automatisch erstellt. Daf??r werden Daten von Yahoo Finance analysiert und in einem B??rsenbericht ausgewertet. Die Kursdaten k??nnen zeitverz??gert sein. Alle Texte sowie die Hinweise und Informationen stellen keine Anlageberatung oder Empfehlung zum Kauf oder Verkauf von Wertpapieren dar (?? 85 WpHG). Sie dienen lediglich der pers??nlichen Information und geben ausschlie??lich die Meinung des Autors wieder. Es wird keine Empfehlung f??r eine bestimmte Anlagestrategie abgegeben. Die Inhalte von dogsofthedax.com richten sich ausschlie??lich an nat??rliche Personen mit Wohnsitz in der Bundesrepublik Deutschland.\n\nDie ver??ffentlichten Artikel, Analysen, Daten, Tools und Prognosen sind mit gr????ter Sorgfalt und nach bestem Wissen und Gewissen recherchiert und erstellt. Die Quellen wurden als vertrauensw??rdig erachtet. Eine Garantie, Gew??hrleistung oder Haftung f??r die Richtigkeit, Vollst??ndigkeit und Aktualit??t der zur Verf??gung gestellten Inhalte und Informationen kann nicht ??bernommen werden.'
