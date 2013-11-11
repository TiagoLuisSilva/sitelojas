from django.forms import ModelForm

from models import Produtos
class ProdutosForms(ModelForm):	
   # codigo_interno = ModelForm.CharField(max_length=100) 
   # descricao = ModelForm.CharField(max_length=100) 
  #  valor = ModelForm.DecimalField(max_digits=10, decimal_places=2) 
    class Meta:
        model = Produtos 
        fields = ['codigo_interno', 'descricao', 'valor']