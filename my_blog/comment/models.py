from django.db import models

from django.contrib.auth.models import User
from article.models import ArticlePost
from ckeditor.fields import RichTextField
# Create your models here.


class Comment(models.Model):
    """评论"""
    article = models.ForeignKey(
        ArticlePost,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='文章',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='作者',
    )
    # body = models.TextField(verbose_name='文章主体')
    body = RichTextField(verbose_name='文章主体')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        ordering = ('created',)
        verbose_name = verbose_name_plural = '评论'

    def __str__(self):
        return self.body[:20]
