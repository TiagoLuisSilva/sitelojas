# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

def list(request):
    return render_to_response('lista.html',{}, context_instance=RequestContext(request))

def cadastrar(request):
    return render_to_response('novo_produto.html',{}, context_instance=RequestContext(request))

def excluir(request):
    return render_to_response('lista.html',{}, context_instance=RequestContext(request))