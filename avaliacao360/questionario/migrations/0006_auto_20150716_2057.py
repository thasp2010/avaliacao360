# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0005_auto_20150716_2055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionario',
            old_name='descricao',
            new_name='descricaoquest',
        ),
    ]
