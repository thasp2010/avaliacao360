# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0008_auto_20150716_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionario_questao',
            name='idquestao',
            field=models.ForeignKey(related_name='idquestao', verbose_name='Quest\xe3o', to='questionario.Questao'),
        ),
        migrations.AlterField(
            model_name='questionario_questao',
            name='idquestionario',
            field=models.ForeignKey(related_name='idquestionario', verbose_name='Question\xe1rio', to='questionario.Questionario'),
        ),
    ]
