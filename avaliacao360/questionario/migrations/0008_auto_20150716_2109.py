# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0007_auto_20150716_2100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionario_questao',
            old_name='questao',
            new_name='idquestao',
        ),
        migrations.RenameField(
            model_name='questionario_questao',
            old_name='questionario',
            new_name='idquestionario',
        ),
    ]
