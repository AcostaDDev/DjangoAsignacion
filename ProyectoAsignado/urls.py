
from django.contrib import admin
from django.urls import path, include

from Alumnos import views

urlpatterns = [
    path('alumnos/', include('Alumnos.urls')),
    path('admin/', admin.site.urls),
]
