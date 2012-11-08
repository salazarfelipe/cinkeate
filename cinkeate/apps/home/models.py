from django.db import models

class Materia(models.Model):
	nombre = models.CharField(max_length=100)
	codigo = models.CharField(max_length=100 , primary_key=True)
	programa = models.CharField(max_length=100)
	tematica = models.TextField()

	def __unicode__(self):
		return self.nombre
