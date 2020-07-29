from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=200, verbose_name='Название')
    text = models.TextField(verbose_name='Текст статьи')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')
    image = models.ImageField(verbose_name='Изображение', null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
