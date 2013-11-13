import pyparsing as pp
"""
	#remindly #when tomorrow #where mc donalds #who @test #what meet for lunch
"""

Sentence = pp.Group( pp.OneOrMore( pp.Word( pp.alphanums + "`~!@$%^&*()_+-=[]{};\"':,.<>/?" ) ) )
Sentence.setParseAction( lambda s, l, t: " ".join( t[0] ) )
Who = pp.Keyword( "#who" ) + Sentence
Who.setParseAction( lambda s, l, t: { "who": t[1] } )
What = pp.Keyword( "#what" ) + Sentence
What.setParseAction( lambda s, l, t: { "what": t[1] } )
When = pp.Keyword( "#when" ) + Sentence
When.setParseAction( lambda s, l, t: { "when": t[1] } )
Where = pp.Keyword( "#where" ) + Sentence
Where.setParseAction( lambda s, l, t: { "where": t[1] } )
HashTagParam = pp.Or( [ Who, What, Where, When ] )
Remindly = pp.Keyword( "#remindly" ).suppress()
TweetParser = Remindly + pp.OneOrMore( HashTagParam )
TweetParser.setParseAction( lambda s, l, t: { "tweet": dict( ( k, v ) for d in t for( k, v ) in d.items() ) } )

