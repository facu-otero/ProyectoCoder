from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.forms import CursoFormulario
from AppCoder.models import Curso

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

def profesores(request):
    return render(request,'AppCoder/profesores.html')

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

    
