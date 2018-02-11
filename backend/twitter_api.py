from twitter import Twitter, OAuth


class TwitterAPI:
    ACCESS_TOKEN = "223212203-5n4o9eTcRmKaxoPxtAelhufNzkdOTCSjn1dpku6U"
    ACCESS_SECRET = "kmqNtVCtlyxJ7tS9U0C4HjfjAtE3Djqb3CDrIhFHEoJQt"
    CONSUMER_KEY = "h5csBXeGpJmLma9IgnoV3JWfn"
    CONSUMER_SECRET = "2OVIV2H7kG1TLaNI7FFZ0Gn6odOda8UuojyVkh8emgRnlxB1wW"
    oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

    def __init__(self):
        # Initiate the connection to Twitter REST API
        self.twitter = Twitter(auth=self.oauth)

    def get_active_tweets(self, text, lat, lon, radius):
        json = self.twitter.search.tweets(q=text, result_type='recent',
                                          geocode="{},{},{}km".format(lat, lon, radius),
                                          count=100)
        return json

    def get_passive_tweets(self, lat, lon, radius):
        json = self.twitter.search.tweets(q='*',
                                          geocode="{},{},{}km".format(lat, lon, radius),
                                          count=100)
        return json

    def extract_image_tweets(self, tweets):
        return [i for i in tweets if ('media' in i['entities'] and i['entities']['media'][0]['type'] == 'photo')]
