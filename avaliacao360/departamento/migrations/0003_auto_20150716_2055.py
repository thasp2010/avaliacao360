# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_auto_20150711_1723'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'verbose_name': 'Departamento', 'verbose_name_plural': 'Departamentos'},
        ),
    ]
