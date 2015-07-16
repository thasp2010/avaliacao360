#coding: utf8
from django.db import models


class Departamento(models.Model):
	descricaodep = models.CharField(max_length = 60,null= False,blank = False)

	def __unicode__(self):
		return self.descricaodep


