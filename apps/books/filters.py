import django_filters
from django.db.models import Q

from .models import Book, Chapter, BookMark


class BookFilter(django_filters.rest_framework.FilterSet):

    category = django_filters.CharFilter(method='category_filter', help_text='图书的类别')
    min_rank = django_filters.NumberFilter(name='rank', lookup_expr='gte', help_text='最小评分')
    max_rank = django_filters.NumberFilter(name='rank', lookup_expr='lte', help_text='最大评分')
    min_price = django_filters.NumberFilter(name='price', lookup_expr='gte', help_text='最小价格')
    max_price = django_filters.NumberFilter(name='price', lookup_expr='lte', help_text='最大价格')
    new = django_filters.BooleanFilter(name='is_new', help_text='设置值为3时选出新书')
    end = django_filters.BooleanFilter(name='is_end', help_text='设置值为3时选出完结的书')
    index = django_filters.BooleanFilter(name='is_index', help_text='设置值为3时选出在书城首页显示的书')
    author = django_filters.CharFilter(name='author', lookup_expr='contains', help_text='图书的作者')

    def category_filter(self, queryset, name ,value):
        return queryset.filter(Q(category__name__icontains=value) | Q(category__parent_category__name__icontains=value))

    class Meta:
        model = Book
        fields = ['min_rank', 'max_rank', 'min_price', 'max_price', 'new', 'index', 'end']


class ChapterFilter(django_filters.rest_framework.FilterSet):

    """
    按顺序进行过滤
    """
    book = django_filters.CharFilter(method='book_filter', help_text='图书的 ID')
    start = django_filters.NumberFilter(method='start_filter', help_text='从哪个章节开始加载，传章节号（1，2，3···）')
    count = django_filters.NumberFilter(method='count_filter', help_text='加载多少个章节')

    def count_filter(self, queryset, name, value):
        return queryset.all()[:value]

    def start_filter(self, queryset, name, value):
        return queryset.filter(index__gte=value)

    def book_filter(self, queryset, name, value):
        return queryset.filter(book__name__icontains=value)

    class Meta:
        model = Chapter
        fields = ['book', 'start', 'count']


class BookMarkFilter(django_filters.rest_framework.FilterSet):

    user = django_filters.CharFilter(method='user_filter', help_text='用户对应 ID')
    book = django_filters.CharFilter(method='book_filter', help_text='图书对应 ID')

    def user_filter(self, queryset, name, value):
        return queryset.filter(user__id=value)

    def book_filter(self, queryset, name, value):
        return queryset.filter(book__name__icontains=value)

    class Meta:
        model = BookMark
        fields = ['user', 'book']