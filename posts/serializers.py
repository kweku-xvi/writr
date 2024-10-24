from .models import Blog
from rest_framework import serializers


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'cover_image', 'content', 'created_at', 'updated_at']

        read_only_fields = ['id', 'created_at', 'updated_at']