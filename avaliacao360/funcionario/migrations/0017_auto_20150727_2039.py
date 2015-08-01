# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0016_funcionario_isgerente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='isgerente',
            field=models.NullBooleanField(verbose_name=b'Gerente'),
        ),
    ]
