#coding: utf8
from django.db import models


class Departamento(models.Model):
	descricao = models.CharField(max_length = 60,null= False,blank = False)

	def __unicode__(self):
		return self.descricao

	class Meta:
		verbose_name = 'Departamento'
		verbose_name_plural = 'Departamentos'


