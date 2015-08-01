#coding: utf8
from django.db import models
from funcionario.models import Funcionario



class Questionario(models.Model):

	descricao = models.CharField(max_length = 45)

	def __unicode__(self):
		return self.descricao

class Questao(models.Model):

	enunciado = models.TextField(null= False,blank = False)
	alternativaA = models.TextField(null= False,blank = False)
	alternativaB = models.TextField(null= False,blank = False)
	alternativaC = models.TextField(null= True,blank = True)
	alternativaD = models.TextField(null= True,blank = True)
	alternativaE = models.TextField(null= True,blank = True)

	def __unicode__(self):
		return self.enunciado

	class Meta:
		verbose_name = 'Questao'
		verbose_name_plural = 'Questoes'

class Questionario_Questao(models.Model):
	
	idquestao = models.ForeignKey(Questao,null=False, 
		                          blank = False,
		                          related_name='idquestao',
		                          verbose_name=u'Questão')
	idquestionario = models.ForeignKey(Questionario,
		                               null=False, 
		                               blank = False,
		                               related_name='idquestionario',
		                               verbose_name=u'Questionário')

	def __unicode__(self):
		return self.idquestionario.descricao +'-'+self.idquestao.enunciado

	class Meta:
		verbose_name = 'Questões dos questionários'
		verbose_name_plural = 'Questões dos questionários'

class Resposta(models.Model):
	questao = models.ForeignKey(Questao,
								null=False, 
								blank = False,
								related_name='questao')

	questionario = models.ForeignKey(Questionario,
									null=False, 
									blank = False,
									related_name='questionario')
	
	resposta = models.CharField(max_length = 45,null= False)
	
	avaliador = models.ForeignKey(Funcionario,
		                          null=True,
		                          blank = True, 
		                          related_name ='avaliador_id' )

	funcionario = models.ForeignKey(Funcionario,
									null = True,
									blank = True,
									related_name = 'funcionario_id')

	def __unicode__(self):
		return self.resposta

	class Meta:
		verbose_name = 'Resposta'
		verbose_name_plural = 'Respostas'