# Generated by Django 3.2.9 on 2021-11-06 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Carros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='descricao',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='carro',
            name='observacoes',
            field=models.CharField(max_length=200),
        ),
    ]
