from rest_framework import serializers

from .models import Category, Chapter, CollectionBook, Book, BookMark


class CategorySerializer(serializers.ModelSerializer):
    """
    类别
    """
    class Meta:
        model = Category
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    """
    图书
    """

    class Meta:
        model = Book
        fields = '__all__'


class ChapterSerializer(serializers.ModelSerializer):
    """
    章节
    """
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = Chapter
        fields = '__all__'


class BookMarkSerializer(serializers.ModelSerializer):
    """
    书签
    """

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = BookMark
        fields = '__all__'


class CollectionBookSerializer(serializers.ModelSerializer):
    """
    藏书
    """

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = CollectionBook
        fields = '__all__'
