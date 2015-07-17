from django.conf.urls import patterns, include, url

from .views import *

urlpatterns = patterns('',
	url(r'^Ingreso/$', Ingreso),
	url(r'^registrarse/$',registrarse.as_view(), name='registrarse'),
	url(r'^inicio/$',inicio.as_view()),	
	url(r'^cerrar/$',Salir),
	url(r'^$',index.as_view()),

)
