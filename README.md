# youtube_data_api

A Django Rest Framework Application 

## Application 
### There is mainly 1 resource:
- VideoDetails

## API Actions:
- A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
- A basic search API to search the stored videos using their title and description.

## Available APIs
### Get data from YouTube Data API

### ```GET https://www.googleapis.com/youtube/v3/search ```

#### List all the data from youtube using 'q'(query)
```
parameters:

params = {
        'part': 'snippet',
        'q': 'game',
        'key': API_KEY,
        'type': 'video',
        'order': 'date',
        'publishedAfter': <Any date>
    }
 Response:
{
  "kind": "youtube#searchListResponse",
  "etag": "WKjFtcCM2J4jkF_JwYmEjIWNALo",
  "nextPageToken": "CAEQAA",
  "regionCode": "IN",
  "pageInfo": {
    "totalResults": 1000000,
    "resultsPerPage": 1
  },
  "items": [
    {
      "kind": "youtube#searchResult",
      "etag": "EdKm-F90qJXgx4u8AR1ItVnXUnk",
      "id": {
        "kind": "youtube#video",
        "videoId": "_XCnOFZTxFE"
      },
      "snippet": {
        "publishedAt": "2021-11-19T10:04:13Z",
        "channelId": "UCjv4s7xmkWL4WBFZ3b6Pp6A",
        "title": "Poppy Playtime: HUGGY vs Squid Game Magnet - Stop Motion ASMR Scary Teacher 3D Among Us Animation",
        "description": "Welcome to Magnetic Food, We...
",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/_XCnOFZTxFE/default_live.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/_XCnOFZTxFE/mqdefault_live.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/_XCnOFZTxFE/hqdefault_live.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Magnetic Food",
        "liveBroadcastContent": "live",
        "publishTime": "2021-11-19T10:04:13Z"
      }
    }
  ]
}
```

### ```GET /api/get-videos ```
#### List all the stored videos
Response:

```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

Response:
{
    "count": 5,
    "next": "http://127.0.0.1:8000/api/get-videos?page=2",
    "previous": null,
    "results": [
        {
            "videoId": "WPGbHm2mHRo",
            "title": "Steph Curry Is Playing Career-Best Basketball | NBA Fantasy Basketball Game Recaps | November 18",
            "description": "Josh Lloyd looks back at Thursday's NBA Games, discussing the big performances and surprises, Steph Curry's surge towards another MVP, a detailed look at ...",
            "publishedAt": "2021-11-19T05:07:32Z",
            "thumbnail_url": "https://i.ytimg.com/vi/WPGbHm2mHRo/default_live.jpg"
        },
        {
            "videoId": "wVITmKho_K8",
            "title": "RAPTORS at JAZZ | FULL GAME HIGHLIGHTS | November 18, 2021",
            "description": "Stream More Live Games With NBA LEAGUE PASS: https://app.link.nba.com/e/subscribe_now Subscribe to the NBA: https://on.nba.com/2JX5gSN The Utah ...",
            "publishedAt": "2021-11-19T04:24:35Z",
            "thumbnail_url": "https://i.ytimg.com/vi/wVITmKho_K8/default.jpg"
        },
        {
            "videoId": "B7fsYF_8G7M",
            "title": "THIS MINECRAFT DROPPER MADE CHOP RAGE QUIT THE GAME",
            "description": "THIS MINECRAFT DROPPER MADE CHOP RAGE QUIT THE GAME Subscribe to 3rd (BGMI) Channel: https://bit.ly/3Br2XAD In Today's video Chop and Frosty ...",
            "publishedAt": "2021-11-19T03:45:01Z",
            "thumbnail_url": "https://i.ytimg.com/vi/B7fsYF_8G7M/default.jpg"
        }
    ]
}
```

### Here i implemented 2 ways to search our database

## Search By Query Params
### ```GET /api/search?desc=NBA&title=MVP```
#### Search API

Query params:
```desc``` 
```title```
```
Response:
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "videoId": "WPGbHm2mHRo",
            "title": "Steph Curry Is Playing Career-Best Basketball | NBA Fantasy Basketball Game Recaps | November 18",
            "description": "Josh Lloyd looks back at Thursday's NBA Games, discussing the big performances and surprises, Steph Curry's surge towards another MVP, a detailed look at ...",
            "publishedAt": "2021-11-19T05:07:32Z",
            "thumbnail_url": "https://i.ytimg.com/vi/WPGbHm2mHRo/default_live.jpg"
        },
        {
            "videoId": "174z9crutVM",
            "title": "Golden State Warriors vs. Cleveland Cavaliers Full Game Highlights | NBA Season 2021-22",
            "description": "Golden State Warriors vs. Cleveland Cavaliers Full Game Highlights | NBA Season 2021-22.",
            "publishedAt": "2021-11-19T03:42:08Z",
            "thumbnail_url": "https://i.ytimg.com/vi/174z9crutVM/default.jpg"
        }
    ]
}
```

### A similar API is made with ```django-filter``` and can be accessed with ```/api/search?{QUERY}```

# ASYC BEHAVIOR

#### Here i am using ```django-background-tasks``` to continuously send requests to YouTube Data API after every 10sec and store all the data in ```database``` in the backgroud.


## Setup Instructions

### Clone this repo

`git clone https://github.com/avigupta10/youtube_data_api.git`

### Create Virtual Environment and Install Required Python Modules
`cd youtube_data_api`

Install venv
`pip install virtualenv`

For Creating a venv run this 
`virtualenv -p python3 venv`

Activate virtualenv 
`venv\Scripts\activate`

Install requirements
```bash
pip install -r requirements.txt
```
### Start Web Server

To start the web server you need to run the following sequence of commands.

Run the django web server.
```bash
python manage.py runserver
```

### Start Background Tasks
Open a new terminal and head to the same path of you project and activate your virtual environment. Next , type in
```bash
python manage.py process_tasks
```
Thats it you're done
