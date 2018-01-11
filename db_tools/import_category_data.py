import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wechatRead.settings_dev")

import django
django.setup()

from books.models import Category

from data.category_data import row_data


for category in row_data:
    c = Category()
    c.name = category['name']
    c.category_type = 1
    c.save()

    for sub_cate in category['sub_cat']:
        sub_c = Category()
        sub_c.name = sub_cate['name']
        sub_c.category_type = 2
        sub_c.parent_category = c
        sub_c.save()
