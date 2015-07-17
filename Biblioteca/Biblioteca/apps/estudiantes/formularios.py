from django.contrib import admin
from django.forms import ModelForm
from django import forms
from .models import *

class reservaForm(ModelForm):
	class Meta():
		model = Estudiante
		exclude=['Libro']
		#podemos acultar los campos k no quremos ver como libro o bien podemos crear un formulario como en el modelos