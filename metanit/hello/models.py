from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

class Fly(models.Model):
    paraplan = models.CharField(max_length=50)
    podveska = models.CharField(max_length=30)