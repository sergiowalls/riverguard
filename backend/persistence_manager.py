import time

from flask import logging, jsonify

from VisionAPI import VisionAPI
from persistence import Persistence
from twitter_api import TwitterAPI

RADIUS = "13"

TWEET_TABLE = 'tweets'
CACHE_TIME = 20


class PersistenceManager:
    def __init__(self, path, log):
        self.last_request = time.time() - CACHE_TIME
        self.log = log
        self.twitterAPI = TwitterAPI()
        self.repository = Persistence(path, logging.getLogger(__name__))
        self.repository.init_db()

    def list(self):
        if (time.time() - self.last_request) >= CACHE_TIME:

            t = TwitterAPI()
            active = t.get_active_tweets("#riverguard", "36.528580", "-6.213026", RADIUS)["statuses"]
            passive = t.get_passive_tweets("36.528580", "-6.213026", RADIUS)["statuses"]
            passive = t.extract_image_tweets(passive)[:15]

            v = VisionAPI()
            passive = v.tag_images(passive)
            relevant_tags = ["waste", "algae", "fish", "water"]
            passive = self.filter_non_relevant_tweets(passive, relevant_tags)

            tweets = active + passive

            self.log.info('getting tweets from twitter')
            for tweet in tweets:
                self.repository.create(tweet)
            self.last_request = time.time()
        return self.repository.list()

    def filter_non_relevant_tweets(self, tweets, relevant_tags):
        filtered_tweets = []
        for tweet in tweets:
            tags = [tag["Label"] for tag in tweet["tags"]]
            if set(relevant_tags) & set(tags):
                filtered_tweets.append(tweet)
        return filtered_tweets