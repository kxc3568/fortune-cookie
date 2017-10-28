import twitter
from fortune_cookie.settings import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET

api = twitter.Api(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
		access_token_key=ACCESS_TOKEN, access_token_secret=ACCESS_SECRET, tweet_mode='extended')

def getTimeline(name):
	statuses = api.GetUserTimeline(screen_name=name)
	text = []
	for i in range(0,10):
		if statuses[i].retweeted_status is not None:
			text.append(statuses[i].retweeted_status.full_text.encode('utf-8'))
		else:
			text.append(statuses[i].full_text.encode('utf-8'))
	return text