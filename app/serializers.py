# serializers.py
from rest_framework import serializers
from .models import posts

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = posts
        fields = ['id', 'title', 'description', 'image']
