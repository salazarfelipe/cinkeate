from django.contrib import admin
from cinkeate.apps.home.models import Materia,Programa,Usuario,Profesor, Parcial, Hoja_Parcial, Actividad, Actividad_Materia, Actividad_Parcial, Comentario_Parcial


class AdminMateria(admin.ModelAdmin):
	list_filter = ('nombre',)
	ordering = ('-nombre',)
	search_fields = ('nombre', 'tematica', 'semestre',)

admin.site.register(Materia, AdminMateria)
admin.site.register(Programa)
admin.site.register(Profesor)
admin.site.register(Usuario)
admin.site.register(Parcial)
admin.site.register(Hoja_Parcial)
admin.site.register(Actividad)
admin.site.register(Actividad_Materia)
admin.site.register(Actividad_Parcial)
admin.site.register(Comentario_Parcial)