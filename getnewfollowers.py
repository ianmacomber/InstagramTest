from instagram.client import InstagramAPI

INSTAGRAM_CLIENT_ID = 'ab909284384242d3a9588475d3974c92'
INSTAGRAM_CLIENT_SECRET = 'e3e3ceff63c3415b971e7d8d217f6181'

#api = InstagramAPI(client_id=INSTAGRAM_CLIENT_ID, client_secret=INSTAGRAM_CLIENT_SECRET)
api = InstagramAPI(access_token='560816190.ab90928.76d186dd69074303a931540389cdfa84')

# This section shows how to get the number of followers for a specific user
slalomtokyodrift = api.user(560816190)
print(slalomtokyodrift.id)
print(slalomtokyodrift.counts['followed_by'])

# Now we are going to get a list of the users that liked my most recent picture.
userfeed = api.user_recent_media(user_id=560816190, count=1)

print(userfeed)
'''
([Media: 943764376376221251_560816190], 'https://api.instagram.com/v1/users/560816190/media/recent?access_token=560816190.ab90928.76d186dd69074303a931540389cdfa84&count=1&max_id=943764376376221251_560816190')
'''

a = userfeed[0]
print(a)
# [Media: 943764376376221251_560816190]
print('\n')


mediafile = a[0]
print(mediafile)
# Media: 943764376376221251_560816190

# Everyone who has liked my most recent file
print(api.media_likes(mediafile.id))

recentlikers = api.media_likes(mediafile.id)

print(recentlikers[0])
print(recentlikers[0].id)

# SO what's going on here is that if someone is private we can't see their followers.
# That's probably fine here because I only care about those that are public.
# Try catch in the for loop
print("Check 1")
guy = api.user(recentlikers[0].id)
#guy = api.user(369668590)
print("Check 2")

print(guy.username)


print("Check")

print(guy.full_name)
print(guy.website)

print(guy.counts['followed_by'])

