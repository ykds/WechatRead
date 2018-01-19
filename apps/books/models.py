from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Category(models.Model):
    """
    图书分类
    """

    CATEGORY_TYPE = (
        (1, '一级类别'),
        (2, '二级类别')
    )

    name = models.CharField(max_length=15, verbose_name='类别', unique=True)
    category_type = models.IntegerField(choices=CATEGORY_TYPE, null=True, blank=True, verbose_name='类别级别')
    parent_category = models.ForeignKey('self', related_name='sub_cat', verbose_name='子类别', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '图书类别'
        verbose_name_plural = verbose_name


class Book(models.Model):
    """
    公共图书
    """
    name = models.CharField(max_length=15, verbose_name='图书名称')
    author = models.CharField(max_length=20, verbose_name='作者')
    cover = models.ImageField(upload_to='books/cover',  blank=True, max_length=100, verbose_name='图书封面')
    category = models.ForeignKey(Category, related_name='books', default='', verbose_name='类别')
    brief = models.TextField(default='', blank=True, verbose_name='图书简介')
    word_count = models.IntegerField(default=0, verbose_name='总字数')
    copyright = models.CharField(max_length=100, blank=True, verbose_name='版权信息')
    rank = models.FloatField(default=0, blank=True, verbose_name='评分')
    price = models.FloatField(default=0, verbose_name='价格')
    read_count = models.IntegerField(default=0, blank=True, verbose_name='阅读人数')
    is_new = models.BooleanField(default=False, verbose_name='是否新书')
    is_index = models.BooleanField(default=False, verbose_name='是否在首页显示')
    is_end = models.BooleanField(default=False, verbose_name='是否完结')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '公共图书'
        verbose_name_plural = verbose_name


class Chapter(models.Model):
    """
    图书章节
    """
    name = models.CharField(max_length=30, verbose_name='章节名')
    index = models.IntegerField(verbose_name='章节号')
    book = models.ForeignKey(Book, related_name='chapters', verbose_name='从属图书')
    content = models.TextField(verbose_name='内容')
    word_count = models.IntegerField(default=0, verbose_name='字数')
    price = models.FloatField(default=0, verbose_name='价格')
    #is_free = models.BooleanField(default=False, verbose_name='是否免费')
    update_time = models.DateTimeField(default=datetime.now, verbose_name='更新时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name


class BookMark(models.Model):
    """
    书签
    """

    User = get_user_model()

    user = models.ForeignKey(User, related_name='my_bookmarks', verbose_name='用户', help_text='用户对应的 ID')
    book = models.ForeignKey(Book, related_name='bookmarks', verbose_name='图书', help_text='图书对应的 ID')
    #chapter = models.ForeignKey(Chapter, )
    desc = models.TextField(verbose_name='截取文本', help_text='截取文本，以这段文本定位')
    index = models.IntegerField(default=0, verbose_name='字符位置', help_text='字符位置')

    def __str__(self):
        return self.book.name

    class Meta:
        verbose_name = '书签'
        verbose_name_plural = verbose_name


class CollectionBook(models.Model):
    """
    藏书
    """
    # 因为user中引用了books中的一些模型，如果在全局声明会导致循环导入，所以把User的引用放在这里延迟导入
    User = get_user_model()

    book = models.OneToOneField(Book, verbose_name='图书', help_text='图书对应 ID')
    user = models.ForeignKey(User, related_name='my_books')
    read_time = models.FloatField(default=0, verbose_name='阅读时长')
    start_read_time = models.DateTimeField(default=datetime.now, verbose_name='开始阅读时间')
    is_finish = models.BooleanField(default=False, verbose_name='是否读完', help_text='是否读完')

    def __str__(self):
        return self.book.name

    class Meta:
        verbose_name = '藏书'
        verbose_name_plural = verbose_name


