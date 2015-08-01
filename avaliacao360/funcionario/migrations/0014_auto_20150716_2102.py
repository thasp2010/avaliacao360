# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0013_auto_20150716_2100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funcionario',
            old_name='depFuncionario',
            new_name='Funcionario',
        ),
    ]
