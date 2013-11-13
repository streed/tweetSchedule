from tweetSchedule.celery import app
from django.conf import settings

import tweepy


@app.task()
def send_tweet( who, what, where, when, token ):

	auth = tweepy.OAuthHandler( settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET )
	auth.set_access_token( token["oauth_token"], token["oauth_token_secret"] )
	api = tweepy.API( auth )

	who = [ "@%s" % i for i in who.split( " " ) ]
	who = ",".join( who )
	s = "#who %s #what %s #where %s"  % ( who, what, where )

	api.update_status( s )

@app.task
def schedule_tweet( who, what, where, when, tokens ):
	"""This will send the tweet"""

	send_tweet( who, what, where, when, tokens )
