from rest_framework import serializers

from app.core.base_serializer import BaseSerializer


class UserSerializer(BaseSerializer):
    """
    user info serializer
    """

    user_name = serializers.CharField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    current_state = serializers.CharField()
    avatar = serializers.ImageField()
    description = serializers.CharField()
    mobile = serializers.CharField()
    email = serializers.EmailField()
    is_staff = serializers.BooleanField()
    is_active = serializers.BooleanField()
    date_joined = serializers.DateTimeField()


class TaskSerializer(BaseSerializer):
    name = serializers.CharField(read_only=True)
    state = serializers.CharField()
    due_date = serializers.DateTimeField()
