from django.urls import path
from AppCoder import views

urlpatterns = [
    path('',views.inicio),
    path('crea-curso/<nombre>/<camada>',views.crea_curso), 
    path('profesores/',views.profesores),
    path('estudiantes/',views.estudiantes),
    path('entregables/',views.entregables),
   
]