import time

from flask import logging, jsonify

from VisionAPI import VisionAPI
from persistence import Persistence
from twitter_api import TwitterAPI

TWEET_TABLE = 'tweets'
ONE_MINUTE = 60


class PersistenceManager:
    def __init__(self, path, log):
        self.last_request = time.time() - ONE_MINUTE
        self.log = log
        self.twitterAPI = TwitterAPI()
        self.repository = Persistence(path, logging.getLogger(__name__))
        self.repository.init_db()

    def list(self):
        if (time.time() - self.last_request) >= ONE_MINUTE:

            t = TwitterAPI()
            active = t.get_active_tweets("#riverguard", "36.528580", "-6.213026", "5")["statuses"]
            passive = t.get_passive_tweets("36.528580", "-6.213026", "5")["statuses"]
            passive = t.extract_image_tweets(passive)[:15]

            v = VisionAPI()
            passive = v.tag_images(passive)

            tweets = active + passive

            self.log.info('getting tweets from twitter')
            for tweet in tweets:
                self.repository.create(tweet)
            self.last_request = time.time()
        return self.repository.list()