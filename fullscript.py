from instagram.client import InstagramAPI
import operator
import time
import json
import sys

INSTAGRAM_CLIENT_ID = 'ab909284384242d3a9588475d3974c92'
INSTAGRAM_CLIENT_SECRET = 'e3e3ceff63c3415b971e7d8d217f6181'

#api = InstagramAPI(client_id=INSTAGRAM_CLIENT_ID, client_secret=INSTAGRAM_CLIENT_SECRET)
api = InstagramAPI(access_token='560816190.ab90928.76d186dd69074303a931540389cdfa84')

# This section shows how to get the number of followers for a specific user
slalomtokyodrift = api.user(560816190)

# Here we are putting our most recent 150 followers into a dictionary, sorting by order, and saving it.

# Next step is to do this for a lot of media.
allusers = {} # This is eventually going to be where we put in the existing dictionary to add.

# Add the existing text file
d = open("text2.txt", "r")
lines = d.readlines()
a = len(lines[0])-1
b = lines[0][1:a]
bstrip = b.split(",")

for i in bstrip:
    c, d = i.replace(" ", "").replace('"', '').split(":")
    allusers[c] = int(d)

firstlen = len(allusers)

print("Current dictionary has {0} people".format(firstlen))

increment = 0
while increment < 2:
    # Get the most recent picture
    try:
        userfeed = api.user_recent_media(user_id=slalomtokyodrift.id, count=1)
        recentlikers = api.media_likes(userfeed[0][0].id) # This might not be a list of lists anymore
    # If it doesn't work, wait 500 seconds and return to the top of the while loop.
    # But there are two kinds of errors -- one is too many API calls, one is a call to a private user!
    # So what I need to do is add PRIVATE USERS to the dicionary as well with a zero.
    except:
        print("API Error getting most recent pic")
        e = sys.exc_info()[0]
        print(e)
        time.sleep(500)
        continue

    # For each of the most recent likers
    for i in range(len(recentlikers)):    
        try:
            if recentlikers[i].username in allusers.keys():
                pass
                #print("Already got {0}".format(recentlikers[i]))
            else:
                 guy = api.user(recentlikers[i].id)
                 allusers.update({guy.username:guy.counts['followed_by']})
                 print("Added public user {0} ".format(guy.username), time.strftime("%Y-%m-%d %H:%M:%S"))
                 time.sleep(.5)
        # If the user is private, add them.
        except:
            if recentlikers[i].username in allusers.keys():
                pass
            else:
                allusers.update({recentlikers[i].username:0})
                print("Added private user {0} ".format(recentlikers[i]), time.strftime("%Y-%m-%d %H:%M:%S"))
            #e = sys.exc_info()[0]
            #print(e)
            time.sleep(.5)
            pass
    
    increment = increment + 1
    print("We are on increment {0}".format(increment))
    time.sleep(50)

print(sorted(allusers.items(), key=operator.itemgetter(1)))
print("We added {0} users.".format(len(allusers)-firstlen))

json.dump(allusers, open("text2.txt", 'w'))
