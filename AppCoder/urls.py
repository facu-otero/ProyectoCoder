from django.urls import path
from AppCoder import views

urlpatterns = [
    path('',views.inicio, name = "inicio"),
    path('crea-curso/<nombre>/<camada>',views.crea_curso), 
    path('cursos/',views.cursos, name = "cursos"),
    path('profesores/',views.profesores, name = "profesores"),
    path('estudiantes/',views.estudiantes, name = "estudiantes"),
    path('entregables/',views.entregables, name = "entregables"),
    path('cursoFormulario/',views.cursoFormulario, name = "cursoFormulario"),
    path('busquedaCamada/',views.busquedaCamada, name = "busquedaCamada"),
    path('buscar/',views.buscar, name = "buscar"),
    path('lista_profesores/',views.leer_profesores, name = "lista_profesores"),
    path('eliminarProfesor/<id_profesor>/',views.elimina_profesor, name = "eliminarProfesor"),
    path('editarProfesor/<profesor_nombre>/',views.editar_profesor, name = "editarProfesor"),
 
]