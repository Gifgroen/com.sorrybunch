# Create your views here.
from django.shortcuts import render_to_response

def index(request):
	return render_to_response('home.html', '', {})
	
def photos(request):
	return render_to_response('photos.html', '', {})
	
def contact(request):
	return render_to_response('contact.html', '', {})
		
def booker(request):
	return render_to_response('booker.html', '', {})
		
def video(request):
	return render_to_response('video.html', '', {})

def bio(request):
	return render_to_response('bio.html', '', {})

def songs(request):
	return render_to_response('songs.html', '', {})
	
def news(request):
	return render_to_response('news.html', '', {})

def gigs(request):
	return render_to_response('gigs.html', '', {})
	
def page_not_found(request):
	return render_to_response('404.html', '', {})