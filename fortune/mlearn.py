#encoding: utf-8
import json
import os
from os.path import join, dirname
from watson_developer_cloud import ToneAnalyzerV3
#encoding: utf-8

tone_analyzer = ToneAnalyzerV3(
    username='13f686ae-28d7-41e7-bef3-08b4120f7160',
    password='dTxwOTgWtT0O',
    version='2016-05-19')

#insert tweet here
tweet = "I am sad"

#anger, disgust, fear, joy, sadness

#initialize fortunes and vector 'em' in a dictionary
fortunes = ["Always love", "I want to die"]
fortunevals = {}

for f in fortunes:
  fortune = tone_analyzer.tone(f, tones='emotion',
    content_type='text/plain')
  for emotions in fortune["document_tone"]["tone_categories"][0]["tones"]:
    fortunevals.setdefault(f,[]).append(emotions["score"])

#print(fortunevals)

#analyse the tweet and shit lmao haha
tone = tone_analyzer.tone(tweet, tones='emotion',
    content_type='text/plain')

s = ""
tweets={}
for emotions in tone["document_tone"]["tone_categories"][0]["tones"]:
  tweets.setdefault(tweet,[]).append(emotions["score"])

#print(tweets)

#find fortune match
bestfortunes = {}

for f in fortunevals:
  sum = 0;
  for i in range(len(fortunevals[f])):
    sum+=abs(tweets[tweet][i]-fortunevals[f][i])
  bestfortunes[f]=sum

finalfortune = (max(bestfortunes.keys(), key=(lambda k: bestfortunes[k])))

#print(finalfortune)