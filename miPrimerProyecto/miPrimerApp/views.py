from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse

# Create your views here.
def home(request):
    plantilla = open("C:/Users/Davinson/OneDrive - Tecnologico de Antioquia Institucion Universitaria/Documentos/Davinson/clases/2022-2/Tendencias de desarrollo/DJANGO/miPrimerProyecto/miPrimerApp/templates/index.html")
    template = Template(plantilla.read())
    plantilla.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)