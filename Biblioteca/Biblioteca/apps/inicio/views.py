from django.shortcuts import render, render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
# Create your views here.
from django.views.generic import TemplateView, FormView
from .forms import UserForm
from django.core.urlresolvers import reverse_lazy
from .models import Perfiles
class index(TemplateView):
	#template_name='base.html'
	template_name='index.html'
class inicio(TemplateView):
	template_name='base.html'
def Ingreso(request):
	#if not request.user.is_anonymous():
	#	return HttpResponseRedirect('/ingreso/')
	if request.method == 'POST':
		formulario=AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario, password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('/inicio/')
				else:
					return render_to_response('inicio/noactivo.html',context_instance=RequestContext(request))
			else:
				return render_to_response('inicio/nousuario.html',context_instance=RequestContext(request))
	else:
		formulario=AuthenticationForm()
	return render_to_response('inicio/index.html',{'formulario':formulario},context_instance=RequestContext(request))

class registrarse(FormView):
	template_name = 'inicio/nuevousuario.html'
	form_class = UserForm
	success_url = reverse_lazy('registrarse')
	sms=False
	def form_valid(self, form):
		user=form.save()
		perfil = Perfiles()
		perfil.usuario = user
		perfil.telefono = form.cleaned_data['telefono']
		perfil.save()
		sms=True
		return super (registrarse, self).form_valid(form)

@login_required(login_url='/inicio')
def Salir(request):
	logout(request)
	return HttpResponseRedirect('/')