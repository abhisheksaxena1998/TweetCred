import pandas as pd
from pandas import DataFrame
import pandas.io.data

def normalizeFeatures(filename):
	features = pd.read_csv(filename)
	normalized = pd.read_csv(filename)
	features.mean()
	features.std()
	normalized['favorite_count'] = (features['favorite_count'] - features.mean()[0])/features.std()[0]
	normalized['followers_count'] = (features['followers_count'] - features.mean()[1])/features.std()[1]
	normalized['friends_count'] = (features['friends_count'] - features.mean()[1])/features.std()[1]
	normalized['statuses_count'] = (features['statuses_count'] - features.mean()[2])/features.std()[2]
	normalized['retweet_count'] = (features['retweet_count'] - features.mean()[4])/features.std()[4]
	normalized['Fr_Fo_Ratio'] = (features['Fr_Fo_Ratio'] - features.mean()[10])/features.std()[10]
	normalized['St_Fo_Ratio'] = (features['Fr_Fo_Ratio'] - features.mean()[11])/features.std()[11]
	normalized.to_csv('MoreNormalized.csv')
