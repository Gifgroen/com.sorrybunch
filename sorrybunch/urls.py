from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from website import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sorrybunch.views.home', name='home'),
    # url(r'^sorrybunch/', include('sorrybunch.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url("^$",  views.index),
    url("^photos/$", views.photos),
    url("^contact/$", views.contact),
    url("^booker/$", views.booker),
    url("^video/$", views.video),
    url("^bio/$", views.bio),
    url("^songs/", views.songs),
    url("^news/", views.news),
    url("^gigs/", views.gigs),
)

handler404 = 'website.views.page_not_found'
