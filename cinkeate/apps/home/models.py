from django.db import models

class Programa(models.Model):
	nombre = models.CharField(max_length=100)
	#ISCS? que campo es este?
	#Semaforo seria otra clase (tabla) ?
	def __unicode__(self):
		return self.nombre	

class Usuario(models.Model):
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	correo = models.EmailField()
	clave = models.CharField(max_length=30)
	fechaNacimiento = models.DateField()
	idPrograma = models.ForeignKey(Programa)
	semestre = models.IntegerField()
	telefono = models.CharField(max_length=20)
	def __unicode__(self):
		return self.nombre

class Materia(models.Model):
	nombre = models.CharField(max_length=100)
	codigo = models.CharField(max_length=100 , primary_key=True)
	#idPrograma = models.ForeignKey(Programa) #0
	tematica = models.TextField()
	def __unicode__(self):
		return self.nombre

class Profesor(models.Model):
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	nick = models.CharField(max_length=100)
	correo = models.EmailField()	
	idPrograma = models.ForeignKey(Programa)
	correo1 = models.EmailField()
	correo2 = models.EmailField()
	idMateria = models.ManyToManyField(Materia) #1	
	def __unicode__(self):
		return self.nombre


class Parcial(models.Model):
	OPCIONES_DIFICULTAD = zip( range(1,6), ('Refacil','Facil','Normal','Dificil','Redificil'))
	OPCIONES_NOTA = zip((num/10.0 for num in range(0,51,1)),(num/10.0 for num in range(0,51,1))) 
	OPCIONES_SEMESTRE = zip(range(1,13),range(1,13)) 

	idMateria = models.ForeignKey(Materia)
	idProfesor = models.ForeignKey(Profesor)
	dificultad = models.IntegerField(choices=OPCIONES_DIFICULTAD, default=3) #2
	#calificacion  ? es diferente a dificultad y nota?	
	nota = models.FloatField(choices=OPCIONES_NOTA)#3
	fecha = models.DateField(help_text='Aproximada')
	semestre = models.IntegerField(choices=OPCIONES_SEMESTRE)

  
class Hoja_Parcial(models.Model):
	idParcial = models.ForeignKey(Parcial)	
	numero = models.PositiveIntegerField()
	formato = models.CharField(max_length=10)
	def __unicode__(self):
		return "hoja "+self.numero
  


"""
#0.1 Si activo este campo como ForeignKey me saca error al intentar ver las materias (esto no pasa con lso otros ForeignKey)
0.2 Si activo el campo tambien me saca error al ver los parciales
Lo curiosos de los dos y es que al intengar agregar no pone problema

#1Tengo entendido que esto ya me crea la relacion de Profesor-Materias, cito la guia:
Behind the scenes, Django creates an intermediary join table to represent the many-to-many relationship.
It doesn't matter which model gets the ManyToManyField, but you need it in only one of the models - not in both.

#2 Para poner un rango se puede hacer de varias maneras:
crear una nueva clase IntegerRangeField por ej que reciba los rangos como param
#se puede hacer con validadores luego
#Se puee hacer con el parametro choices, me parecio la mas simple y fue la que tome

#3 Esta fue un toque mas complicada porque el range no soporta floats, pero en realidad hice lo mismo que para las opciones de dificultad
Tambien se puede definir nota asi-> nota = models.FloatField(max_digits=2, decimal_places=1) 
para que tenga un decimal  y un entero, pero faltaria definir que el rango es de 0 a 5

Falta definir que valores TIENEN que ir (not null o blank=false)

Me surgieron varias dudas con respecto a las actividades entonces mejor no lo hice por ahora.

Las clases que llamo desde un ForeignKey tienen que estar arriba en el codigo  :S wtf?
"""