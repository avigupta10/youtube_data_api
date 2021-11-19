from django.urls import path
from .views import store_details, GetVideoDetails, SearchVideoByQueryParams, api_details

urlpatterns = [
    path('', api_details),
    path('get-videos', GetVideoDetails.as_view()),
    path('search', SearchVideoByQueryParams.as_view()),
]

# running store_details task in background after every 10sec and stops never
store_details(repeat=10, repeat_until=None)
