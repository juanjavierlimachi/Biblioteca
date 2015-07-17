from django.contrib import admin
from .models import *
# Register your models here.

class LibroAdmin(admin.ModelAdmin):
	list_display = ('id','nombre','resumen','imagen_portadas')
	list_filter=('autor',)
	search_fields = ('nombre','autor__nombre')
	list_editable =('nombre','resumen')
	filter_horizontal = ('autor',)
	def imagen_portadas(self, libro):
		url =libro.Traer_url_portadas()
		tag ="<img src='%s'>" % url
		return tag
	imagen_portadas.allow_tags = True

admin.site.register(Libro,LibroAdmin)
admin.site.register(categorias)