
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class CursoFormulario(forms.Form):
    
    nombre = forms.CharField()
    camada = forms.IntegerField()

class ProfesorFormulario(forms.Form):
    
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)
    

class UserEditForm(UserCreationForm):#para ahcer formulario perssonalizado
    #campos que queremos modificar del fomulario
    email=forms.EmailField(label="Modificar email")
    password1=forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    first_name=forms.CharField()
    last_name=forms.CharField()
    
    class Meta:#clase interna del userCreateForm para pisar lo que viene predeterminado(una de las coasas qque puedo modificar es los campos que quiero mostrar, por ejemplo por defecto viene email y contraseña, en cambio con la modificacion puedo ver ademas el nombre y apellido)
        #tienen que ser datos que se encuentren dentro del model de django que estoy usando
        model=User
        fields=['email', 'password1', 'password2', 'first_name', 'last_name']    
