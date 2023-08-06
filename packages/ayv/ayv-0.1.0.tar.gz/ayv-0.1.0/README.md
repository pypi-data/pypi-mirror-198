# youtube

> A python library for working with the YouTube API. Enables the user to find YouTube Videos, Channels and Playlists.

## Installation
```sh
pip install youtube
```

## Get started

To get started, you a verified Google Account and Google API keys. Follow this [tutorial]() that details the process of getting the API keys as well as enabling the neccssary services and authorizing a test account for use with the library.

To find videos matching a particular serach query like *Python programming videos*, import the library, then provide it with the path to the credentials file that you downloaded from Google:
```sh
from youtube import YouTube

credentials_file = '/home/user/Downloads/credentials.json'
token_path = '/home/user'
youtube = Youtube(credentials_file, token_path)
```

Then call the ```search_videos``` method on the youtube object with the query.

```sh
python_programming_videos = youtube.search_videos('python programming videos')
```

To find the most popular Kenyan YouTube Videos:
```sh
most_popular_us_videos = youtube.find_most_popular_videos_by_region('ke')
```
