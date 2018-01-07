from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserProfile(AbstractUser):

    nickname = models.CharField(max_length=15, verbose_name='昵称')
    email = models.EmailField(verbose_name='邮箱', default='', blank=True)
    gender = models.CharField(choices=(('male', '男'), ('female', '女')), max_length=6, verbose_name='性别')
    introduce = models.TextField(max_length=100, verbose_name='自我介绍', default='', blank=True, null=True)
    image = models.ImageField(upload_to='users/images', max_length=100, verbose_name='头像')
    motto = models.CharField(max_length=20, blank=True, null=True, verbose_name='我的签名')
    province = models.CharField(max_length=25, verbose_name='省份')
    city = models.CharField(max_length=15, verbose_name='城市')
    read_time = models.FloatField(default=0, verbose_name='阅读时间')
    likes = models.IntegerField(default=0, verbose_name='点赞数')

    def __str__(self):
        name = self.nickname or self.username
        return name

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
