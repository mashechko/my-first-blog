# Generated by Django 3.0.8 on 2020-07-29 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200729_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(null=True, upload_to='upload/', verbose_name='Файл'),
        ),
    ]
