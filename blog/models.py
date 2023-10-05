from django.db import models

from users.models import User, NULLABLE


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    content = models.TextField(verbose_name='содержимое')
    image = models.ImageField(verbose_name='изображение', **NULLABLE)
    count = models.IntegerField(default=0, verbose_name='количество просмотров')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='пользователь')
    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'

    def __str__(self):
        return f'{self.title}'
