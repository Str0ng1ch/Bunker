from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    correct = models.IntegerField()
    incorrect = models.IntegerField()


class Attempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    correct = models.IntegerField()
    incorrect = models.IntegerField()
