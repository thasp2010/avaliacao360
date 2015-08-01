# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='reponsavel',
            field=models.ForeignKey(related_name='responsavel', default=1, to='funcionario.Funcionario'),
            preserve_default=False,
        ),
    ]
