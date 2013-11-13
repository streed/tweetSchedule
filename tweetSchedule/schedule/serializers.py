from .models import Action
from rest_framework import serializers

class ActionSerializer( serializers.HyperlinkedModelSerializer ):
	class Meta:
		model = Action
		fields = ( "id", "owner", "who", "what", "where", "when", )
