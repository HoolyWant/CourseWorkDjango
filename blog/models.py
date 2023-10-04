from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    content = models.TextField(verbose_name='содержимое')
    links = models.CharField(max_length=500, verbose_name='статьи')
    image = models.ImageField(verbose_name='изображение')
    count = models.IntegerField(verbose_name='количество просмотров')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'

    def __str__(self):
        return f'{self.title} {self.count}'
