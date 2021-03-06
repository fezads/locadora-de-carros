# Generated by Django 3.2.9 on 2021-11-06 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Modelos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=7)),
                ('ano', models.CharField(max_length=20)),
                ('cor', models.CharField(max_length=20)),
                ('descricao', models.TextField(max_length=200)),
                ('observacoes', models.TextField(max_length=200)),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Modelos.modelo')),
            ],
        ),
    ]
