# Generated by Django 4.0.2 on 2022-04-12 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0012_remove_libro_fecha_desplegar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='hora_creacion',
            field=models.TimeField(blank=True, null=True, verbose_name='Hora de creación'),
        ),
    ]