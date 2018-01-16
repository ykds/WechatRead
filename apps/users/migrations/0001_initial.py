# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-14 14:55
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nickname', models.CharField(max_length=15, verbose_name='昵称')),
                ('email', models.EmailField(blank=True, default='', max_length=254, verbose_name='邮箱')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], max_length=6, verbose_name='性别')),
                ('introduce', models.TextField(blank=True, default='', max_length=100, null=True, verbose_name='自我介绍')),
                ('image', models.ImageField(upload_to='users/images', verbose_name='头像')),
                ('motto', models.CharField(blank=True, max_length=20, null=True, verbose_name='我的签名')),
                ('province', models.CharField(max_length=25, verbose_name='省份')),
                ('city', models.CharField(max_length=15, verbose_name='城市')),
                ('read_time', models.FloatField(default=0, verbose_name='阅读时间')),
                ('likes', models.IntegerField(default=0, verbose_name='点赞数')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField(default=0, verbose_name='余额')),
                ('present', models.FloatField(default=0, verbose_name='赠币')),
                ('recharge', models.FloatField(default=0, verbose_name='充值币')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户账户',
                'verbose_name_plural': '用户账户',
            },
        ),
        migrations.CreateModel(
            name='DealLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='购买时间')),
                ('buy_type', models.IntegerField(choices=[(1, '支付'), (2, '收入')], verbose_name='购买类型')),
                ('use_currency', models.IntegerField(choices=[(1, '充值币'), (2, '赠币')], verbose_name='使用货币')),
                ('money', models.FloatField(default=0, verbose_name='金额')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book', verbose_name='图书')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Chapter', verbose_name='章节')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '交易记录',
                'verbose_name_plural': '交易记录',
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='关注时间')),
                ('followed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed', to=settings.AUTH_USER_MODEL, verbose_name='被关注者')),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL, verbose_name='关注者')),
            ],
            options={
                'verbose_name': '关注',
                'verbose_name_plural': '关注',
            },
        ),
        migrations.CreateModel(
            name='Purchased',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='购买时间')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book', verbose_name='图书')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Chapter', verbose_name='章节')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '已购内容',
                'verbose_name_plural': '已购内容',
            },
        ),
    ]
