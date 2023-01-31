# Generated by Django 4.1.3 on 2022-11-15 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titulo')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('slug', models.CharField(max_length=150, unique=True, verbose_name='URL amigable')),
                ('vivible', models.BooleanField(verbose_name='visible')),
                ('create_at', models.DateField(auto_now_add=True, verbose_name='Creado el ')),
                ('update_at', models.DateField(auto_now=True, verbose_name='Actualizado el ')),
            ],
            options={
                'verbose_name': 'Pagina',
                'verbose_name_plural': 'Paginas',
            },
        ),
    ]
