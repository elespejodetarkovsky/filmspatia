from django.db import models

# Create your models here.

class Genero(models.Model):
    """
    Generará el o los generos del film  (p. ej. ciencia ficción, poesía, etc.).
    """
    name = models.CharField(max_length=200, help_text="Ingrese el nombre del género (p. ej. Ciencia Ficción, Poesía Francesa etc.)")
    
    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        """
        return self.name
    
from django.urls import reverse #Used to generate URLs by reversing the URL patterns


class Film(models.Model):
    """
    Modelo que representa una película (un film genérico).
    """

    title = models.CharField(max_length=200)

    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    # ForeignKey, ya que una película tiene un solo director, pero el mismo director puede haber dirigido muchas pelis.
    # 'Director' es un string, en vez de un objeto, porque la clase Author aún no ha sido declarada.

    resumen = models.TextField(max_length=1000, help_text="Ingrese una breve descripción del libro")

    genero = models.ManyToManyField(Genero, help_text="Seleccione el género de la película")
    # ManyToManyField, porque un género puede contener muchos films y un film puede cubrir varios géneros.
    
    lengua = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    
    pais = models.CharField(max_length=200)
    
    cartel_img = models.ImageField(upload_to="ImgFilm")
    
    
    def __str__(self):
        """
        String que representa al objeto Libro
        """
        return self.title
    
    
    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Film
        """
        return reverse('film-detail', args=[str(self.id)])
    
    def display_genero(self):
        """
        Crea un string para mostrar en el admin
        """
        return ', '.join([ Genero.name for Genero in self.genero.all()[:3] ])
#     
    display_genero.short_description = 'genero'
    
    
import uuid # Requerida para las instancias de películas únicas
from django.contrib.auth.models import User
from datetime import date


class FilmInstance(models.Model):
    """
    Modelo que representa una copia específica de una peli (i.e. que puede ser prestado por la biblioteca).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para este film particular en todo el catálogo")
    film = models.ForeignKey(Film, on_delete=models.SET_NULL, null=True) 
    #usuario = models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True)
    fechaPedido = models.DateField(null=True, blank=True)
    prestado_a = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    
    class Meta:
        ordering = ["prestado_a"]
        

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s (%s)' % (self.id,self.film.title)
    
    
class Persona(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    
#     def get_absolute_url(self):
#         """
#         Retorna la url para acceder a una instancia particular de un autor.
#         """
#         return reverse('persona-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String para representar el Objeto Modelo
        """
        return '%s, %s' % (self.last_name, self.first_name)
    
    
class Director(Persona):
    """
    Modelo que representa un director
    """
    date_of_death = models.DateField('Año muerte', null=True, blank=True)
    image = models.ImageField(upload_to="ImgDirectores")
    
    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un director.
        """
        return reverse('director-detail', args=[str(self.id)])
    
class Usuario(Persona):
    """
    Modelo que representa un director
    """
    tel = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    image = models.ImageField(upload_to="ImgUsuarios")
    

class Language(models.Model):
    """Este modelo representa los lenguajes (e.g. English, French, Japanese, etc.)"""
    name = models.CharField(max_length=200,
                            help_text="Ingrese el lenguaje correspondiente (principal)")

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name
    

    