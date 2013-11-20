from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf

from produtos.models import Produtos
def login(request):
    return render_to_response('login.html',{}, context_instance=RequestContext(request))

def index(request):    
    
    if request.method=='POST':
       search_key =  request.POST.get("search_key")
       print search_key
       produtos = Produtos.objects.filter(descricao__contains=search_key)
    else:
        produtos = ""

    return render_to_response('index.html',{"produtos" :produtos}, context_instance=RequestContext(request))