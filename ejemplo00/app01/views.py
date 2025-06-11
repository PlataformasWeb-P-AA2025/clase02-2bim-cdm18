from django.shortcuts import render
from administrativo.models import Estudiante


# Create your views here.

def estudiantes_list(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'templates/estudiantes_list.html', {'estudiantes': estudiantes})
