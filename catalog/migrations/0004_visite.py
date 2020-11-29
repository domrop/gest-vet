# Generated by Django 3.1.2 on 2020-11-23 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20201122_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_visita', models.DateTimeField(default=None)),
                ('anamnesi', models.CharField(blank=True, max_length=2048, null=True, verbose_name='anamnesi')),
                ('prognosi', models.CharField(blank=True, max_length=2048, null=True, verbose_name='prognosi')),
                ('prescrizioni', models.CharField(blank=True, max_length=2048, null=True, verbose_name='prescrizioni')),
                ('idPaziente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.pazienti')),
            ],
        ),
    ]
