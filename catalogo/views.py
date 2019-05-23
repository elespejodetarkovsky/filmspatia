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
    
    #Número de visita en esta vista, se cuenta como una variable de sisión
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_films':num_films,'num_instances':num_instances,
                 'num_directores':num_directores,
                 'num_visits':num_visits},
    )
    
from django.views import generic

class FilmListView(generic.ListView):
    model = Film
    
class FilmDetailView(generic.DetailView):
    model = Film
    
class DirectorListView(generic.ListView):
    model = Director
    
class DirectorDetailView(generic.DetailView):
    model = Director

from django.contrib.auth.mixins import LoginRequiredMixin

class prestamosByUserListView(LoginRequiredMixin,generic.ListView):
    """
    Generic class-based view listing books on loan to current user. 
    """
    print("Usuario registrado")
    model = FilmInstance
    template_name ='catalogo/filminstance_list_films_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return FilmInstance.objects.filter(prestado_a=self.request.user)
    
    
