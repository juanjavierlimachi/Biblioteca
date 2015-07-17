from django.conf.urls import patterns, include, url

from .views import *

urlpatterns = patterns('',
	url(r'^buscar/$',buscarView.as_view(), name='buscar'),
	url(r'^busqueda/$',busquedaView.as_view(), name='buscarView'),
	url(r'^RegistrarLibro/$',RegistrarLibro.as_view(), name='RegistrarLibro'),
	#este la url para pa peticion ajx
	url(r'^busqueda_ajax/$',busquedaAjaxView.as_view(), name='buscarView'),

)
