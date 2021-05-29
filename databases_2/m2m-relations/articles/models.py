from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )
    #scopes = models.ManyToManyField('Scope', through='Scope_Article', related_name='articles')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Scope(models.Model):
    name = models.CharField(max_length=256, verbose_name='Тема')
    article = models.ManyToManyField(Article, through='Scope_Article', related_name='scopes')

    def __str__(self):
        return self.name


class Scope_Article(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='статья')
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE, verbose_name='тема')
    is_main = models.BooleanField(verbose_name='Основная тема', default=False)

    def __str__(self):
        return f'{self.scope} - {self.article} - {self.is_main}'
