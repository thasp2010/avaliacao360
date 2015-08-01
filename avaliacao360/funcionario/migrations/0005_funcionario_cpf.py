# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0004_auto_20150712_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='cpf',
            field=models.CharField(default=0, max_length=11),
            preserve_default=False,
        ),
    ]
