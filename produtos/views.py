from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.decorators import login_required

from models import Produtos
from forms import ProdutosForms

@login_required
class ProdutosList(ListView):
    model = Produtos
 
@login_required
class ProdutoCreate(CreateView):
    form_class = ProdutosForms 
    model = Produtos  
    success_url = reverse_lazy('produtos_list')

@login_required
class ProdutoUpdate(UpdateView):
    form_class = ProdutosForms 
    model = Produtos 
    success_url = reverse_lazy('produtos_list')

@login_required
def ProdutoDelete(request):
    if request.method=='POST':
       id_prod =  request.POST.get("id_prod")  
       produto = get_object_or_404(Produtos, pk=id_prod)    
       produto.delete()

    return redirect('produtos_list')
