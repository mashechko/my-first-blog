# Generated by Django 3.0.8 on 2020-08-27 17:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 27, 17, 52, 4, 883563, tzinfo=utc), null=True, verbose_name='Дата публикации'),
        ),
    ]
