# from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.
# def homepage(request):
#     return render(request, "homepage.html")

class Homepage(TemplateView):
    template_name = "homepage.html"


# url - view - html
    
# Class Base view

class Homefilmes(ListView):
    template_name = "homefilmes.html"
    model = Filme
    # objet_list -> Lista de itens do modelo

class Detalhesfilmes(DetailView):
    template_name = 'detalhesfilmes.html'
    model = Filme
    # object -> 1 item do nosso modelo.


# def homefilmes(request):
#     context = {}
#     lista_filmes = Filme.objects.all()
#     context['lista_filmes'] = lista_filmes
#     return render(request, "homefilmes.html", context)