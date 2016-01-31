import pandas as pd
from pandas import DataFrame
import pandas.io.data
import twython
from twython import Twython

APP_KEY = ''
APP_SECRET = ''
ACCESS_TOKEN = ''

d = {'id':'', 'created_at':'', 'from_user':'', 'followers_count':'', 'friends_count':'', 'statuses_count':'', 'verified':'', 'location':'', 'text':'', 'retweet_count':'', 'favorite_count':'', 'hashtag_count':'', 'url_count':'', 'mentions_count':'', 'links':''}

def getFeatures(filename):
	csvfile = pd.read_csv(filename) #Reading the .csv files containing tweets.
	tweet_ids = csvfile['id_str']	#Copying the 'id_str' attribute values to a item.
	length = len(tweet_ids)			#Getting the length of 'tweet_ids'.
	
	df = DataFrame(d, index=[0])	#Creating a DataFrame

	twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
	ACCESS_TOKEN = twitter.obtain_access_token()
	twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
	#Generating Access Token

	for i in range(0, length):
		status = twitter.show_status(id=tweet_ids[i])
		d['id'] = status['id_str'].encode('utf-8')
		d['created_at'] = status['created_at'].encode('utf-8')
		d['from_user'] = status['user']['screen_name'].encode('utf-8')
		d['followers_count'] = status['user']['followers_count']
		d['friends_count'] = status['user']['friends_count']
		d['statuses_count'] = status['user']['statuses_count']
		d['verified'] = status['user']['verified']
		d['location'] = 0 if (len(status['user']['location'].encode('utf-8'))==0) else 1
		d['text'] = status['text'].encode('utf-8')
		d['retweet_count'] = status['retweet_count']
		d['favorite_count'] = status['favorite_count']
		d['hashtag_count'] = len(status['entities']['hashtags'])
		d['url_count'] = len(status['entities']['urls'])
		d['mentions_count'] = len(status['entities']['user_mentions'])
		if(len(status['entities']['urls'])>0):
    			for x in range(0, len(status['entities']['urls'])):
       				d['links'] += status['entities']['urls'][x]['expanded_url'].encode('utf-8') + "  "
		df = df.append(d, ignore_index=True)
		df.to_csv('NSamples.csv') #Saving file to disk
		d['links'] = ''
	print "\nAll Done!"