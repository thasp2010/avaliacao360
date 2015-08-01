# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0009_auto_20150715_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='usuarioFunc',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
