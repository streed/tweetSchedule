# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from schedule.models import Action


def index( request ):
	actions = Action.objects.all().order_by( '-when' )[:50]

	actions = [ a.toString() for a in actions ]

	template = loader.get_template( 'display/index.html' )

	context = Context({
		'actions': actions 
	})

	return HttpResponse(template.render(context))

def about( request ):
	actions = Action.objects.all().order_by( '-when' )[:50]

	actions = [ a.toString() for a in actions ]

	template = loader.get_template( 'display/about.html' )

	context = Context({
		'actions': actions 
	})

	return HttpResponse(template.render(context))

def map( request ):
	actions = Action.objects.all().order_by( '-when' )[:50]

	actions = [ a.toString() for a in actions ]

	template = loader.get_template( 'display/map.html' )

	context = Context({
		'actions': actions 
	})

	return HttpResponse(template.render(context))
