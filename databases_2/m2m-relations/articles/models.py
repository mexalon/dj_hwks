from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


# class Scope(models.Model):
#     topic = models.CharField(max_length=256, verbose_name='Тема')
#     article = models.ManyToManyField(Article, through='Scope_Article', related_name='scopes')
#
#     def __str__(self):
#         return self.topic
#
#
# class Scope_Article(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='статья')
#     scope = models.ForeignKey(Scope, on_delete=models.CASCADE, verbose_name='тема')
#     is_main = models.BooleanField(verbose_name='Основная тема', default=False)
#
#     def __str__(self):
#         return f'{self.scope} - {self.article} - {self.is_main}'

class Topic(models.Model):
    topic = models.CharField(max_length=256, verbose_name='Тема')
    article = models.ManyToManyField(Article, through='Scopes', related_name='topics')

    def __str__(self):
        return self.topic


class Scopes(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='статья', related_name='scopes')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='тема')
    is_main = models.BooleanField(verbose_name='Основная тема', default=False)

    def __str__(self):
        return f'{self.topic} - {self.article} - {self.is_main}'
