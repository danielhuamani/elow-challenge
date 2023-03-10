# Generated by Django 3.2 on 2023-01-11 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('is_published', models.BooleanField(default=False, verbose_name='Esta publicado?')),
                ('date_start', models.DateTimeField(verbose_name='Fecha de Inicio')),
                ('address', models.CharField(max_length=255, verbose_name='Dirección')),
                ('num_tickets', models.IntegerField(verbose_name='Numero de entradas')),
            ],
            options={
                'verbose_name': 'Events',
                'verbose_name_plural': 'Eventss',
            },
        ),
    ]
