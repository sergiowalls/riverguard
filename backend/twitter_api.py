import requests
from twitter import Twitter, OAuth, TwitterHTTPError

class TwitterAPI:
    #API_URL = "https://api.twitter.com/1.1"
    #params = "/search/tweets.json?oauth_consumer_key=h5csBXeGpJmLma9IgnoV3JWfn&oauth_token=223212203-5n4o9eTcRmKaxoPxtAelhufNzkdOTCSjn1dpku6U&oauth_signature_method=HMAC-SHA1&oauth_timestamp=1518282682&oauth_nonce=u3TGDi&oauth_version=1.0&oauth_signature=kU0fH6vah556kooOwAcytUvJaUI%3D"
    #URL = "https://api.twitter.com/1.1/search/tweets.json?oauth_consumer_key=h5csBXeGpJmLma9IgnoV3JWfn&oauth_token=223212203-5n4o9eTcRmKaxoPxtAelhufNzkdOTCSjn1dpku6U&oauth_signature_method=HMAC-SHA1&oauth_timestamp=1518282682&oauth_nonce=u3TGDi&oauth_version=1.0&oauth_signature=kU0fH6vah556kooOwAcytUvJaUI%3D"
    #URL = "https://api.twitter.com/1.1/search/tweets.json?oauth_consumer_key=h5csBXeGpJmLma9IgnoV3JWfn&oauth_token=223212203-5n4o9eTcRmKaxoPxtAelhufNzkdOTCSjn1dpku6U&oauth_signature_method=HMAC-SHA1&oauth_timestamp=1518294265&oauth_nonce=P1q1yL&oauth_version=1.0&oauth_signature=dPCvCypVUZxvJi4YfIjVxU19GWw%3D"

    ACCESS_TOKEN = "223212203-5n4o9eTcRmKaxoPxtAelhufNzkdOTCSjn1dpku6U"
    ACCESS_SECRET = "kmqNtVCtlyxJ7tS9U0C4HjfjAtE3Djqb3CDrIhFHEoJQt"
    CONSUMER_KEY = "h5csBXeGpJmLma9IgnoV3JWfn"
    CONSUMER_SECRET = "2OVIV2H7kG1TLaNI7FFZ0Gn6odOda8UuojyVkh8emgRnlxB1wW"
    oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

    def __init__(self):
        # Initiate the connection to Twitter REST API
        self.twitter = Twitter(auth=self.oauth)

    def set_query(self, text, lat, lon, radius):
        self.text = text
        self.lat = lat
        self.lon = lon
        self.radius = radius

    def get_active_tweets(self):
        json = self.twitter.search.tweets(q='#riverguard', result_type='recent',
                                          geocode="{},{},{}km".format(self.lat, self.lon, self.radius),
                                          count=100)
        print len(json['statuses'])
        return json


    def get_passive_tweets(self):
        json = self.twitter.search.tweets(q='*',
                                          geocode="{},{},{}km".format(self.lat, self.lon, self.radius),
                                          count=100)

        #print json
        print len(json['statuses'])
        #json['statuses'] = [i for i in json['statuses'] if ('media' in i['entities'] and i['entities']['media'][0]['type'] == 'photo')]
        return json

    def extract_image_tweets(self, tweets):
        return [i for i in tweets['statuses'] if ('media' in i['entities'] and i['entities']['media'][0]['type'] == 'photo')]