# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0005_funcionario_cpf'),
        ('questionario', '0004_auto_20150712_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planejamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avaliador', models.ForeignKey(related_name='avaliadorid', to='funcionario.Funcionario')),
                ('funcionario', models.ForeignKey(related_name='funcionarioid', to='funcionario.Funcionario')),
                ('questionario', models.ForeignKey(related_name='questionarioid', to='questionario.Questionario')),
            ],
        ),
    ]
