from rest_framework import serializers

from app.core.base_serializer import BaseSerializer


class ContainCommentSerializer(BaseSerializer):
    category = serializers.CharField()
    text = serializers.CharField()
