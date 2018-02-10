
from twitter_api import TwitterAPI
t = TwitterAPI()
t.set_query("cadiz", "36.528580","-6.213026", "5")
j = t.get_json()
print j
