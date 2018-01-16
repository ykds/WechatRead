from rest_framework import serializers
from datetime import datetime, timedelta

from .models import Follow, UserProfile, EmailVerifyCode


class FollowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follow
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    followed = FollowSerializer(many=True)
    following = FollowSerializer(many=True)


class VerifyCodeSerializer(serializers.Serializer):

    email = serializers.EmailField(max_length=50)

    def validate_email(self, email):

        if UserProfile.objects.filter(email=email):
            raise serializers.ValidationError('用户已存在')

        one_minute_age = datetime.now() - timedelta(minutes=1)
        if EmailVerifyCode.objects.filter(add_time__gt=one_minute_age, email=email):
            raise serializers.ValidationError('距离上一次发送未超过60s')

        return email


