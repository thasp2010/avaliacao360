# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0002_auto_20150712_1327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resposta', models.CharField(max_length=45)),
                ('questao', models.ForeignKey(related_name='questao', to='questionario.Questao')),
                ('questionario', models.ForeignKey(related_name='questionario', to='questionario.Questionario')),
            ],
        ),
    ]
