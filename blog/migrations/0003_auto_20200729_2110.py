# Generated by Django 3.0.8 on 2020-07-29 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200729_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='Изображение'),
        ),
    ]