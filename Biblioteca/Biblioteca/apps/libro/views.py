from django.shortcuts import render
from django.views.generic import TemplateView, ListView,CreateView
from django.core.urlresolvers import reverse_lazy
from .models import Libro
from Biblioteca.apps.autores.models import Autor
# Create your views here.
class buscarView(TemplateView):
	#template_name = 'libros/buscar.html'

	def post(self, request, *args, **kwargs):
		buscar = request.POST['buscalo']
		libros = Libro.objects.filter(nombre__contains=buscar)
		if libros:
			datos=[]
			for libro in libros:
				autores =libro.autor.all()
				datos.append(dict([(libro,autores)]))
		
			return render(request, 'libros/buscar.html',
						{'datos':datos})
		else:
			autores=Autor.objects.filter(nombre__contains=buscar)
			return render(request, 'libros/buscar.html',
						{'autores':autores,'autor':True})

class busquedaView(ListView):
	model =Autor
	template_name = 'libros/busqueda.html'
	context_object_name = 'autores'

from django.core import serializers
from django.http import HttpResponse
class busquedaAjaxView(TemplateView):
	def get(self, request, *args, **kwargs):
		id_autor = request.GET['id']
		libros = Libro.objects.filter(autor__id=id_autor)
		#print libros
		data = serializers.serialize('json', libros,fields=('nombre','resumen'))
		return HttpResponse(data, mimetype='application/json')
class RegistrarLibro(CreateView):
	template_name = 'libros/RegistrarLibro.html'
	model=Libro
	success_url = reverse_lazy('consultaLibos')