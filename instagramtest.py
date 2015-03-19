from PIL import Image
from instagram.client import InstagramAPI


# Adding key and secret
INSTAGRAM_CLIENT_ID = 'ab909284384242d3a9588475d3974c92'
INSTAGRAM_CLIENT_SECRET = 'e3e3ceff63c3415b971e7d8d217f6181'

#api = InstagramAPI(client_id=INSTAGRAM_CLIENT_ID, client_secret=INSTAGRAM_CLIENT_SECRET)
api = InstagramAPI(access_token='560816190.ab90928.76d186dd69074303a931540389cdfa84')

# get popular images feed
popular_media = api.media_popular(count=20)

#print(popular_media)
#[Media: 943282867753880642_1564117978, ]

'''
# extract urls of popular images to a list
photolist = []
for media in popular_media:
    photolist.append(media.images['standard_resolution'].url)

print('Top photos from Instagram')
html = ''

for p in photolist:
    html = html + '<img src=' + p + ' width="150" />'

from IPython.core.display import HTML
HTML(html)

print(photolist)
print(html)
'''

print(api.user(560816190)) # User: slalomtokyodrift

slalomtokyodrift = api.user(560816190)

print(slalomtokyodrift)
type(slalomtokyodrift)

userfeed = api.user_media_feed()
#print(api.user_media_feed())
'''
([Media: 943792603680955088_177410725, Media: 943784011489945691_11830841, Media: 943782190417903538_5773262, Media: 943775704302409102_571726460, Media: 943764376376221251_560816190, Media: 943751880354234522_12646983, Media: 943747892504593683_22449256, Media: 943744146039769036_12320896, Media: 943738998089254600_5359800, Media: 943724709361145448_359208764, Media: 943723746810735968_53034170, Media: 943723268011379027_1671457, Media: 943711188038248285_297381336, Media: 943710367290097434_28902942, Media: 943706536227806490_560816190, Media: 943672365075988614_38828391, Media: 943670572578776882_11295776, Media: 943669159621975224_252714246, Media: 943659954147612651_359208764, Media: 943656341634066784_26847345], 'https://api.instagram.com/v1/users/self/feed?access_token=560816190.ab90928.76d186dd69074303a931540389cdfa84&max_id=943656341634066784_26847345')
'''

#print(userfeed)
a = userfeed[0]
b = userfeed[1]
print(a)
print("I'm a fuckup \n \n \n")
print(b)
print(type(a))
