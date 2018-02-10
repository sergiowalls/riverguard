import requests

class TwitterAPI:
    #API_URL = "https://api.twitter.com/1.1"
    #params = "/search/tweets.json?oauth_consumer_key=h5csBXeGpJmLma9IgnoV3JWfn&oauth_token=223212203-5n4o9eTcRmKaxoPxtAelhufNzkdOTCSjn1dpku6U&oauth_signature_method=HMAC-SHA1&oauth_timestamp=1518282682&oauth_nonce=u3TGDi&oauth_version=1.0&oauth_signature=kU0fH6vah556kooOwAcytUvJaUI%3D"
    URL = "https://api.twitter.com/1.1/search/tweets.json?oauth_consumer_key=h5csBXeGpJmLma9IgnoV3JWfn&oauth_token=223212203-5n4o9eTcRmKaxoPxtAelhufNzkdOTCSjn1dpku6U&oauth_signature_method=HMAC-SHA1&oauth_timestamp=1518282682&oauth_nonce=u3TGDi&oauth_version=1.0&oauth_signature=kU0fH6vah556kooOwAcytUvJaUI%3D"
    #URL = "https://api.twitter.com/1.1/search/tweets.json?oauth_consumer_key=h5csBXeGpJmLma9IgnoV3JWfn&oauth_token=223212203-5n4o9eTcRmKaxoPxtAelhufNzkdOTCSjn1dpku6U&oauth_signature_method=HMAC-SHA1&oauth_timestamp=1518288807&oauth_nonce=ELcqJ5&oauth_version=1.0&oauth_signature=2MAscCaicpnOgZMfHjdMpJxMuU4%3D&q=cadiz&geocode=36.528580,-6.213026,5km"

    def set_query(self, text, lat, lon, radius):
        self.text = text
        self.lat = lat
        self.lon = lon
        self.radius = radius
    
    def get_json(self):
        response = requests.get(self.URL + "&q={}&geocode={},{},{}km".format(self.text, self.lat, self.lon,self.radius)) 
        json = response.json()
        return json
