from books.models import Chapter, Category, CollectionBook, Book, BookMark

import xadmin


class CategoryAdmin:
    list_display = ['name']


class BookAdmin:
    list_display = ['name', 'author', 'category', 'word_count', 'copyright', 'rank', 'price', 'read_count',
                    'is_new', 'is_index', 'is_end']
    search_fields = ['author', 'name', 'category']
    list_filter = ['author', 'category', 'rank', 'is_new', 'is_index', 'is_end']
    list_editable = ['is_new', 'is_index', 'is_end']
    readonly_fileds = ['read_count']


class ChapterAdmin:
    list_display = ['name', 'index', 'book', 'word_count', 'price']


class BookMarkAdmin:
    list_display = ['user', 'book', 'index']
    list_filter = ['user', 'book']


class CollectionBookAdmin:
    list_display = ['book', 'user', 'start_read_time', 'is_finish']
    list_editable = ['is_finish']
    list_filter = ['book', 'user']


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Chapter, ChapterAdmin)
xadmin.site.register(CollectionBook, CollectionBookAdmin)
xadmin.site.register(BookMark, BookAdmin)
xadmin.site.register(Book, BookAdmin)
