from django.db import models

# Create your models here.

class Tweets( models.Model ):
	author = models.CharField( max_length=144 )
	tweet = models.CharField( max_length=144 )

