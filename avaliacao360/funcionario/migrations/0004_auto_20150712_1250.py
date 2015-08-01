# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0003_auto_20150712_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='reponsavel',
            field=models.ForeignKey(related_name='responsavel', blank=True, to='funcionario.Funcionario', null=True),
        ),
    ]
