from django.db import models
from Biblioteca.apps.autores.models import Autor
# Create your models here.
class categorias(models.Model):
	Nombre_Categoria =models.CharField(max_length=50)
	def __unicode__(self):
		return self.Nombre_Categoria
class Libro(models.Model):
	autor = models.ManyToManyField(Autor)
	nombre = models.CharField(max_length=50)
	resumen= models.TextField(max_length=300)
	portadas = models.ImageField(upload_to = 'portadas')
	categoria = models.ForeignKey(categorias)
	def __unicode__(self):
		return self.nombre

	def Traer_url_portadas(self):
		return 'http://localhost:8000/media/%s' % self.portadas