# Generated by Django 4.2.1 on 2023-05-21 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_distance_destination'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distance',
            name='destination',
        ),
        migrations.AddField(
            model_name='distance',
            name='source',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.address'),
        ),
    ]
