from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=70)
    role = models.CharField(max_length=70)
    nationality = models.CharField(max_length=70)


class Editorial(models.Model):
    name = models.CharField(max_length=70)
    country = models.CharField(max_length=70)
    state = models.CharField(max_length=70)


class Comic(models.Model):
    name = models.CharField(max_length=70)
    published_year = models.IntegerField()
    editorial = models.CharField(max_length=70)
