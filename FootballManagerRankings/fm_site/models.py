from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=255)
    age = models.BigIntegerField(null=True)
    position = models.BigIntegerField(null=True)
    club = models.BigIntegerField(null=True)
    foot = models.BigIntegerField(null=True)


class Club(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)