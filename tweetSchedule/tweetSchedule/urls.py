from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from rest_framework import routers
from schedule import views as sviews

router = routers.DefaultRouter()
router.register( "actions", sviews.ActionViewSet )

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tweetSchedule.views.home', name='home'),
    # url(r'^tweetSchedule/', include('tweetSchedule.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'', include('social_auth.urls')),
    url( r'^$', 'scheduleDisplay.views.index' ),
    url( r'^about/', 'scheduleDisplay.views.about' ),
    url( r'^map/', 'scheduleDisplay.views.map' ),
    url(r'^api/', include( router.urls ) ),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
