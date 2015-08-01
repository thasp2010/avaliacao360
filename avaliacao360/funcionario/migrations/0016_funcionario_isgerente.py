# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0015_auto_20150716_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='isgerente',
            field=models.NullBooleanField(),
        ),
    ]
