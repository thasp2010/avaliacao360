#coding: utf8
from django.db import models
from funcionario.models import Funcionario
from questionario.models import Questionario


class Planejamento(models.Model):
	avaliador = models.ForeignKey(Funcionario,null=False, blank = False,related_name='avaliadorid')
	funcionario = models.ForeignKey(Funcionario,null=False, blank = False,related_name='funcionarioid')
	questionario = models.ForeignKey(Questionario,null=False, blank = False,related_name='questionarioid')
	status       = models.NullBooleanField(default=False)

	def __unicode__(self):
		return 'Funcionario:'+self.funcionario.nome+'- Avaliador:'+self.avaliador.nome

	class Meta:
		verbose_name = 'Planejamento'
		verbose_name_plural = 'Planejamentos'