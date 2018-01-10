import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wechatRead.settings_dev")

import django
django.setup()


from books.models import Book, Category

from data.book_data import row_data


for book in row_data:
    b = Book()
    b.name = book['name']
    b.author = book['author']
    b.cover = book['cover']
    b.brief = book['brief']
    b.word_count = book['word_count']
    b.copyright = book['copyright']
    b.rank = book['rank']
    b.price = book['price']
    b.read_count = book['read_count']
    b.is_end = book['is_end']
    b.is_index = book['is_index']
    b.is_new = book['is_new']

    category = Category.objects.filter(name=book['category'])
    if category:
        category = category[0]
        b.category = category
    b.save()