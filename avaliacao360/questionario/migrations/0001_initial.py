# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questionario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enunciado', models.TextField()),
                ('questao1', models.TextField()),
                ('questao2', models.TextField()),
                ('questao3', models.TextField()),
                ('questao4', models.TextField()),
                ('questao5', models.TextField()),
            ],
        ),
    ]
