# Create your views here.
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('home.html', '', {})

def page_not_found(request):
    return render_to_response('404.html', '', {})