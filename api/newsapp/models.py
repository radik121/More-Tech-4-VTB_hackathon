from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse


class Trends(models.Model):
    name = models.CharField('Название тренда', max_length=255, db_index=True, unique=True)
    description = models.TextField('Краткое Описание', max_length=1000, db_index=True)
    url = models.URLField('URL', max_length=1024, db_index=True, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Тренд'
        verbose_name_plural = 'Тренды'
        ordering = ['name']


class Insites(models.Model):
    title_insites = models.CharField('Заголовок инсайта', max_length=255, db_index=True, unique=True)
    description = models.TextField('Краткое Описание', max_length=1000, db_index=True)

    def __str__(self):
        return f'{self.title_insites}'

    class Meta:
        verbose_name = 'Инсайт'
        verbose_name_plural = 'Инсайты'
        ordering = ['title_insites']


class Positions(models.Model):
    name = models.CharField('Название должности', max_length=124, db_index=True, unique=True)
    slug = models.SlugField('Slug', max_length=124, unique=True)

    def get_absolute_url(self):
        return reverse('pos', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ['name']


class News(models.Model):
    title = models.CharField('Заголовок', max_length=255, db_index=True, unique=True)
    description = models.TextField('Описание', max_length=1000, db_index=True)
    url = models.URLField('URL', max_length=1024, db_index=True, unique=True)
    date = models.DateField('Дата', max_length=10, db_index=True, )
    tags = ArrayField(models.CharField('Теги', max_length=15))
    positions = models.ForeignKey(Positions, verbose_name='Должность', on_delete=models.CASCADE)
    insites = models.ForeignKey(Insites, verbose_name='Инсайты', on_delete=models.CASCADE)
    trends = models.ManyToManyField(Trends)
    fresh = models.BooleanField()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['date']
