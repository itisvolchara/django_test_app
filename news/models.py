from django.db import models


class Articles(models.Model):

    title = models.CharField('Название', max_length=100)
    announce = models.CharField('Анонс', max_length=250)
    text = models.TextField('Содержание')
    date_time = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
