from django.conf.urls import patterns, url

from produtos import views

urlpatterns = patterns('',
     url(r'^$', views.ProdutosList.as_view(), name='produtos_list'),
     url(r'^new$', views.ProdutoCreate.as_view(), name='produto_new'),
     url(r'^edit/(?P<pk>\d+)$', views.ProdutoUpdate.as_view(), name='produto_edit'),
     url(r'^delete/(?P<pk>\d+)$', views.ProdutoDelete.as_view(), name='produto_delete'),
)