import facebook

fbtoken = 'EAADzOZBZAyuRYBAGmXw8Rjn1havpQfHLWXPQVh3I8ItJMbz1KhMOyNM7wcNTlZAbzGiY2aHKtHJxrXZCMiFB5eaAThZAsvVdT0gXC681UBwBLyZCLs2ZAHd06rTOXRfL9RQgG2mZAHqsZBRc5BLhzqM9RGsUTwZAB3ee1qz28g0sBSjl9uzZCsC9Gj5'

graph = facebook.GraphAPI(access_token=fbtoken)
#to post to your wall
graph.put_object("me", "feed", message="Posting on my wall!")