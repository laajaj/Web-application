# Generated by Django 3.1.3 on 2020-11-27 21:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wwwApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vol',
            name='heure_arrivee',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name="heure d'arrivée "),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vol',
            name='heure_depart',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='heure de départ'),
            preserve_default=False,
        ),
    ]
