import requests

from .models import VideoDetails

QUERY = 'game'


def get_api_data(API_KEY, url, videos_published_after):
    """
    Getting all the data from YouTube Data API using given parameters
    :param API_KEY:
    :param url:
    :param videos_published_after:
    :return: <List<Dictionary>>
    """
    params = {
        'part': 'snippet',
        'q': QUERY,
        'key': API_KEY,
        'type': 'video',
        'order': 'date',
        'publishedAfter': videos_published_after
    }

    data = requests.get(url, params)

    if 'error' in data.json():
        print(data.json()['error'])
        return

    results = data.json()['items']

    video_details = []

    for result in results:
        video = {
            'videoId': result['id']['videoId'],
            'title': result['snippet']['title'],
            'thumbnail_url': result['snippet']['thumbnails']['default']['url'],
            'publishedAt': result['snippet']['publishedAt'],
            'description': result['snippet']['description'],
        }

        video_details.append(video)

    return video_details


def get_videos(video_id):
    """
    :param video_id:
    :return: bool
    """
    video = VideoDetails.objects.filter(videoId=video_id)
    if video.exists():
        return True
    else:
        return False
