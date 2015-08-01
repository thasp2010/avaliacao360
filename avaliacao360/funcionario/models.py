#coding: utf8
from django.db import models
from django.contrib.auth.models import User
from departamento.models import Departamento


class Funcionario(models.Model):
	nome            = models.CharField(max_length = 60,null= False,blank = False)
	cpf             = models.CharField(max_length = 11,null= False,blank = False)
	Departamento    = models.ForeignKey(Departamento,null= False,blank = False)
	reponsavel      = models.ForeignKey('self',null= True,blank = True, related_name='responsavel')
	usuario         = models.OneToOneField(User,unique = True,null= True,blank = True)
	isgerente       = models.NullBooleanField(verbose_name='Gerente')
	
	
	def __unicode__(self):
		return self.nome

	class Meta:
		verbose_name = 'Funcionario'
		verbose_name_plural = 'Funcionarios'
		
