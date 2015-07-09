from django.db import models


class Departamento(models.Model):
	descricao = models.CharField(max_length = 60)


