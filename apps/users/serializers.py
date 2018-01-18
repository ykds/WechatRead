from datetime import datetime, timedelta

from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Follow, UserProfile, EmailVerifyCode, Account, Purchased, DealLog


class FollowUserDetailSerializer(serializers.ModelSerializer):

    """
    返回关注信息时序列化部分用户信息
    """

    class Meta:
        model = UserProfile
        fields = ['id', 'nickname', 'gender', 'image', 'province', 'city']


class FollowedSerializer(serializers.ModelSerializer):

    """序列化关注我的人的信息"""

    followed_user = FollowUserDetailSerializer(source='followed', read_only=True)

    class Meta:
        model = Follow
        fields = ['followed', 'followed_user', 'follow_time']


class FollowingSerializer(serializers.ModelSerializer):

    """
    序列化我关注的人的信息
    """

    following_user = FollowUserDetailSerializer(source='following', read_only=True)

    class Meta:
        model = Follow
        fields = ['following', 'following_user', 'follow_time']


class UserRegisterSerializer(serializers.ModelSerializer):

    """
    用户注册时验证用户提交的信息
    """

    code = serializers.CharField(required=True, min_length=6, max_length=6, write_only=True, help_text='验证码')
    email = serializers.EmailField(required=True, label='邮箱', validators=[UniqueValidator(
        queryset=UserProfile.objects.all(), message='邮箱已存在 ')], help_text='邮箱')
    password = serializers.CharField(style={'input_type': 'password'}, label='密码', help_text='密码', write_only=True)

    def validate_code(self, code):

        record_code = EmailVerifyCode.objects.filter(email=self.initial_data['email'], code=code)
        if record_code:
            record_code = record_code[0]
            one_hour_age = datetime.now() - timedelta(hours=1)
            if record_code.add_time < one_hour_age:
                raise serializers.ValidationError('验证码过期')

            if record_code.code != code:
                raise serializers.ValidationError('验证码错误')
        else:
            raise serializers.ValidationError('验证码错误')

    def validate(self, attrs):
        attrs['username'] = attrs['email']
        attrs['nickname'] = attrs['email']
        attrs['password'] = make_password(attrs['password'])
        del attrs['code']
        return attrs

    class Meta:
        model = UserProfile
        fields = ['code', 'email', 'password']


class UserDetailSerializer(serializers.ModelSerializer):

    """
    序列化用户的详细信息
    """

    class Meta:
        model = UserProfile
        fields = ['nickname', 'email', 'gender', 'introduce', 'image', 'motto', 'province', 'city', 'read_time',
                  'likes']


class VerifyCodeSerializer(serializers.Serializer):

    """
    请求验证码时验证邮箱
    """

    email = serializers.EmailField(max_length=50)

    def validate_email(self, email):

        if UserProfile.objects.filter(email=email):
            raise serializers.ValidationError('用户已存在')

        one_minute_age = datetime.now() - timedelta(minutes=1)
        if EmailVerifyCode.objects.filter(add_time__gt=one_minute_age, email=email):
            raise serializers.ValidationError('距离上一次发送未超过60s')

        return email



