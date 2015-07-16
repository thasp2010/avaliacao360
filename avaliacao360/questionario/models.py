#coding: utf8
from django.db import models

class Questionario(models.Model):
	descricaoquest = models.CharField(max_length = 45)

	def __unicode__(self):
		return self.descricaoquest

class Questao(models.Model):
	enunciado = models.TextField(null= False,blank = False)
	alternativaA = models.TextField(null= False,blank = False)
	alternativaB = models.TextField(null= False,blank = False)
	alternativaC = models.TextField(null= True,blank = True)
	alternativaD = models.TextField(null= True,blank = True)
	alternativaE = models.TextField(null= True,blank = True)

	def __unicode__(self):
		return self.enunciado

class Questionario_Questao(models.Model):
	idquestao = models.ForeignKey(Questao,null=False, blank = False,related_name='idquestao')
	idquestionario = models.ForeignKey(Questionario,null=False, blank = False,related_name='idquestionario')

	def __unicode__(self):
		return self.idquestionario.descricaoquest

class Resposta(models.Model):
	questao = models.ForeignKey(Questao,null=False, blank = False,related_name='questao')
	questionario = models.ForeignKey(Questionario,null=False, blank = False,related_name='questionario')
	resposta = models.CharField(max_length = 45,null= False)

