# Generated by Django 3.0.8 on 2020-08-05 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_post_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='link',
            field=models.URLField(null=True, verbose_name='Cсылка'),
        ),
    ]