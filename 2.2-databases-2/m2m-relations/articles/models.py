from django.db import models


class Articles_tag(models.Model):
    name = models.CharField(max_length=40, unique=True, verbose_name='Тег')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

class Article(models.Model):
    title = models.CharField(max_length=256, unique=True, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )
    tags = models.ManyToManyField("Articles_tag", through="Scope")

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, to_field='title', related_name='scopes')
    tag = models.ForeignKey(Articles_tag, on_delete=models.CASCADE, to_field='name', related_name='scopes')
    is_main = models.BooleanField(default=False, verbose_name='Основной')
