from django.db import models


class VideoDetails(models.Model):
    videoId = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    description = models.TextField()
    publishedAt = models.DateTimeField(auto_now_add=False)
    thumbnail_url = models.URLField()

    def __str__(self):
        return self.title
