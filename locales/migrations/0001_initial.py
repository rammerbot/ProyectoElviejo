# Generated by Django 4.1.3 on 2022-12-14 14:08

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local', models.CharField(max_length=50, verbose_name='Local')),
                ('descripcion', ckeditor.fields.RichTextField(verbose_name='Descripcion')),
                ('ubicacion', models.CharField(max_length=220, verbose_name='Direccion')),
                ('imagen', models.ImageField(upload_to='media/articles', verbose_name='Imagen')),
                ('mapa', models.URLField(verbose_name='Google.maps')),
            ],
            options={
                'verbose_name': 'Local',
                'verbose_name_plural': 'Locales',
            },
        ),
    ]
