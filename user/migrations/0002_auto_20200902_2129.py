# Generated by Django 3.0.8 on 2020-09-02 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isauthor',
            field=models.BooleanField(default=False, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='user',
            name='profileimg',
            field=models.ImageField(null=True, upload_to='', verbose_name='Фото профиля'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, unique=True, verbose_name='Имя пользователя'),
        ),
    ]
