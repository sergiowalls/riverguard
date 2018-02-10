import requests

class TwitterAPI:
    #API_URL = "https://api.twitter.com/1.1"
    #params = "/search/tweets.json?oauth_consumer_key=h5csBXeGpJmLma9IgnoV3JWfn&oauth_token=223212203-5n4o9eTcRmKaxoPxtAelhufNzkdOTCSjn1dpku6U&oauth_signature_method=HMAC-SHA1&oauth_timestamp=1518282682&oauth_nonce=u3TGDi&oauth_version=1.0&oauth_signature=kU0fH6vah556kooOwAcytUvJaUI%3D"
    #URL = "https://api.twitter.com/1.1/search/tweets.json?oauth_consumer_key=h5csBXeGpJmLma9IgnoV3JWfn&oauth_token=223212203-5n4o9eTcRmKaxoPxtAelhufNzkdOTCSjn1dpku6U&oauth_signature_method=HMAC-SHA1&oauth_timestamp=1518282682&oauth_nonce=u3TGDi&oauth_version=1.0&oauth_signature=kU0fH6vah556kooOwAcytUvJaUI%3D"
    URL = "https://api.twitter.com/1.1/search/tweets.json?oauth_consumer_key=h5csBXeGpJmLma9IgnoV3JWfn&oauth_token=223212203-5n4o9eTcRmKaxoPxtAelhufNzkdOTCSjn1dpku6U&oauth_signature_method=HMAC-SHA1&oauth_timestamp=1518294265&oauth_nonce=P1q1yL&oauth_version=1.0&oauth_signature=dPCvCypVUZxvJi4YfIjVxU19GWw%3D"

    def set_query(self, text, lat, lon, radius):
        self.text = text
        self.lat = lat
        self.lon = lon
        self.radius = radius
    
    def get_json(self):
        response = requests.get(self.URL + "&q={}&geocode={},{},{}km&count=100".format(self.text, self.lat, self.lon,self.radius))
        json = response.json()
        #print len(json['statuses'])
        json['statuses'] = [i for i in json['statuses'] if(i['geo'])]
        #print len(json['statuses'])
        return json
