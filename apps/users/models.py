from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserProfile(AbstractUser):

    nickname = models.CharField(max_length=50, verbose_name='昵称', help_text='昵称')
    email = models.EmailField(max_length=50, verbose_name='邮箱', default='', blank=True, help_text='邮箱')
    gender = models.CharField(choices=(('male', '男'), ('female', '女')), max_length=6, verbose_name='性别', help_text='性别')
    introduce = models.TextField(max_length=100, verbose_name='自我介绍', default='', blank=True, null=True, help_text='自我介绍')
    image = models.ImageField(upload_to='users/images', max_length=100, verbose_name='头像', help_text='头像')
    motto = models.CharField(max_length=20, blank=True, null=True, verbose_name='我的签名', help_text='我的签名')
    province = models.CharField(max_length=25, verbose_name='省份', help_text='省份')
    city = models.CharField(max_length=15, verbose_name='城市', help_text='城市')
    read_time = models.FloatField(default=0, verbose_name='阅读时间', help_text='阅读时间')
    likes = models.IntegerField(default=0, verbose_name='点赞数', help_text='点赞数')

    def __str__(self):
        name = self.nickname or self.username
        return name

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class Follow(models.Model):
    """
    用户关注
    """
    followed = models.ForeignKey(UserProfile, related_name='followed', verbose_name='被关注者', help_text='被关注者 ID')
    following = models.ForeignKey(UserProfile, related_name='following', verbose_name='关注者', help_text='关注者 ID')
    follow_time = models.DateTimeField(default=datetime.now, verbose_name='关注时间', help_text='关注时间')

    def __str__(self):
        return self.following.nickname

    class Meta:
        verbose_name = '关注'
        verbose_name_plural = verbose_name


class Account(models.Model):
    """
    用户账户
    """
    user = models.ForeignKey(UserProfile, verbose_name='用户', )
    balance = models.FloatField(default=0, verbose_name='余额', help_text='余额')
    present = models.FloatField(default=0, verbose_name='赠币', help_text='赠币')
    recharge = models.FloatField(default=0, verbose_name='充值币', help_text='充值币')

    def __str__(self):
        return self.user.nickname

    class Meta:
        verbose_name = '用户账户'
        verbose_name_plural = verbose_name


class Purchased(models.Model):
    """
    用户已购内容
    """

    from books.models import Chapter, Book

    user = models.ForeignKey(UserProfile, verbose_name='用户')
    book = models.ForeignKey(Book, verbose_name='图书', help_text='图书对应 ID')
    chapter = models.ForeignKey(Chapter, blank=True, null=True, verbose_name='章节', help_text='章节对应 ID')
    buy_time = models.DateTimeField(default=datetime.now, verbose_name='购买时间')

    def __str__(self):
        return self.user.nickname + "  " + self.book.name

    class Meta:
        verbose_name = '已购内容'
        verbose_name_plural = verbose_name


class DealLog(models.Model):
    """
    交易记录
    """

    from books.models import Book, Chapter

    BUY_TYPE = (
        ('pay', '支付'),
        ('income', '收入')
    )

    CURRENCY = (
        ('recharge', '充值币'),
        ('present', '赠币')
    )

    user = models.ForeignKey(UserProfile, verbose_name='用户', help_text='用户对应 ID')
    book = models.ForeignKey(Book, verbose_name='图书', help_text='图书对应 ID')
    chapter = models.ForeignKey(Chapter, blank=True, null=True, verbose_name='章节', help_text='章节对应 ID')
    buy_time = models.DateTimeField(default=datetime.now, verbose_name='购买时间', help_text='购买时间')
    buy_type = models.IntegerField(choices=BUY_TYPE, verbose_name='购买类型', help_text='是支付的记录还是收入的记录')
    use_currency = models.IntegerField(choices=CURRENCY, verbose_name='使用货币', help_text='是哪一种货币，充值币还是赠币')
    money = models.FloatField(default=0, verbose_name='金额', help_text='涉及金额')

    def __str__(self):
        return self.user.nickname

    class Meta:
        verbose_name = '交易记录'
        verbose_name_plural = verbose_name


class EmailVerifyCode(models.Model):

    SEND_TYPE = (
        ('register', '注册'),
        ('forger', ',忘记密码'),
    )

    code = models.CharField(max_length=6, verbose_name='验证码')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    send_type = models.CharField(max_length=10, choices=SEND_TYPE, verbose_name='发送类型')
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = '验证码'
        verbose_name_plural = verbose_name