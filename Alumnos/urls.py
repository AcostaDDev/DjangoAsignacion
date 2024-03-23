from django.urls import path

from . import views

app_name = 'Alumnos'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:alumno_id>/', views.alumno, name='alumno'),
]