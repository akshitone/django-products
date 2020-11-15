from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Product(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
