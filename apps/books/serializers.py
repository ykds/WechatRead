from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Category, Chapter, CollectionBook, Book, BookMark


class CategorySerializer2(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """
    类别
    """

    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = Category
        fields = '__all__'


class ChapterSerializer(serializers.ModelSerializer):
    """
    章节
    """
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = Chapter
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Chapter.objects.all(),
                fields = ('name', 'book'),
                message='已存在'
            )
        ]


class BookSerializer(serializers.ModelSerializer):
    """
    图书
    """
    category = serializers.CharField(read_only=True)

    chapters = ChapterSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Book.objects.all(),
                fields = ('name', 'author'),
                message='已存在'
            )
        ]





class BookMarkSerializer(serializers.ModelSerializer):
    """
    书签
    """

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    book_name = serializers.CharField(source='book.name', read_only=True)

    class Meta:
        model = BookMark
        fields = ['id', 'book', 'book_name', 'desc', 'index', 'user']


class CollectionBookSerializer(serializers.ModelSerializer):
    """
    藏书
    """

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    book_name = serializers.CharField(source='book.name', read_only=True)

    start_read_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    read_time = serializers.FloatField(read_only=True)

    class Meta:
        model = CollectionBook
        fields = ['id', 'book', 'book_name', 'start_read_time', 'read_time', 'is_finish', 'user']
        validators = [
            UniqueTogetherValidator(
                queryset=CollectionBook.objects.all(),
                fields = ('book', 'user'),
                message='已存在'
            )
        ]
