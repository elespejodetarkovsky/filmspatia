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

    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    # ForeignKey, ya que una película tiene un solo director, pero el mismo director puede haber dirigido muchas pelis.
    # 'Director' es un string, en vez de un objeto, porque la clase Author aún no ha sido declarada.

    resumen = models.TextField(max_length=1000, help_text="Ingrese una breve descripción del libro")

    genero = models.ManyToManyField(Genero, help_text="Select a genre for this book")
    # ManyToManyField, porque un género puede contener muchos films y un film puede cubrir varios géneros.
    
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
    
    
    
import uuid # Requerida para las instancias de películas únicas

class FilmInstance(models.Model):
    """
    Modelo que representa una copia específica de una peli (i.e. que puede ser prestado por la biblioteca).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para este film particular en todo el catálogo")
    film = models.ForeignKey(Film, on_delete=models.SET_NULL, null=True) 
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    fechaPedido = models.DateField(null=True, blank=True)

#     LOAN_STATUS = (
#         ('m', 'Maintenance'),
#         ('o', 'On loan'),
#         ('a', 'Available'),
#         ('r', 'Reserved'),
#     )

    #status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Disponibilidad del libro')

    class Meta:
        ordering = ["usuario"]
        

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s (%s)' % (self.id,self.book.title)
    
    
class Persona(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    
    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un autor.
        """
        return reverse('author-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String para representar el Objeto Modelo
        """
        return '%s, %s' % (self.last_name, self.first_name)
    
    
class Director(Persona):
    """
    Modelo que representa un director
    """
    date_of_death = models.DateField('Died', null=True, blank=True)
    
class Usuario(Persona):
    """
    Modelo que representa un director
    """
    tel = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    

    