# Create your views here.
from django.shortcuts import render_to_response

def news(request):
    return render_to_response('news.html', '', {})

def gigs(request):
    return render_to_response('gigs.html', '', {})