# Generated by Django 3.0.8 on 2020-09-01 13:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20200831_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 1, 13, 42, 50, 712712, tzinfo=utc), null=True, verbose_name='Дата публикации'),
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]
