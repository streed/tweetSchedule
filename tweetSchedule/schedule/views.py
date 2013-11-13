# Create your views here.
from .models import Action

import dateutil.parser, pytz
from django.utils import timezone

from social_auth.models import UserSocialAuth
from django.contrib.auth.models import User

from rest_framework import viewsets, status
from rest_framework.decorators import action, link
from rest_framework.response import Response

from .serializers import ActionSerializer
from .tasks import schedule_tweet


class ActionViewSet( viewsets.ModelViewSet ):
	queryset = Action.objects.all()
	serializer_class = ActionSerializer

	@link()
	def schedule_tweet( self, request, pk=None ):
		if( pk ):
			a = Action.objects.filter( id=pk )[0]
			user = User.objects.get( username=a.owner )
			tokens = UserSocialAuth.objects.get(user=user)

			tokens = tokens.tokens

			schedule_tweet.apply_async( ( a.who, a.what, a.where, a.when, tokens, ), eta=a.when )

			return Response({"status": "scheduled"})

		else:
			return Response({"status": "not scheduled"})

