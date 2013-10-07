from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from website import views

urlpatterns = patterns('',
	# url(r'^$', views.news, name='news'),
)