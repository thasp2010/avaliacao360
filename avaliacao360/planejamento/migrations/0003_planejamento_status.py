# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planejamento', '0002_auto_20150716_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='planejamento',
            name='status',
            field=models.NullBooleanField(default=False),
        ),
    ]
