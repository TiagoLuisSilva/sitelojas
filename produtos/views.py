from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.decorators import login_required

from models import Produtos
from forms import ProdutosForms

from django.utils.decorators import method_decorator

class LoginRequiredMixin(object):
    def __init__(self, request, *args, **kwargs):
        self.as_super = super(LoginRequiredMixin, self)
        self.as_super.__init__(request, *args, **kwargs)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return self.as_super.dispatch(self, *args, **kwargs)

class ProdutosList(LoginRequiredMixin, ListView):
    model = Produtos
  
class ProdutoCreate(LoginRequiredMixin, CreateView):
    form_class = ProdutosForms 
    model = Produtos  
    success_url = reverse_lazy('produtos_list')
  
class ProdutoUpdate(LoginRequiredMixin, UpdateView):
    form_class = ProdutosForms 
    model = Produtos 
    success_url = reverse_lazy('produtos_list')
 
def ProdutoDelete(request):
    if request.method=='POST':
       id_prod =  request.POST.get("id_prod")  
       produto = get_object_or_404(Produtos, pk=id_prod)    
       produto.delete()

    return redirect('produtos_list')

class LoginRequiredMixin(object):
    def as_view(cls):
        return login_required(super(LoginRequiredMixin, cls).as_view())
