from django.db import models
from django.contrib.auth import get_user_model
from django.forms import ValidationError


class TimeStampeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class HashTag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Product(TimeStampeModel):
    STATUS_CHOICES = [
        ('판매중', '판매중'),
        ('판매완료', '판매완료'),
        ('예약중', '예약중'),
    ]
    title = models.CharField(max_length=50)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='판매중')
    content = models.TextField()
    image = models.ImageField(
        upload_to='images/',
        blank=True,
    )
    price = models.IntegerField()
    hits = models.IntegerField(default=0)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='products'
    )
    like_users = models.ManyToManyField(
        get_user_model(),
        related_name='like_products',
    )
    hashtags = models.ManyToManyField(
        HashTag,
        related_name='products',
    )

    def clean(self):
        super().clean()
        if self.price >= 999999999:
            raise ValidationError(
                "판매 금액은 999,999,999 까지 입력 가능합니다."
            )

    def __str__(self):
        return f"{self.status} - {self.title}"


class Comment(TimeStampeModel):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    content = models.CharField(max_length=120)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='comment'
    )

    def __str__(self):
        return self.content
