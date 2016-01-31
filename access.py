APP_KEY = 'Xa6dDss4hQAgC2KA5x9jUXIdV'
APP_SECRET = 'Mxq0NGtbEmRtJLucjlRMSedt2rJRxLKSCcAghT3W4O15OEKgsP'
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'

def getToken():
	twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
	ACCESS_TOKEN = twitter.obtain_access_token()
	twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
	print "Access Token Generated!"