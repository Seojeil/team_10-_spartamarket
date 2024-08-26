from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User



class User(AbstractUser):
    pass
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics/', default='default.jpg')
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    
    def __str__(self):
        return f'{self.user.username} Profile'



# 새로운 사용자가 생성될 때 해당 사용자의 프로필을 자동으로 생성하는 데코레이터
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# 사용자의 정보가 업데이트될 때 해당 사용자의 프로필도 함께 저장하는 데코레이터
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
