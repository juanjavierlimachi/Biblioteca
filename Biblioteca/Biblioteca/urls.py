from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings#importtamos el setting
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Biblioteca.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',#este para optener las images de todos los uatores
    	{'document_root': settings.MEDIA_ROOT, } ),
    #las urls de mi aplicacion inicio
    url(r'^',include('Biblioteca.apps.inicio.urls')),
    #Autores
    url(r'^',include('Biblioteca.apps.autores.urls')),
    #de libros
     url(r'^',include('Biblioteca.apps.libro.urls')),
    #Estudiantes
    url(r'^',include('Biblioteca.apps.estudiantes.urls')),
)
