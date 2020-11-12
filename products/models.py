from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)
