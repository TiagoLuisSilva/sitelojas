from django.db import models
from django_thumbs.db.models import ImageWithThumbsField
class Produtos(models.Model):
      codigo_interno = models.CharField(max_length=30)
      descricao = models.CharField(max_length=30)
      slug = models.SlugField(max_length = 100, blank = True, unique = True)
      valor = models.DecimalField(max_digits=10, decimal_places=2)

      def unicode(self):
         return self.descricao

      def get_absolute_url(self):
         return reverse('album', kwargs={'slug': self.slug})

#class Fotos(models.Model):
#      produto =  models.ForeignKey('Produtos')
#      titulo = models.CharField(u'Titulo', max_length = 100)
#      slug = models.SlugField(max_length = 100, blank = True, unique = True)
#      descricao = models.TextField(blank = True)
#      original = ImageWithThumbsField(
#        null = True,
#        blank = True, 
#        upload_to='galeria/original',
#        # Tamanhos das imagens que a galeria aceita
#        sizes=((125,125),(200,200),(500,500))
#        )
#       thumbnail = models.ImageField(
#            null=True,
#            blank=True,
#            upload_to='galeria/thumbnail',
#            )

#    def __unicode__(self):
#        return self.titulo

#   def get_absolute_url(self):
#        #return reverse('album', kwargs={'slug': self.slug})
#        return self.original

#    def get_exibicao(self):
#        nome_arq = str(self.original)
#        delimiter = nome_arq.find(".JPG")
#        # Exibicao da Imagem em 500x500
#        nome_arq = nome_arq[:delimiter] + ".500x500.jpg"
#        return nome_arq
#    def get_thumbnail(self):
#        nome_arq = str(self.original)
#        delimiter = nome_arq.find(".JPG")        
#        # Exibicao da Imagem em na miniatura em 125x125
#        nome_arq = nome_arq[:delimiter] + ".125x125.jpg"
#        return nome_arq






