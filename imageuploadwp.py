import requests
import json
import base64

#chartfile = '/dogs_of_the_dax_charttwitterupdate.jpg'#'/dogs_of_the_daxcharttwitterupdate.jpg'
#upload_url = 'http://dogsofthedax.com/wp-content/uploads/2021/02/'

user = 'janlukaskiermeyer'
pythonapp = 'Dx0C yb2d OSSj AHrM yHjG 5Vi4'

#######################

# This code is based on the post of the user smaffulli @ https://discussion.dreamhost.com/t/how-to-post-content-to-wordpress-using-python-and-rest-api/65166

url = 'http://www.dogsofthedax.com/wp-json/wp/v2' # the url of the wp access loc
token = base64.standard_b64encode((user + ':' + pythonapp).encode('utf-8')) # we have to encode the usr and pw
headers = {'Authorization': 'Basic ' + token.decode('utf-8')} # here we define which the auth. type used

media = {'file': open('Barchart_Einzelaktien_Dogs.jpg','rb')} # 'picture.jpg' path to the image, we load it as a binary file

image = requests.post(url + '/media', headers=headers, files=media) # create a post request with the file
link = json.loads(image.content.decode('utf-8'))['link'] # get the link to the image out of the response
postid =json.loads(image.content.decode('utf-8'))['id'] # get the post-id of the image out of the response (we will use it further down to change the wp-image parameters)
print('Bild bei: {} veröffentlicht. ID: {}'.format(link, postid))