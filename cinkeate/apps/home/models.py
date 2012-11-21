from django.db import models

class Programa(models.Model):
	nombre = models.CharField(max_length=100)
	codigoPrograma = models.CharField(max_length=30)
	semaforo = models.URLField(blank=True);
	def __unicode__(self):
		return self.nombre	

class Usuario(models.Model):
	nombres = models.CharField(max_length=100)
	apellidos = models.CharField(max_length=100)
	correo = models.EmailField()
	clave = models.CharField(max_length=30)
	fechaNacimiento = models.DateField()
	idPrograma = models.ForeignKey(Programa)
	semestre = models.IntegerField()
	telefono = models.CharField(max_length=20,blank=True)
	def __unicode__(self):
		return self.nombres+" "+self.apellidos

class Materia(models.Model):
	nombre = models.CharField(max_length=100)
	codigo = models.CharField(max_length=100 , primary_key=True)
	idPrograma = models.ForeignKey(Programa) #0
	tematica = models.TextField(blank=True)
	def __unicode__(self):
		return self.nombre

class Profesor(models.Model):
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	nick = models.CharField(max_length=100)	
	idPrograma = models.ForeignKey(Programa)
	correo1 = models.EmailField(blank=True)
	correo2 = models.EmailField(blank=True)
	idMateria = models.ManyToManyField(Materia) #1Profesor_Materia
	def __unicode__(self):
		return self.nombre+" "+self.apellido


class Parcial(models.Model):
	OPCIONES_DIFICULTAD = zip( range(1,6), ('Refacil','Facil','Normal','Dificil','Redificil'))
	OPCIONES_NOTA = zip((num/10.0 for num in range(0,51,1)),(num/10.0 for num in range(0,51,1))) 
	OPCIONES_SEMESTRE = zip(range(1,13),range(1,13)) 
	idMateria = models.ForeignKey(Materia)
	idUsuario = models.ForeignKey(Usuario)
	idProfesor = models.ForeignKey(Profesor)
	dificultad = models.IntegerField(choices=OPCIONES_DIFICULTAD, default=3) #2
	calificacion  = models.FloatField()
	numCalificaciones = models.IntegerField()
	nota = models.FloatField(choices=OPCIONES_NOTA)
	fecha = models.DateField(help_text='Aproximada')
	semestre = models.IntegerField(choices=OPCIONES_SEMESTRE)
	def __unicode__(self):
		return "Parcial de %s"%unicode(self.idMateria)
  
class Hoja_Parcial(models.Model):
	idParcial = models.ForeignKey(Parcial)
	archivo = models.FileField(upload_to='/parciales')	#Definir el upload_to
	tipo = models.CharField(max_length=30)
	numero = models.PositiveIntegerField()
	formato = models.CharField(max_length=10)
	def __unicode__(self):
		return "Hoja %d de %s" %(self.numero,unicode(self.idParcial))

class Actividad(models.Model):
  	idUsuario = models.ForeignKey(Usuario)
  	tipo = models.CharField(max_length=20)
  	fecha = models.DateField(auto_now_add=True)
  	def __unicode__(self):
		return "%s por %s" %(self.tipo,unicode(self.idUsuario))

class Actividad_Materia(models.Model):
  	idActividad = models.ForeignKey(Actividad)
  	idMateria = models.ForeignKey(Materia)
  	def __unicode__(self):
		return "%s (%s)" %(unicode(self.idActividad),unicode(self.idMateria))

class Actividad_Parcial(models.Model):
  	idActividad = models.ForeignKey(Actividad)
  	idParcial = models.ForeignKey(Parcial)
  	def __unicode__(self):
		return "%s (%s)" %(unicode(self.idActividad),unicode(self.idParcial))

class Comentario_Parcial(models.Model):  	
  	idParcial = models.ForeignKey(Parcial)
  	idUsuario = models.ForeignKey(Usuario)
  	texto = models.TextField(max_length=300)
  	def __unicode__(self):
		return "Comentario de %s en %s" %(unicode(self.idUsuario),unicode(self.idParcial))
  	
"""
No se que ruta definir para el upload_to, por lo tanto no pude probar la subida de archivos y las hojas_parcial

falta devfinir not null o blank=false

Las clases que llamo desde un ForeignKey tienen que estar arriba en el codigo  :S wtf?
"""