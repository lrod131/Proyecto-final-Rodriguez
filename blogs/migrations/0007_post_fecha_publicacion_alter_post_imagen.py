# Generated by Django 4.1.7 on 2023-03-31 11:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_alter_post_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fecha_publicacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/imagenes/'),
        ),
    ]
