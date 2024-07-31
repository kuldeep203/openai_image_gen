from rest_framework import serializers
from image_generator.models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("id", "prompt", "image_url", "task_id", "created_at")
