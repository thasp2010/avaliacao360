# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0006_funcionario_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funcionario',
            old_name='user',
            new_name='usuarioFunc',
        ),
    ]
