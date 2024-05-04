from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    """
    Abstract Serializer
    """

    id = serializers.IntegerField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    modified_at = serializers.DateTimeField(read_only=True)

    class Meta:
        abstract = True
