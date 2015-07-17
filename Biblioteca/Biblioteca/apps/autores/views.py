from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,ListView
from Biblioteca.apps.autores.models import *
from django.core.urlresolvers import reverse_lazy
# Create your views here.
class RgistrarAutor(CreateView):
	template_name = 'autores/registroAutor.html'
	model = Autor
	success_url = reverse_lazy('reportar_autor')
class reportarAutor(ListView):
	template_name='autores/reportarAutor.html'
	model=Autor#aki retornamos todos los autores de mi table autor
	context_object_name = 'autores'#es una lista para recorrer los autores en em html
#me quede en el video 7 jejeej
