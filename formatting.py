import pandas as pd
from pandas import DataFrame
import pandas.io.data

def doFormatting(filename):
	features = pd.read_csv('Normalized.csv')
	file1 = open('Formatted.txt', 'w')
	for i in range(0, len(features)):
		file1.write(str(features['label'][i]) + " qid:1" + " 1:"+str(features['followers_count'][i]) + " 2:"+str(features['friends_count'][i]) + " 3:"+str(features['statuses_count'][i]) + " 4:"+str(features['mentions_count'][i]) + " 5:"+str(features['retweet_count'][i]) + " 6:"+str(features['favorite_count'][i]) + " 7:"+str(features['hashtag_count'][i]) + " 8:"+str(features['url_count'][i]) + " 9:"+str(features['verified'][i]) + " 10:"+str(features['location'][i]) + "\n")
	file1.close()