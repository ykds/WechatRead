import django_filters

from .models import Follow, UserProfile

class FollowFilter(django_filters.rest_framework.FilterSet):

    followed = django_filters.NumberFilter(method='followed_filter', help_text='传入某个用户的ID, 搜索出关注这个用户的所有用户')
    following = django_filters.NumberFilter(method='following_filter', help_text='传入某个用户的ID, 搜索出这个用户关注的所有用户')

    def followed_filter(self, queryset, name, value):
        return queryset.filter(following__id=value)

    def following_filter(self, queryset, name, value):
        return queryset.filter(followed__id=value)

    class Meta:
        model = Follow
        fields = ['followed', 'following']
