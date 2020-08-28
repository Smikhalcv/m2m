from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title



class Tegs(models.Model):

    topic = models.CharField(max_length=256, verbose_name='Название')
    scopes = models.ManyToManyField(
        Article,
        related_name='scopes',
        through='Relationship',
        through_fields=('tegs', 'article')
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.topic

class Relationship(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    tegs = models.ForeignKey(Tegs, on_delete=models.CASCADE)
    main_teg = models.BooleanField()

    class Meta:
        ordering = ["-main_teg"]