
from django.contrib import admin
from django.urls import path, include

from Alumnos import views

urlpatterns = [
    path('alumnos/', include('Alumnos.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('', views.log_out, name='logout'),
]
