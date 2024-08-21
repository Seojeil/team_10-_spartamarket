from django.db import models
from django.contrib.auth import get_user_model


class Product(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='images/',
        blank=True
    )
    price = models.IntegerField()
    # 글작성자
    # author = models.ForeignKey(
    #     get_user_model(),
    #     on_delete=models.CASCADE,
    #     related_name='products'
    #     )
    # 찜하기
    # like_users = models.ManyToManyField(
    #     get_user_model(),
    #     related_name='like_products',
    #     null=True,
    #     )

    def __str__(self):
        return self.title


class Comment(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    content = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 댓글 작성자
    # author = models.ForeignKey(
    #     get_user_model(),
    #     on_delete=models.CASCADE,
    #     related_name='comment'
    #     )

    def __str__(self):
        return self.content
