# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0012_auto_20150716_2055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funcionario',
            old_name='nomeFuncionario',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='usuarioFunc',
            new_name='usuario',
        ),
    ]
