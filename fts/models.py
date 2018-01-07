from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField
from django.db import models


class Article(models.Model):
    headline = models.TextField()
    content = models.TextField()
    search_vector = SearchVectorField(null=True)

    class Meta(object):
        indexes = [GinIndex(fields=['search_vector'])]


class Comment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    content = models.TextField()
