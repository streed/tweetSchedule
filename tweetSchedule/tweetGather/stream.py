from tweepy import OAuthHandler, StreamListener, Stream as TweepyStream

import os
import json
import shlex
import ConfigParser as configparser

from requests import post, get

from tweet_parser import TweetParser
from datetime import datetime, timedelta

def parseWhen( s ):
	if( s == "tomorrow" ):
		return str( datetime.now() + timedelta( days=1 ) )
	elif( "in" in s ):
		parts = s.split( " " )

		num = int( parts[1] )

		param = { parts[2]: num }

		return str( datetime.now() + timedelta( **param ) )


class StreamerListener( StreamListener ):

	def on_status( self, tweet ):
		t = TweetParser.parseString( tweet.text )[0]
		t = t["tweet"]

		data = {}

		if( "who" in t ):
			data["who"] = t["who"]
		else:
			data["who"] = tweet.author.screen_name

		if( "when" in t ):
			data["when"] = parseWhen( t["when"] )
		else:
			data["when"] = str( datetime.now() + timedelta( minutes=5 ) )

		if( "where" in t ):
			data["where"] = t["where"]
		else:
			data["where"] = "Where you are."

		if( "what" in t ):
			data["what"] = t["what"]
		else:
			data["what"] = ""

		data["owner"] = tweet.author.screen_name

		headers = {}

		headers["Content-type"] = 'application/json; charset=utf8'

		res = post( "http://localhost:8000/api/actions/", data=json.dumps( data ), headers=headers )

		print( res.text )

		res = res.json()

		if( "id" in res ):
			get( "http://localhost:8000/api/actions/%d/schedule_tweet" % res["id"] )

		print( res )

	def on_error( self, code ):
		print "Error:", code


def make_api(consumer=None, consumer_secret=None, token=None, secret=None):

	if consumer == None or consumer_secret == None or token == None or secret == None:
		config = configparser.ConfigParser()
		config.readfp( open( os.path.expanduser( "~/.remindlyTwitter" ) ) )

		consumer = config.get( "twitter", "consumer" )
		consumer_secret = config.get( "twitter", "consumer_secret" )
		token = config.get( "twitter", "token" )
		secret = config.get( "twitter", "secret" )

	auth = OAuthHandler( consumer, consumer_secret )
	auth.set_access_token( token, secret )

	return tweepy.API( auth )


class Streamer( object ):

	def __init__( self, queue, terms=[], consumer=None, consumer_secret=None,
			token=None, secret=None):

		if consumer == None or consumer_secret == None or token == None or secret == None:
			config = configparser.ConfigParser()
			config.readfp( open( os.path.expanduser( "~/.slackTwitter" ) ) )

			consumer = config.get( "twitter", "consumer" )
			consumer_secret = config.get( "twitter", "consumer_secret" )
			token = config.get( "twitter", "token" )
			secret = config.get( "twitter", "secret" )

		auth = OAuthHandler( consumer, consumer_secret )
		auth.set_access_token( token, secret )

		listener = StreamerListener()
		self.stream = TweepyStream( auth=auth, listener=listener )

		self._queue = queue
		self._terms = terms
	
	def start( self ):
		self.stream.filter( track=self._terms )

