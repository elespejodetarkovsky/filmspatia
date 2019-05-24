from django import forms

from .models import FilmInstance

class FilmInstanceForm(forms.ModelForm):
    '''Formulario en donde el usario registrado
    podrá ingresar sus películas'''
    class Meta:
        model = FilmInstance
        fields = ('film', 'prestado_a',)