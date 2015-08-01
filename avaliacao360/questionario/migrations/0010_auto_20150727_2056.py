# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0017_auto_20150727_2039'),
        ('questionario', '0009_auto_20150726_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='resposta',
            name='avaliador',
            field=models.ForeignKey(related_name='avaliador_id', blank=True, to='funcionario.Funcionario', null=True),
        ),
        migrations.AddField(
            model_name='resposta',
            name='funcionario',
            field=models.ForeignKey(related_name='funcionario_id', blank=True, to='funcionario.Funcionario', null=True),
        ),
    ]
