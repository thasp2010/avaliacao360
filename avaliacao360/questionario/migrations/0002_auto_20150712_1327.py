# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enunciado', models.TextField()),
                ('alternativaA', models.TextField()),
                ('alternativaB', models.TextField()),
                ('alternativaC', models.TextField()),
                ('alternativaD', models.TextField()),
                ('alternativaE', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Questionario_Questao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idquestao', models.ForeignKey(related_name='idquestao', to='questionario.Questao')),
            ],
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='enunciado',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='questao1',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='questao2',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='questao3',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='questao4',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='questao5',
        ),
        migrations.AddField(
            model_name='questionario',
            name='descricaoquest',
            field=models.CharField(default='null', max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionario_questao',
            name='idquestionario',
            field=models.ForeignKey(related_name='idquestionario', to='questionario.Questionario'),
        ),
    ]
