from django.db.models import Q

from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter

from background_task import background

from youtube_data_api import settings
from .models import VideoDetails
from .serializers import VideoSerializer
from .utils import get_api_data, get_videos

SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'

VIDEOS_PUBLISHED_AFTER = '2021-11-10T11:49:10Z'


@background()
def store_details():
    """
    Storing all the data we get from YouTube Data API to Django Model
    :param request:
    :return:
    """
    print('running')
    received_data = get_api_data(settings.YOUTUBE_DATA_API_KEY, SEARCH_URL, VIDEOS_PUBLISHED_AFTER)
    if received_data:

        for data in received_data:

            video = get_videos(data.get('videoId'))

            if not video:
                videos = VideoDetails(
                    videoId=data['videoId'],
                    title=data['title'],
                    description=data['description'],
                    publishedAt=data['publishedAt'],
                    thumbnail_url=data['thumbnail_url']
                )
                videos.save()


@api_view(['GET'])
def api_details(request):
    """
    :param request:
    :return:
    """
    details = {
        'GET - Video Details': 'http://127.0.0.1:8000/api/get-videos',
        'GET - Search': 'http://127.0.0.1:8000/api/search?desc=&title=',
    }
    return Response(details)


class GetVideoDetails(ListAPIView):
    queryset = VideoDetails.objects.order_by('-publishedAt')
    serializer_class = VideoSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'description')


class SearchVideoByQueryParams(ListAPIView):
    serializer_class = VideoSerializer

    def get_queryset(self):
        """
        Searching model with Q lookup
        :return:
        """
        try:
            queryset = VideoDetails.objects.all()
            title = self.request.query_params.get('title')
            desc = self.request.query_params.get('desc')
            if title is not None or desc is not None:
                title_queryset = queryset.filter(Q(title__icontains=title))
                desc_queryset = queryset.filter(Q(title__icontains=desc))

                queryset = title_queryset | desc_queryset
                return queryset
        except:
            return Response({'error':'Please provide Title as well as Description'})


