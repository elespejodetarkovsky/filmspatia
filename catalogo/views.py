from django.shortcuts import render

# Create your views here.
#La función render genera html en funcion de datos y plantillas

from .models import Film, Director, FilmInstance, Genero

def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_films=Film.objects.all().count()
    num_instances=FilmInstance.objects.all().count()
    # Libros disponibles (status = 'a')
    #num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_directores = Director.objects.count()  # El 'all()' esta implícito por defecto.
    
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_films':num_films,'num_instances':num_instances,'num_directores':num_directores},
    )
    
from django.views import generic

class FilmListView(generic.ListView):
    model = Film
    
class FilmDetailView(generic.DetailView):
    model = Film
    
# class DirectoresListView(generic.ListView):
#     model = Director
# 
# class DirectoresDetail(generic.detail):
#     model = Director