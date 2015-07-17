from django.conf.urls import patterns, include, url

from .views import *

urlpatterns = patterns('',

	url(r'^autores/$',RgistrarAutor.as_view(), name="registrar_autor"),
	url(r'^reportar/$',reportarAutor.as_view(), name="reportar_autor"),
)
