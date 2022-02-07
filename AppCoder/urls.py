from django.urls import path
from AppCoder import views

#para hacer el logout
from django.contrib.auth.views import LogoutView

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
    path('listaCursos/',views.CursoList.as_view(), name = "List"),
    path('detalleCursos/<pk>',views.CursoDetail.as_view(), name = "Detail"),#pk seria la primary key que es el ID
    path('crearCurso/',views.CursoCreate.as_view(), name = "New"),
    path('actualizaCursos/<pk>',views.CursoUpdate.as_view(), name = "Edit"),
    path('eliminaCursos/<pk>',views.CursoDelete.as_view(), name = "Delete"),
    path('login/',views.login_request, name = "Login"),
    path('registro/',views.register, name = "Registro"),
    path('logout/',LogoutView.as_view(template_name='AppCoder/logout.html'), name = "logout"),
    path('editarPerfil/',views.editarPerfil,name = "editarPerfil"),
    
]