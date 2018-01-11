import django_filters
from django.db.models import Q

from .models import Book


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