import django_filters
from django.db.models import Q

from .models import Book, Chapter, BookMark


class BookFilter(django_filters.rest_framework.FilterSet):

    category = django_filters.CharFilter(method='category_filter')
    min_rank = django_filters.NumberFilter(name='rank', lookup_expr='gte')
    max_rank = django_filters.NumberFilter(name='rank', lookup_expr='lte')
    min_price = django_filters.NumberFilter(name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(name='price', lookup_expr='lte')
    new = django_filters.BooleanFilter(name='is_new')
    end = django_filters.BooleanFilter(name='is_end')
    index = django_filters.BooleanFilter(name='is_index')
    author = django_filters.CharFilter(name='author', lookup_expr='contains')

    def category_filter(self, queryset, name ,value):
        return queryset.filter(Q(category__name__icontains=value) | Q(category__parent_category__name__icontains=value))

    class Meta:
        model = Book
        fields = ['min_rank', 'max_rank', 'min_price', 'max_price', 'new', 'index', 'end']


class ChapterFilter(django_filters.rest_framework.FilterSet):

    """
    按顺序进行过滤
    """
    book = django_filters.CharFilter(method='book_filter')
    start = django_filters.NumberFilter(method='start_filter')
    count = django_filters.NumberFilter(method='count_filter')

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

    user = django_filters.CharFilter(method='user_filter')
    book = django_filters.CharFilter(method='book_filter')

    def user_filter(self, queryset, name, value):
        return queryset.filter(user__id=value)

    def book_filter(self, queryset, name, value):
        return queryset.filter(book__name__icontains=value)

    class Meta:
        model = BookMark
        fields = ['user', 'book']