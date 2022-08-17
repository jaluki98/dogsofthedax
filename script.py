# -*- coding: utf-8 -*-
import tweepy
import stocksscript
import time as tmes
from datetime import datetime as dt
import facebook
import sys
import os

#Facebook Token
fbtoken = 'EAADzOZBZAyuRYBAPe3D1wbSSUSQfekT1eV2vcF62Df7d47Bx1OZBLrSo0M4aQsE9f6AtjwurqGSidQBxw5b9VmCyJJewoT83ZBYha0V1OeA88xJ5MtQ06ZBzAa5D5J9bY4nwVPX329YwQFkIkmlntiadQeAmCbePyJwFLlE3xpwZDZD'
graph = facebook.GraphAPI(access_token=fbtoken)

#Keys und Token Twitter
CONSUMER_KEY = 'QA8MwyQ7vU0Kej5DqJpYg7rr1'
CONSUMER_SECRET = 'YzUGJMNuqO6YClqWT0pz8gKnC5TzSz11mU1Ha2cmGSfvQrynFB'
ACCESS_KEY = '1353817832665083904-vlvn3FzZTm6k5wOCWaPW9epcA2uako'
ACCESS_SECRET = 'wuisfjGULZ4wWdTW9Cv2NyTxVRJxqLzMD1FJxzfGCDs4x'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True,
	wait_on_rate_limit_notify=True)

#----------------------------------------------------------------------
eins = 'ein'

output1 = stocksscript.bayerstart()
output2 = stocksscript.bayerschluss()

output3 = stocksscript.basfstart()
output4 = stocksscript.basfschluss()

output5 = stocksscript.eoanstart()
output6 = stocksscript.eoanschluss()

output7 = stocksscript.allianzstart()
output8 = stocksscript.allianzschluss()

output9 = stocksscript.muvrstart()
output10 = stocksscript.muvrschluss()

output11 = stocksscript.telekomstart()
output12 = stocksscript.telekomschluss()

output13 = stocksscript.bmwstart()
output14 = stocksscript.bmwschluss()

output15 = stocksscript.siemensstart()
output16 = stocksscript.siemensschluss()

output17 = stocksscript.volkswagenstart()
output18 = stocksscript.volkswagenschluss()

output19 = stocksscript.deutschepoststart()
output20 = stocksscript.deutschepostschluss()

output21 = stocksscript.wochenende()

