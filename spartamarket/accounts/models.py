from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    image = models.ImageField(upload_to='profile_pics/', default='default.jpg')
    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name='followers')
    
    def __str__(self):
        return f'{self.username} Profile'

