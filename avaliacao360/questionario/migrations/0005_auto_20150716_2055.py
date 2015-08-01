# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0004_auto_20150712_1337'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questao',
            options={'verbose_name': 'Questao', 'verbose_name_plural': 'Questoes'},
        ),
        migrations.AlterModelOptions(
            name='questionario_questao',
            options={'verbose_name': 'Quest\xf5es dos question\xe1rios', 'verbose_name_plural': 'Quest\xf5es dos question\xe1rios'},
        ),
        migrations.AlterModelOptions(
            name='resposta',
            options={'verbose_name': 'Resposta', 'verbose_name_plural': 'Respostas'},
        ),
        migrations.RenameField(
            model_name='questionario',
            old_name='descricaoquest',
            new_name='descricao',
        ),
    ]
