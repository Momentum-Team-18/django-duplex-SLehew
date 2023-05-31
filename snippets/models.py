from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    location = models.CharField(max_length=30, blank=True, null=True)


class Snippet(models.Model):
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    snip = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.ForeignKey(to='Language', on_delete=models.CASCADE,)

    def __str__(self):
        return self.description


class Language(models.Model):
    language = models.TextField(max_length=200)
