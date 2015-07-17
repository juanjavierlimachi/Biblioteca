from django.conf.urls import patterns, include, url

from .views import *

urlpatterns = patterns('',
	url(r'^reservar/(?P<id>\d+)/$',Reservrlibros),
	url(r'^consultaLibos/$',ConsultaLibros.as_view(), name='ConsultaLibros'),
	url(r'^reservaExitosa/$',MostrarReservas),
	#url(r'^Verreservas/$',Verreservas),
	#url(r'^busqueda_ajax/$',ReservasLibros.as_view(), name='buscarView'), el id lo pasamos en una vista como parametro
)
