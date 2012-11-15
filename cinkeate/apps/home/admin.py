from django.contrib import admin
from cinkeate.apps.home.models import Materia,Programa,Usuario,Profesor, Parcial, Hoja_Parcial

admin.site.register(Materia)
admin.site.register(Programa)
admin.site.register(Profesor)
admin.site.register(Usuario)
admin.site.register(Parcial)
admin.site.register(Hoja_Parcial)