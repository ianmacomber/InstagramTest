from instagram.client import InstagramAPI
import operator
import time

INSTAGRAM_CLIENT_ID = 'ab909284384242d3a9588475d3974c92'
INSTAGRAM_CLIENT_SECRET = 'e3e3ceff63c3415b971e7d8d217f6181'

#api = InstagramAPI(client_id=INSTAGRAM_CLIENT_ID, client_secret=INSTAGRAM_CLIENT_SECRET)
api = InstagramAPI(access_token='560816190.ab90928.76d186dd69074303a931540389cdfa84')

# This section shows how to get the number of followers for a specific user
slalomtokyodrift = api.user(560816190)

# Here we are putting our most recent 150 followers into a dictionary, sorting by order, and saving it.

# Now we are going to get a list of the users that liked my most recent picture.
# userfeed = api.user_recent_media(user_id=560816190, count=1)
# Trying to use slalomtokyodrift as a stored user failed because method expects an int
userfeed = api.user_recent_media(user_id=slalomtokyodrift.id, count=1)

print(userfeed)
'''
([Media: 943764376376221251_560816190], 'https://api.instagram.com/v1/users/560816190/media/recent?access_token=560816190.ab90928.76d186dd69074303a931540389cdfa84&count=1&max_id=943764376376221251_560816190')
'''
# This was the old solution:
'''
a = userfeed[0]
print(a)
mediafile = a[0]
print(mediafile)
'''
# This works just as well so we will use it now.
print(userfeed[0][0])
# Media: 943764376376221251_560816190

# Everyone who has liked my most recent file
print(api.media_likes(userfeed[0][0].id))

recentlikers = api.media_likes(userfeed[0][0].id)

# Now what we want to do is write all of these people into a dictionary with likes
allusers = {}

print(len(recentlikers))
print(recentlikers[0])
print(recentlikers[0].id)

# This worked perfectly.  Print the range of lists.
for i in range(len(recentlikers)):
    try:
        guy = api.user(recentlikers[i].id)
        allusers.update({guy.username:guy.counts['followed_by']})
    except:
        pass

# old
# print(allusers)
# new prints everything
print(sorted(allusers.items(), key=operator.itemgetter(1)))

# Next step is to do this for a lot of media.
allusers = {}
userfeed = api.user_recent_media(user_id=slalomtokyodrift.id, count=20)
print(userfeed)
print("The length of the user feed is: ", len(userfeed))

'''
([Media: 946674877296975191_560816190, Media: 946590435161316376_560816190, Media: 946523401878675397_560816190, Media: 946462028826058625_560816190, Media: 946335711698787874_560816190, Media: 946265158027747105_560816190, Media: 945871598195481778_560816190, Media: 945782329422552534_560816190, Media: 945658329841180408_560816190, Media: 945616810081951315_560816190, Media: 945256369363263311_560816190, Media: 945195853970316597_560816190, Media: 945129801743769177_560816190, Media: 945051285765397890_560816190, Media: 944996705664933758_560816190, Media: 944893818221796566_560816190, Media: 944817445960588849_560816190, Media: 944501488696335663_560816190, Media: 944318377731727220_560816190, Media: 944266530891407007_560816190], 'https://api.instagram.com/v1/users/560816190/media/recent?access_token=560816190.ab90928.76d186dd69074303a931540389cdfa84&count=20&max_id=944266530891407007_560816190')
'''

#allusers
#print(userfeed[0])
#print("The ACTUAL length of the user feed is: ", len(userfeed[0]))

'''
[Media: 946674877296975191_560816190, Media: 946590435161316376_560816190, Media: 946523401878675397_560816190, Media: 946462028826058625_560816190, Media: 946335711698787874_560816190, Media: 946265158027747105_560816190, Media: 945871598195481778_560816190, Media: 945782329422552534_560816190, Media: 945658329841180408_560816190, Media: 945616810081951315_560816190, Media: 945256369363263311_560816190, Media: 945195853970316597_560816190, Media: 945129801743769177_560816190, Media: 945051285765397890_560816190, Media: 944996705664933758_560816190, Media: 944893818221796566_560816190, Media: 944817445960588849_560816190, Media: 944501488696335663_560816190, Media: 944318377731727220_560816190, Media: 944266530891407007_560816190]
'''

#print(userfeed[0][1])

for j in range(len(userfeed[0])):
    #print(j)
    #print(userfeed[0][j])
    #print(userfeed[0][j])
    #print(type(userfeed[0][j]))
    recentlikers = api.media_likes(userfeed[0][j].id)
    #print(recentlikers)

    for i in range(len(recentlikers)):
        #try:
        #    # Make this only call the API if the person isn't in our top 1000.
        #    guy = api.user(recentlikers[i].id)
        #    print(guy) # Same thing
        #    print(recentlikers[i]) # Same thing
        #    print(recentlikers[i].id)
        #    print(type(guy))
        #    print(type(recentlikers[i]))
        #    allusers.update({guy.username:guy.counts['followed_by']})
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
