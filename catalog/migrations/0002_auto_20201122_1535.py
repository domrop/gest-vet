# Generated by Django 3.1.2 on 2020-11-22 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pazienti',
            options={'ordering': ['nome_paziente']},
        ),
        migrations.RemoveField(
            model_name='pazienti',
            name='paziente',
        ),
        migrations.AddField(
            model_name='pazienti',
            name='email_proprietario',
            field=models.EmailField(blank=True, max_length=100, null=True, verbose_name='email proprietario'),
        ),
        migrations.AddField(
            model_name='pazienti',
            name='nome_paziente',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='nome paziente'),
        ),
        migrations.AddField(
            model_name='pazienti',
            name='razza_paziene',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='nome proprietario'),
        ),
        migrations.AddField(
            model_name='pazienti',
            name='telefono_proprietario',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='telefono proprietario'),
        ),
        migrations.AlterField(
            model_name='pazienti',
            name='cognome_proprietario',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='cognome proprietario'),
        ),
        migrations.AlterField(
            model_name='pazienti',
            name='nome_proprietario',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='nome proprietario'),
        ),
    ]
