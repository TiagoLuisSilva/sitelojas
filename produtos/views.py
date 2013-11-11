from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from models import Produtos
from forms import ProdutosForms


class ProdutosList(ListView, request):
    
    produtos_list = Produtos.objects.all()
    paginator = Paginator(produtos_list, 5)   
    page = request.GET.get('page')
    try:
        produtos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        produtos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        produtos = paginator.page(paginator.num_pages)


    model = produtos

 
class ProdutoCreate(CreateView):
    form_class = ProdutosForms 
    model = Produtos  
    success_url = reverse_lazy('produtos_list')

class ProdutoUpdate(UpdateView):
    form_class = ProdutosForms 
    model = Produtos 
    success_url = reverse_lazy('produtos_list')

class ProdutoDelete(DeleteView):
    model = Produtos 
    success_url = reverse_lazy('produtos_list')

    