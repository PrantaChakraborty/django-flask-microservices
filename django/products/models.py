from django.db import models


# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    image = models.CharField(max_length=255, null=True, blank=True)
    likes = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class User(models.Model):
    pass
