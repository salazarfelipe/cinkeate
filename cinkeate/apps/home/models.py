from django.db import models
from django.contrib.auth.models import User

class Programa(models.Model):
	nombre 			= models.CharField(max_length=100)
	codigoPrograma 	= models.CharField(max_length=30)
	semaforo 		= models.URLField(blank=True) #link a pensum oficial
	def __unicode__(self):
		return self.nombre	



class Materia(models.Model):
	OPCIONES_SEMESTRE 	= zip(range(1,13),range(1,13)) 
	nombre 				= models.CharField(max_length=100)
	codigo 				= models.CharField(max_length=100 , primary_key=True)
	idPrograma 			= models.ForeignKey(Programa) #0
	tematica 			= models.TextField(blank=True)
	semestre 			= models.IntegerField(choices=OPCIONES_SEMESTRE)

	def __unicode__(self):
		return self.nombre

# Extender de User 
class Usuario(models.Model):
	user 			= models.ForeignKey(User, related_name='perfil', unique=True)
	fechaNacimiento = models.DateField(blank=True,null=True)
	idPrograma 		= models.ForeignKey(Programa)
	semestre 		= models.IntegerField()
	telefono 		= models.CharField(max_length=20,blank=True)
	materias 		= models.ManyToManyField(Materia)
	def __unicode__(self):
		return self.user.first_name+" "+self.user.last_name

class Profesor(models.Model):
	nombre 		= models.CharField(max_length=100)
	apellido 	= models.CharField(max_length=100)
	nick 		= models.CharField(max_length=100, blank=True)	
	idPrograma 	= models.ForeignKey(Programa)
	correo1 	= models.EmailField(blank=True)
	correo2 	= models.EmailField(blank=True)
	idMateria 	= models.ManyToManyField(Materia) #1Profesor_Materia
	def __unicode__(self):
		return self.nombre+" "+self.apellido

	class Meta:
		verbose_name_plural=u'Profesores'


class Parcial(models.Model):
	OPCIONES_DIFICULTAD = zip( range(1,6), ('Refacil','Facil','Normal','Dificil','Redificil'))
	OPCIONES_NOTA = zip((num/10.0 for num in range(0,51,1)),(num/10.0 for num in range(0,51,1))) 
	
	numeroParcial = models.IntegerField( range (1,10)) # El numero del parcial eg: parcial 2 CISCO
	idMateria = models.ForeignKey(Materia)
	idUsuario = models.ForeignKey(Usuario)
	idProfesor = models.ForeignKey(Profesor)
	dificultad = models.IntegerField(choices=OPCIONES_DIFICULTAD, default=3) #2
	numCalificaciones = models.IntegerField() #calificaciones hechas por los usuarios
	calificacion  = models.FloatField() #calificacion de los usuarios
	nota = models.FloatField(choices=OPCIONES_NOTA)
	fecha = models.DateField(help_text='Aproximada')
	fechaSubida = models.DateField(auto_now_add=True)
	def __unicode__(self):
		return "Parcial %s"%unicode(self.id)

	class Meta:
		verbose_name_plural=u'Parciales'
  
  
class Hoja_Parcial(models.Model):

	def url(self,filename):
		return "images/Parciales/%s/%s/%s/%s"%(self.idParcial.idMateria, self.idParcial.idProfesor, self.idParcial , filename)

	idParcial = models.ForeignKey(Parcial)
	archivo = models.FileField(upload_to=url)
	#tipo = models.CharField(max_length=30)
	numero = models.PositiveIntegerField() # Se pueden generar archivos pdf o comprimidos que unen los archivos en unno solo
	formato = models.CharField(max_length=10) 
	def __unicode__(self):
		return "Hoja %d de %s" %(self.numero,unicode(self.idParcial))

	class Meta:
		verbose_name_plural=u'Hojas de Parciales'

class Actividad(models.Model):
  	idUsuario = models.ForeignKey(Usuario)
  	tipo = models.CharField(max_length=20)
  	fecha = models.DateField(auto_now_add=True)
  	def __unicode__(self):
		return "%s por %s" %(self.tipo,unicode(self.idUsuario))

	class Meta:
		verbose_name_plural=u'Actividades'

class Actividad_Materia(models.Model):
  	idActividad = models.ForeignKey(Actividad)
  	idMateria = models.ForeignKey(Materia)
  	def __unicode__(self):
		return "%s (%s)" %(unicode(self.idActividad),unicode(self.idMateria))

	class Meta:
		verbose_name_plural=u'Actividades en Materias'

class Actividad_Parcial(models.Model):
  	idActividad = models.ForeignKey(Actividad)
  	idParcial = models.ForeignKey(Parcial)
  	def __unicode__(self):
		return "%s (%s)" %(unicode(self.idActividad),unicode(self.idParcial))

	class Meta:
		verbose_name_plural=u'Actividades en Parciales'

class Comentario_Parcial(models.Model):  	
  	idParcial = models.ForeignKey(Parcial)
  	idUsuario = models.ForeignKey(Usuario)
  	texto = models.TextField(max_length=300)
  	def __unicode__(self):
		return "Comentario de %s en %s" %(unicode(self.idUsuario),unicode(self.idParcial))

	class Meta:
		verbose_name_plural=u'Comentarios de parciales'