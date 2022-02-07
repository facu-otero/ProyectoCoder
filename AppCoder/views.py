from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.forms import CursoFormulario, ProfesorFormulario, UserEditForm
from AppCoder.models import Curso, Profesor, Avatar
from django.views.generic import ListView
#para crud
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
#para login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
#para crear usuario
from django.contrib.auth.forms import UserCreationForm
#para usar mixins, sirve para bloquear contenido cuando el usuario no este logueado en las vistas tipo clases
from django.contrib.auth.mixins import LoginRequiredMixin
#Para importar decoradores, sirve para bloquear contenido cuando el usuario no este logueado en las vistas tipo funciones
from django.contrib.auth.decorators import login_required


# Create your views here.

def crea_curso(self, nombre, camada):
    
    curso = Curso(nombre=nombre, camada=camada)
    curso.save()
    return HttpResponse(f'Se creo el curso de {curso.nombre} con el numero de camada {curso.camada}')

def inicio(request):
    
    avatar= Avatar.objects.filter(user=request.user.id)
    
    return render(request,'AppCoder/inicio.html',{'url': avatar[0].imagen.url})
    
def cursos(request):
    lista = Curso.objects.all()
    
    return render(request,'AppCoder/cursos.html', {"lista":lista})



def estudiantes(request):
    return render(request,'AppCoder/estudiantes.html')

def entregables(request):
    return render(request,'AppCoder/entregables.html') 

def cursoFormulario(request):
    if (request.method == 'POST'):
        
        mi_formulario = CursoFormulario(request.POST)
        
        if(mi_formulario.is_valid()):
            
            data = mi_formulario.cleaned_data
            
            curso = Curso (nombre = data['nombre'], camada = data['camada'])
            
            curso.save()
        
            return render(request, "AppCoder/inicio.html")
    else:
            mi_formulario = CursoFormulario()
    return render(request, "AppCoder/cursoFormulario.html",{'form': mi_formulario})

def busquedaCamada(request):
    return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):
    
        if(request.method == 'GET'):
            
            camada = request.GET['camada']
            cursos = Curso.objects.filter(camada = camada)
            return render(request,"AppCoder/cursos.html", {'cursos': cursos, 'camada': camada})
        else:
            return HttpResponse(f'No se encontro la camada')
# utilizo decorador para que no me aparezca la funcion cunado no este logueado, se pone simepre arriba de la funcion que quiero bloquear cuanod no este logueado
@login_required       
def leer_profesores(request):
    
    profesores = Profesor.objects.all() #traigo todos los profesores
    
    return render(request, "AppCoder/lista_profesores.html",{"profesores":profesores})#con el ultimo pedazo de codigo llamo el contexto, que no es mas que un diccionario

def profesores(request):#para guardar formulario de carga de profesores
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)#aca llegan todos los datos del html
    
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            
            profesor = Profesor (nombre=info['nombre'], apellido=info['apellido'], email=info['email'], profesion=info['profesion'])
            profesor.save()
            return render(request, "AppCoder/inicio.html")#volves al inicio
        
    else:
            miFormulario=ProfesorFormulario()#formulario vacio para cargar de nuevo
            
    return render(request,"AppCoder/profesores.html", {'formulario':miFormulario})
            
    
def elimina_profesor(request, id_profesor):
    profesor=Profesor.objects.get(id=id_profesor)#uso el meetodo get porque me devuelve una unica instancia de esa clase o modelo
    
    profesor.delete()#elimino el profesor seleccionado
    profesores =Profesor.objects.all()#retorno todos los profesores que quedaron
    return render(request,"AppCoder/lista_profesores.html",{"profesores":profesores})#hago que retorne de nuevo la lista de profesores

def editar_profesor(request, profesor_nombre):#para editar el profesor
    profesor=Profesor.objects.get(nombre=profesor_nombre)
    
    if request.method == 'POST':
        
        miFormulario = ProfesorFormulario(request.POST)#aca llegan todos los datos del html
    
        if miFormulario.is_valid():
            
            info = miFormulario.cleaned_data
            
            profesor.nombre=info['nombre']
            profesor.apellido=info['apellido']
            profesor.email=info['email']
            profesor.profesion=info['profesion']
                        
            profesor.save()
            
            return render(request, "AppCoder/inicio.html")#volves al inicio
        
    else:
        #creo el formulario con datos que voy a cambiar osea traigo lo que ya tiene cargado el profeso
            miFormulario=ProfesorFormulario(initial={'nombre':profesor.nombre, 'apellido': profesor.apellido , 'email': profesor.email, 'profesion': profesor.profesion})
            
    #voy al template para editarlo
    return render(request,"AppCoder/editarProfesor.html",{"miformulario":miFormulario, "profesor_nombre":profesor_nombre})#hago que retorne de nuevo la lista de profesores
    
    
class CursoList(LoginRequiredMixin, ListView):#le pongo condicion con mixins de que debe estar logueado para ver  esta class
    
    model= Curso
    template_name="AppCoder/curso_list.html"
class CursoDetail(DetailView):
    
    model= Curso
    template_name="AppCoder/curso_detalle.html"#nos permite renderizar un html con un formulario con los input necesarios para actualizar la nueva informacion o crear una nueva instancia como un nuevo curso

class CursoUpdate(UpdateView):
    
    model= Curso
    success_url='/AppCoder/listaCursos'
    fields=['nombre','camada']
    
    
class CursoDelete(DeleteView):
    
    model= Curso
    success_url='/AppCoder/listaCursos'
    template_name='AppCoder/curso_confirm_delete.html'#renderiza un template de confirmacion que nos permite enviar un template con metodo post para elminar el curso

class CursoCreate(CreateView):
    
    model= Curso
    success_url='/AppCoder/listaCursos'
    fields=['nombre','camada']


    
def login_request(request):
    if request.method =='POST':
        
        form=AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            
            data=form.cleaned_data
            
            user=authenticate(username=data['username'], password=data['password'])
            
            if user is not None:
                login(request, user)
                
                avatar= Avatar.objects.filter(user=request.user.id)
                
                return render(request,'AppCoder/inicio.html',{'mensaje': f'Bienvenido {user.get_username()}','url': avatar[0].imagen.url})
            
            else:
                
                return render(request, 'Appcoder/inicio.html',{'mensaje':'Fallo la auenticacion, intentalo de nuevo'})
            
        else:
            return render(request, 'Appcoder/inicio.html',{'mensaje':'Formulario erroneo'})
    
    else: 
        
        form = AuthenticationForm()
        
        return render(request,'AppCoder/login.html', {'form': form})
    
def register(request): #generar un usuario desde la App
    if request.method =='POST':
        
        form=UserCreationForm(request.POST)
        
        if form.is_valid():
            
            username: form.cleaned_data['username']
            form.save()
            
            return render(request, "AppCoder/inicio.html",{"mensaje": "Usuario creado con exito"})
        
        else:
            return render(request, "AppCoder/inicio.html",{"mensaje": "Usuario no creado, reintentar"})
    
    else:
        
        form = UserCreationForm()
        
        return render(request, 'AppCoder/registro.html',{'form':form})
    
def editarPerfil(request):#para editar perfil de usuario ya creado
    
    usuario = request.user
    
    if request.method == 'POST':
        miFormulario= UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            usuario.save()
            
            return render(request,"AppCoder/inicio.html")
    else:
        miFormulario= UserEditForm(initial={'email':usuario.email, 'first_name':usuario.first_name,'last_name':usuario.last_name })
        
    return render(request,"AppCoder/editarPerfil.html",{'miFormulario':miFormulario, 'usuario':usuario})
                