while eins == 'ein':
	time = dt.now()
	minutes = time.minute
	hours = time.hour
	seconds = time.second
	day = time.weekday()

	if minutes == 00 and hours == 8 and day < 5:
		api.update_status(output1)
		api.update_status(output3)
		api.update_status(output5)
		api.update_status(output7)
		api.update_status(output9)
		api.update_status(output11)
		api.update_status(output13)
		api.update_status(output15)
		api.update_status(output17)
		api.update_status(output19)
		tmes.sleep(5)
		#graph.put_object("me", "feed", message=output1 + '\n\n' + output3 + '\n\n' + output5 + '\n\n' + output7 + '\n\n' + output9 + '\n\n' + output11 + '\n\n' + output13 + '\n\n' + output15 + '\n\n' + output17 + '\n\n' + output19)
		print('Opening Posts gepostet')

	elif minutes == 0 and hours == 20 and day < 5:
		exec(open('barchart.py').read())
		tmes.sleep(50)

	elif minutes == 3 and hours == 20 and day < 5:
		exec(open('charts.py').read())
		tmes.sleep(50)
		print('Charts für heute generiert')

	elif minutes == 24 and hours == 16:
		print("Neustart in 60 Sekunden...")
		tmes.sleep(60)
		os.system("python3 script.py")
		exit()

	elif minutes == 24 and hours == 0:
		print("Neustart in 60 Sekunden...")
		tmes.sleep(60)
		os.system("python3 script.py")
		exit()

	elif minutes == 0 and hours == 15 and day < 5:
		exec(open('barchart.py').read())
		tmes.sleep(60)
		tweet_text_mittag = 'Es ist kurz nach 15 Uhr. Anbei gibt es den täglich Zwischenbericht zu den Dogs Of The DAX. Weitere Informationen unter: dogsofthedax.com #DogsOfTheDAX'
		image_path_mittag = 'Barchart_Einzelaktien_Dogs.jpg'
		api.update_with_media(image_path_mittag, tweet_text_mittag)

	elif minutes == 7 and hours == 20 and day < 5:
		api.update_status(output2)
		api.update_status(output4)
		api.update_status(output6)
		api.update_status(output8)
		api.update_status(output10)
		api.update_status(output12)
		api.update_status(output14)
		api.update_status(output16)
		api.update_status(output18)
		api.update_status(output20)
		tmes.sleep(15)
		#graph.put_object("me", "feed", message=output2 + '\n\n' + output4 + '\n\n' + output6 + '\n\n' + output8 + '\n\n' + output10 + '\n\n' + output12 + '\n\n' + output14 + '\n\n' + output16 + '\n\n' + output18 + '\n\n' + output20)
		#tmes.sleep(20)
		#print('Closing Tweets gepostet')
		#graph.put_photo(image=open('dogs_of_the_dax_charttwitterupdate.jpg', 'rb'), message='Der aktuelle Chart, welcher die Jahres-Performance des DAX-Index mit den Dogs Of The DAX und Small Dogs Of The DAX vergleicht. Weitere Informationen unter: http://dogsofthedax.com')
		#tmes.sleep(15)
		#graph.put_photo(image=open('Barchart_Einzelaktien_Dogs.jpg', 'rb'), message='Anbei der tägliche Chart, welcher die Tagesveränderung der Einzelaktien der diesjährigen Dogs Of The DAX visualisiert darstellt. Weitere Informationen unter: http://dogsofthedax.com')
		#print('Facebook beide Bilder gepostet')
		#tmes.sleep(20)
		import blogposting
		#tmes.sleep(60)
		print('Tagesbericht auf Wordpress veroeffentlicht')
		tmes.sleep(30)
		import instapost
		print("Instagram Post veröffentlicht")

	elif minutes == 15 and hours == 20 and day == 4:
		api.update_status(output21)
		#graph.put_object("me", "feed", message=output21)
		print('Handelswochenende gepostet')
		tmes.sleep(15)


	elif minutes == 00 and hours == 21 and day < 5:
		tweet_text_1 = 'Der aktuelle Chart, welcher die YTD-Performance des #DAX mit den #DogsOfTheDAX vergleicht wird auf Twitter an jedem Wochentag um 21:00 Uhr veröffentlicht. Weitere Informationen unter: dogsofthedax.com #DogsOfTheDAX'
		image_path_1 = 'dogs_of_the_dax_charttwitterupdate.jpg'
		api.update_with_media(image_path_1, tweet_text_1)
		tmes.sleep(30)
		tmes.sleep(35)
		tweet_text_2 = 'Anbei der tägliche Chart, welcher die Tagesveränderung der Einzelaktien der diesjährigen Dogs Of The DAX visualisiert darstellt. Weitere Informationen unter: dogsofthedax.com #DogsOfTheDAX'
		image_path_2 = 'Barchart_Einzelaktien_Dogs.jpg'
		api.update_with_media(image_path_2, tweet_text_2)

	elif seconds % 6 == 0:
		print('Ein paar neuen Personen gefolgt, mit dem Stichwort Aktien (Minute: ',minutes,')')
		from followbot import auto_follow
		auto_follow("Aktien", count=2)

	elif seconds % 7 == 0:
		print('Ein paar neuen Personen gefolgt, mit dem Stichwort Börse (Minute: ',minutes,')')
		from followbot import auto_follow
		auto_follow("Börse", count=2)

	#elif minutes == 40:
		#import tests

	print('Läuft frei. Uhrzeit: ', minutes, ' Minuten - ', hours, 'Stunden - ', day, 'Tag')
	tmes.sleep(60)
