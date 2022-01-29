from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.forms import CursoFormulario, ProfesorFormulario
from AppCoder.models import Curso, Profesor

# Create your views here.

def crea_curso(self, nombre, camada):
    
    curso = Curso(nombre=nombre, camada=camada)
    curso.save()
    return HttpResponse(f'Se creo el curso de {curso.nombre} con el numero de camada {curso.camada}')

def inicio(request):
    return render(request,'AppCoder/inicio.html')
    
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
    
