from django.contrib import admin

from AppCoder.models import Avatar, Curso, Entregable, Estudiante, Profesor

# Register your models here.
#aca se registran todos los modelos que quiero que sean visibles desde el admin

admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Entregable)
admin.site.register(Profesor)
admin.site.register(Avatar)