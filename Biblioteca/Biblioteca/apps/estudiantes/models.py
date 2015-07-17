from django.db import models
from Biblioteca.apps.libro.models import Libro
# Create your models here. from Biblioteca.apps.autores.models import Autor
class Estudiante(models.Model):
	nombre = models.CharField(max_length=50)
	establecimiento = models.CharField(max_length=30)
	ci = models.IntegerField()
	Libro = models.ForeignKey(Libro)
	def __unicode__(self):
		return self.nombre