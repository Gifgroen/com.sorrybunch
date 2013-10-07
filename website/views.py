# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader

from django.shortcuts import render_to_response

from website.models import Article, Gig, Video, Audio, Bio

def index(request):
	return render_to_response('home.html', '', {})
	
def photos(request):
	return render_to_response('photos.html', '', {})
	
def contact(request):
	return render_to_response('contact.html', '', {})
		
def booker(request):
	return render_to_response('booker.html', '', {})
		
def video(request):
	videos = Video.objects.filter(active = True)
	template = loader.get_template('video.html')
	context = Context({
		'videos': videos,
	})
	return HttpResponse(template.render(context))

def bio(request):
	bios = Bio.objects.all()
	template = loader.get_template('bio.html')
	context = Context({
		'bios': bios,
	})
	return HttpResponse(template.render(context))

def songs(request):
	song = Audio.objects.filter(active = True)
	template = loader.get_template('songs.html')
	context = Context({
		'song': song,
	})
	return HttpResponse(template.render(context))
	
def news(request):
	latest_news_list = Article.objects.order_by('-placed')[:1]
	template = loader.get_template('news.html')
	context = Context({
		'latest_news_list': latest_news_list,
	})
	return HttpResponse(template.render(context))

def gigs(request):
	print " Rendering! "
	gigs_list = Gig.objects.order_by('-date')
	template = loader.get_template('gigs.html')
	context = Context({
		'gigs_list': gigs_list,
	})
	return HttpResponse(template.render(context))
	
def page_not_found(request):
	return render_to_response('404.html', '', {})