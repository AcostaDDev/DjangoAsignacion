from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from .models import Alumno
# Create your views here.

@login_required
def index(request):
    alumnos = Alumno.objects.order_by('nombre')
    variables = {'alumnos':alumnos}
    return render(request, 'Alumnos/index.html', variables)


@login_required
def alumno(request, alumno_id):
    alumno = Alumno.objects.get(id=alumno_id)
    variables = {
                    'alumno':alumno,
                }
    return render(request, 'Alumnos/alumno.html', variables)
