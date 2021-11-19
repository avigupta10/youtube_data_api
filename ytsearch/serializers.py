from rest_framework import serializers

from .models import VideoDetails


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoDetails
        fields = (
            'videoId',
            'title',
            'description',
            'publishedAt',
            'thumbnail_url',
        )


