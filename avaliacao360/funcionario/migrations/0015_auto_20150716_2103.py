# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0014_auto_20150716_2102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funcionario',
            old_name='Funcionario',
            new_name='Departamento',
        ),
    ]
