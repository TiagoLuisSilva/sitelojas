# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Produtos

def lista(request):
    produtos = Produtos.objects.all()
    return render_to_response('lista.html',{"produtos" : produtos}, context_instance=RequestContext(request))

def cadastrar(request):
    return render_to_response('novo_produto.html',{}, context_instance=RequestContext(request))

def excluir(request):
    return render_to_response('lista.html',{}, context_instance=RequestContext(request))