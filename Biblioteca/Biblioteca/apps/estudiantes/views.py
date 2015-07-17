from django.shortcuts import render, render_to_response
from django.views.generic import CreateView,TemplateView,ListView
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .formularios import *
from Biblioteca.apps.libro.models import Libro
# Create your views here.
def Reservrlibros(request,id):
	id_libro=id
	if request.method=='POST':
		form=reservaForm(request.POST)
		if form.is_valid():
			estu=Estudiante()
			estu.nombre=request.POST['nombre']
			estu.establecimiento=request.POST['establecimiento']
			estu.ci=request.POST['ci']
			estu.Libro_id=id_libro
			estu.save()
			return HttpResponseRedirect('/reservaExitosa/')
	else:
		form=reservaForm()
	return render_to_response('libros/reservas.html',{'form':form},context_instance=RequestContext(request))

def MostrarReservas(request):
 	reservas=Estudiante.objects.all()
 	libros=Libro.objects.all()
 	return render_to_response('estudiantes/MostrarReservas.html',{'reservas':reservas,'libros':libros},context_instance=RequestContext(request))

class ConsultaLibros(ListView):
	template_name='estudiantes/ConsultaLibros.html'
	model = Libro
	context_object_name = 'libros'

