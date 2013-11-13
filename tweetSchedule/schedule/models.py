from django.db import models

import pretty

# Create your models here.
class Action( models.Model ):
	owner = models.CharField( max_length=144 )
	who = models.CharField( max_length=144 )
	what = models.CharField( max_length=144 )
	where = models.CharField( max_length=144 )
	when = models.DateTimeField()


	def __str__( self ):
		return "<Action( %s, %s, %s, %s )>" % ( self.who, self.who, self.when, self.where )

	def toString( self ):
		who = [ "@%s" % i for i in self.who.split( " " ) ]
		who = ",".join( who )
		when = self.when.replace(tzinfo=None)
		s = "#who %s #what %s #where %s #when %s"  % ( who, self.what, self.where, pretty.date( when ) )

		return s
