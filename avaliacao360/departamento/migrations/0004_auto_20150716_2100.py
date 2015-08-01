# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0003_auto_20150716_2055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departamento',
            old_name='descricaodep',
            new_name='descricao',
        ),
    ]
