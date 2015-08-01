# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0006_auto_20150716_2057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionario',
            old_name='descricaoquest',
            new_name='descricao',
        ),
        migrations.RenameField(
            model_name='questionario_questao',
            old_name='idquestao',
            new_name='questao',
        ),
        migrations.RenameField(
            model_name='questionario_questao',
            old_name='idquestionario',
            new_name='questionario',
        ),
    ]
