from django.db import models
from django.urls import reverse
# Create your models here.

from django.db import models
from django.contrib.auth.models import User
# timezone 用于处理时间相关事务。
from django.utils import timezone
from taggit.managers import TaggableManager
from PIL import Image


class ArticleColumn(models.Model):
    """栏目的model"""
    title = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = '栏目'


# 博客文章数据模型


class ArticlePost(models.Model):

    # 文章栏目的“一对多”外键
    column = models.ForeignKey(
        ArticleColumn,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='article',
        verbose_name='栏目',
    )
    # 文章作者。参数 on_delete 用于指定数据删除的方式
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='作者')
    # charfield保存较短字符，textfield保存长字符
    title = models.CharField(max_length=100, verbose_name='标题')
    body = models.TextField(verbose_name='正文')
    avatar = models.ImageField(
        upload_to='article/%Y%m%d', blank=True, verbose_name='标题图')
    # 文章创建时间。参数 default=timezone.now 指定其在创建数据时将默认写入当前的时间
    created = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    # 文章更新时间。参数 auto_now=True 指定每次数据更新时自动写入当前时间
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    total_views = models.PositiveIntegerField(default=0, verbose_name='浏览数')
    tags = TaggableManager(blank=True, verbose_name='标签')

    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-created' 表明数据应该以倒序排列
        ordering = ('-created',)
        verbose_name = verbose_name_plural = '文章'

    # 函数 __str__ 定义当调用对象的 str() 方法时的返回值内容
    def __str__(self):
        # return self.title 将文章标题返回
        return self.title

    # 获取文章地址
    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.id])

    def save(self, *args, **kwargs):
        # 调用原有save()功能
        article = super(ArticlePost, self).save(*args, **kwargs)

        if self.avatar and not kwargs.get('update_fields'):
            image = Image.open(self.avatar)
            (x, y) = image.size
            new_x = 400
            new_y = int(new_x * (y / x))
            resized_image = image.resize((new_x, new_y), Image.ANTIALIAS)
            resized_image.save(self.avatar.path)

        return article

    def was_created_recently(self):
        # 检查最近发布文章
        diff = timezone.now() - self.created
        if diff.days == 0 and diff.seconds < 60 and diff.seconds >= 0:
            return True
        else:
            return False

