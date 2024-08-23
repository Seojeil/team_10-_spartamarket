from django.db import models
from django.contrib.auth import get_user_model
from django.forms import ValidationError


class TimeStampeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(TimeStampeModel):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(
        upload_to='images/',
        blank=True
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
        null=True,
    )

    def clean(self):
        super().clean()
        if self.price >= 999999999:
            raise ValidationError("판매 금액은 999,999,999 까지 입력 가능합니다.")

    def __str__(self):
        return self.title


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
