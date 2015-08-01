# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0018_funcionario_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='foto',
        ),
    ]
