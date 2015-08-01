# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0002_funcionario_reponsavel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='reponsavel',
            field=models.ForeignKey(related_name='responsavel', to='funcionario.Funcionario', null=True),
        ),
    ]
