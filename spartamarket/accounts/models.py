from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


# class Signup(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
