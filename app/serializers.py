from rest_framework import serializers
from .models import posts

class postSerializer(serializers.ModelSerializer):
    class Meta:
        model = posts
        fields = '__all__'