from django.db import models
from django.contrib.auth.models import User


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.CharField(max_length=200)
    paid = models.CharField(max_length=300)