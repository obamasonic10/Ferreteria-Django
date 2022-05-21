# Generated by Django 3.2.8 on 2022-05-21 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ferreteria', '0003_auto_20220521_0032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('rutAdmin', models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='Rut Administrador')),
                ('nombreAdmin', models.CharField(max_length=60, verbose_name='Nombre Administrador')),
                ('apellidopAdmin', models.CharField(max_length=60, verbose_name='Apellido Paterno Administrador')),
                ('apellidomAdmin', models.CharField(max_length=60, verbose_name='Apellido Materno Administrador')),
                ('password', models.CharField(max_length=60, verbose_name='Password')),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('idcomuna', models.AutoField(primary_key=True, serialize=False, verbose_name='id Comuna')),
                ('nombreComuna', models.CharField(max_length=50, verbose_name='Nombre Comuna')),
            ],
        ),
    ]