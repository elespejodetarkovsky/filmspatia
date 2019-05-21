from django.contrib import admin

# Register your models here.
from .models import Film, Genero, Usuario, Director, FilmInstance, Language

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'display_genero')

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    pass

@admin.register(FilmInstance)
class FilmInstanceAdmin(admin.ModelAdmin):
    pass

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    pass

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass