#encoding: utf-8
import twitter
from datetime import datetime
from fortune_cookie.settings import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET, USERNAME, PASSWORD
import json
from watson_developer_cloud import ToneAnalyzerV3
from .models import Fortune

api = twitter.Api(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
		access_token_key=ACCESS_TOKEN, access_token_secret=ACCESS_SECRET, tweet_mode='extended')

def getTimeline(name):
	statuses = api.GetUserTimeline(screen_name=name)

	# text = ''
	# if len(statuses)<10:
	# 	r = len(statuses)
	# else:
	# 	r = 10
	# for i in range(0,r):
	# 	if statuses[i].retweeted_status is not None:
	# 		text += str(statuses[i].retweeted_status.full_text) + " "
	# 	else:
	# 		text += str(statuses[i].full_text) + " "
	# return text.rstrip()

	text = ''
	stop = 0

	tstring = statuses[0].created_at[4:19] + statuses[0].created_at[25:]
	dt = datetime.strptime(tstring, '%b %d %H:%M:%S %Y')

	if len(statuses)>10:
		r = 10
	else: 
		r = len(statuses)
	for i in range(1,r):
		tstring = statuses[i].created_at[4:19] + statuses[i].created_at[25:]
		delta = dt-dt.strptime(tstring, '%b %d %H:%M:%S %Y')
		if delta.total_seconds()>24*60*60:
			stop = i
			i+=r
	
	for i in range(0,stop):
		if statuses[i].retweeted_status is not None:
			text += str(statuses[i].retweeted_status.full_text) + " "
		else:
			text += str(statuses[i].full_text) + " "
	return text.rstrip()

def getFortune(name):
	tone_analyzer = ToneAnalyzerV3(
    username=USERNAME,
    password=PASSWORD,
    version='2016-05-19')

	#insert tweet here
	tweet = getTimeline(name)

	#populated
	#populate_db()

	#analyze the tweet
	tone = tone_analyzer.tone(tweet, tones='emotion', content_type='text/plain')

	s = ""
	tweets = {}
	for emotions in tone["document_tone"]["tone_categories"][0]["tones"]:
		tweets.setdefault(tweet,[]).append(emotions["score"])

	#find fortune match
	bestfortunes = {}

	queryset = Fortune.objects.all()
	for q in queryset:
		sum = 0
		for i in range(5):
			q1 = q.emotions
			stringlist = q1[q1.index('[')+1:q1.index(']')]
			vals = stringlist.split(', ')
			vals = [float(v) for v in vals]
			sum+=abs(tweets[tweet][i]-vals[i])
		bestfortunes[q.message] = sum

	# for f in fortunevals:
	# 	sum = 0
	# 	for i in range(5):
	# 		sum += abs(tweets[tweet][i]-fortunevals[f][i]) #error
	# 	bestfortunes[f] = sum

	finalfortune = (max(bestfortunes.keys(), key=(lambda k: bestfortunes[k])))
	return finalfortune

def populate_db():
	tone_analyzer = ToneAnalyzerV3(
    username=USERNAME,
    password=PASSWORD,
    version='2016-05-19')
	#anger, disgust, fear, joy, sadness
	file = open("fortune/fortunes.txt","r")
	#initialize fortunes and vector 'em' in a dictionary
	fortunes = file.readlines()

	for f in fortunes:
		fortune = tone_analyzer.tone(f, tones='emotion', content_type='text/plain')
		fortunevals = {}
		for emotions in fortune["document_tone"]["tone_categories"][0]["tones"]:
			fortunevals.setdefault(f,[]).append(emotions["score"])
		model = Fortune.objects.create()
		model.message = f
		model.emotions = fortunevals
		model.save()