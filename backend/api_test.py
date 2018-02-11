from VisionAPI import VisionAPI
from twitter_api import TwitterAPI

from flask import jsonify


t = TwitterAPI()
active = t.get_active_tweets("#riverguard", "36.528580", "-6.213026", "5")["statuses"]
print len(active)
passive = t.get_passive_tweets("36.528580", "-6.213026", "5")["statuses"]
print len(passive)
passive = t.extract_image_tweets(passive)[:15]
print len(passive)

v = VisionAPI()
passive = v.tag_images(passive)
print len(passive)

tweets = active + passive
result = jsonify(tweets)
print result