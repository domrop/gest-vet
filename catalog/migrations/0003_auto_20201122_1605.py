# Generated by Django 3.1.2 on 2020-11-22 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20201122_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pazienti',
            name='razza_paziene',
        ),
        migrations.AddField(
            model_name='pazienti',
            name='razza_paziente',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='razza paziente'),
        ),
    ]
