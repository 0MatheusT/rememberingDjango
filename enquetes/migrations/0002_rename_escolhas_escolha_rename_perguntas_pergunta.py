# Generated by Django 4.0.4 on 2022-04-19 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enquetes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Escolhas',
            new_name='Escolha',
        ),
        migrations.RenameModel(
            old_name='Perguntas',
            new_name='Pergunta',
        ),
    ]
