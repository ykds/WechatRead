import django_filters

from .models import Follow, UserProfile

class FollowFilter(django_filters.rest_framework.FilterSet):

    followed = django_filters.NumberFilter(method='followed_filter')
    following = django_filters.NumberFilter(method='following_filter')

    def followed_filter(self, queryset, name, value):
        return queryset.filter(following__id=value)

    def following_filter(self, queryset, name, value):
        return queryset.filter(followed__id=value)

    class Meta:
        model = Follow
        fields = ['followed', 'following']