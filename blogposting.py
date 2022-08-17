import requests
import json
import base64
import btextpost
import imageuploadwp

beitrag = btextpost.postinhalt()
titel = btextpost.posttitel()

url = 'http://dogsofthedax.com/wp-json/wp/v2'

user = 'janlukaskiermeyer'
password = 'Dx0C yb2d OSSj AHrM yHjG 5Vi4'

creds = user + ':' + password

token = base64.b64encode(creds.encode())

header = {'Authorization': 'Basic ' + token.decode('utf-8')}

id= imageuploadwp.postid

post = {
	#'date': '2020-02-17T21:00:00',
	'title': titel,
	'content': beitrag,
	'status': 'publish',
	'featured_media': id,
	'categories': '6'
}

r = requests.post(url + '/posts', headers=header, json=post)
#def komplettesposting():
print(r)