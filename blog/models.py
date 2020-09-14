from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор', null=True)
    title = models.CharField(max_length=200, verbose_name='Название')
    text = models.TextField(verbose_name='Текст статьи')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации', default=timezone.now())
    image = models.ImageField(verbose_name='Изображение', upload_to='images/', null=True)
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.PROTECT, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('posts_by_categories', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    link = models.URLField(verbose_name='Cсылка', null=True)
    date = models.DateTimeField(verbose_name='Дата', null=True)
    description = models.TextField(verbose_name='Описание статьи', null=True)
    category = models.CharField(max_length=100, verbose_name='Категория', null=True)
    author = models.CharField(max_length=100, verbose_name='Сайт-автор', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-date', 'title']


class Author(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()

  def __str__(self):
      return self.name

