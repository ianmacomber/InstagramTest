from instagram.client import InstagramAPI
import operator
import time
import json

INSTAGRAM_CLIENT_ID = 'ab909284384242d3a9588475d3974c92'
INSTAGRAM_CLIENT_SECRET = 'e3e3ceff63c3415b971e7d8d217f6181'

#api = InstagramAPI(client_id=INSTAGRAM_CLIENT_ID, client_secret=INSTAGRAM_CLIENT_SECRET)
api = InstagramAPI(access_token='560816190.ab90928.76d186dd69074303a931540389cdfa84')

# This section shows how to get the number of followers for a specific user
slalomtokyodrift = api.user(560816190)

# Here we are putting our most recent 150 followers into a dictionary, sorting by order, and saving it.

# Next step is to do this for a lot of media.
allusers = {}
userfeed = api.user_recent_media(user_id=slalomtokyodrift.id, count=20)

for j in range(len(userfeed[0])):
    recentlikers = api.media_likes(userfeed[0][j].id)
    
    for i in range(len(recentlikers)):    
        try:
            if recentlikers[i].username in allusers.keys():
                print("Already got {0}".format(recentlikers[i]))
            else:
                guy = api.user(recentlikers[i].id)
                allusers.update({guy.username:guy.counts['followed_by']})
                print("Added {0}".format(guy.username))
                time.sleep(1)
        except:
            pass

print(sorted(allusers.items(), key=operator.itemgetter(1)))

json.dump(allusers, open("text.txt", 'w'))
