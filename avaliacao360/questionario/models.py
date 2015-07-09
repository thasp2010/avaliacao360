from django.db import models

class Questionario(models.Model):
	enunciado = models.TextField()
	questao1 = models.TextField()
	questao2 = models.TextField()
	questao3 = models.TextField()
	questao4 = models.TextField()
	questao5 = models.TextField()

