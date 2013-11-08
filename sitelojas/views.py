from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
def login(request):
    return render_to_response('login.html',{}, context_instance=RequestContext(request))
def index(request):    

    return render_to_response('index.html',{}, context_instance=RequestContext(request))