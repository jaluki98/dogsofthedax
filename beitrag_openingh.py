from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc import WordPressPost
import datetime as dt


#Time
today_date = dt.date.today()
now = today_date.strftime("%d/%m/%Y")
nowslug = today_date.strftime("%d_%m_%y")

#Beitrag
beitragtext = open('beitragopening.txt', 'r').read()

#Wordpress
your_blog = Client('http:dogsofthedax.com', 'janlukaskiermeyer', 'Ginf3j98-grh834-3fh934n')

myposts=your_blog.call(posts.GetPosts())

post = WordPressPost()
post.title = '{now}: Dogs of The Dax Opening Hours'
post.slug='{nowslug}_dogs_of_the_dax_opening_hours'
post.content = 'Hi'
post.id = your_blog.call(posts.NewPost(post))
post.post_status = 'publish'
your_blog.call(posts.EditPost(post.id, post))