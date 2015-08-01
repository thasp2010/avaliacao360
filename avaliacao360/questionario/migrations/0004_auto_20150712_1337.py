# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0003_resposta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questao',
            name='alternativaC',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='questao',
            name='alternativaD',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='questao',
            name='alternativaE',
            field=models.TextField(null=True, blank=True),
        ),
    ]
