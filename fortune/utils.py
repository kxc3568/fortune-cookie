import twitter
from datetime import datetime
from fortune_cookie.settings import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET

api = twitter.Api(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
		access_token_key=ACCESS_TOKEN, access_token_secret=ACCESS_SECRET, tweet_mode='extended')

def getTimeline(name):
	statuses = api.GetUserTimeline(screen_name=name)

	text = ''
	if len(statuses)<10:
		r = len(statuses)
	else:
		r = 10
	for i in range(0,r):
		if statuses[i].retweeted_status is not None:
			text += str(statuses[i].retweeted_status.full_text) + " "
		else:
			text += str(statuses[i].full_text) + " "
	return text.rstrip()

	# text = ''
	# stop = 0

	# tstring = statuses[0].created_at[4:19] + statuses[0].created_at[25:]
	# dt = datetime.strptime(tstring, '%b %d %H:%M:%S %Y')

	# if len(statuses>10):
	# 	r = 10
	# else: 
	# 	r = len(statuses)
	# for i in range(1,r):
	# 	tstring = statuses[i].created_at[4:19] + statuses[i].created_at[25:]
	# 	delta = dt-dt.strptime(tstring, '%b %d %H:%M:%S %Y')
	# 	if delta.total_seconds()>24*60*60:
	# 		stop = i
	# 		i+=r
	
	# for i in range(0,stop):
	# 	if statuses[i].retweeted_status is not None:
	# 		text += str(statuses[i].retweeted_status.full_text) + " "
	# 	else:
	# 		text += str(statuses[i].full_text) + " "
	# return text.rstrip()