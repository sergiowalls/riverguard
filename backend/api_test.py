from flask import jsonify
from twitter_api import TwitterAPI
from VisionAPI import VisionAPI

t = TwitterAPI()
#t.set_query("", "36.528580", "-6.213026", "10")
t.set_query("", "36.691744", "-6.132894", "5")
#t.set_query("", "36.514440", "-6.258283", "5")

#t.set_query("", "37.632080", "-7.321489", "3")
j = t.get_passive_tweets()
p = t.extract_image_tweets(j)
print len(p)

v = VisionAPI()
p2 = v.tag_images(p[:15])

print p2
