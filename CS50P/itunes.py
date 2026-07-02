# API --> Application programming interfaces are third-party services that we can talk to through our code (pretend to be a browser, connect to that APi, and get something to use in our program). 

# Mostly the APIs are available on the internet nowadays and can be accessed using a web browser 
# for example itunes api : https://itunes.apple.com/search?entity=song&limit=1&term=weezer

# this downloads a text file in your downloads folder (API docs)

# requests module allows us to make web requests(http/https)
# pypi.org/project/requests


# the request returns a JSON type text. language agnostic format to exchange data.

import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

# res = requests.get('https://itunes.apple.com/search?entity=song&limit=1&term='+sys.argv[1])
# print(json.dumps(res.json(),indent=2)) # tells the computer "Hey, this is JSON"

# The response we get back is good and somewhat understandable like lists / dictionaries etc (coincedentally the same syntax). but it needs to be formatted in a proper way so we use json module for that.

# Observation : trackName is a key inside the dictionary which is inside the dictionary which is at the [0] index of a list which is called results. Use Paper Pen for this

# Lets see if we can get 12 songs from weezer

# limit=12

res = requests.get('https://itunes.apple.com/search?entity=song&limit=12&term='+sys.argv[1])

print()

# convert the response using res.json and store it.
for song in res.json()["results"]:
    print(song["trackName"])