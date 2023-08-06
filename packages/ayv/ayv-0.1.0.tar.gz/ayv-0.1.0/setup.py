from setuptools import find_packages, setup

# For consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

VERSION = '0.1.0' 
DESCRIPTION = 'A library to use with the YouTube API. With it you can manage and analyze YouTube resources (Videos, Channels, Playlists, Broadcasts e.t.c) from python scripts.'

setup(
    name='ayv',
    packages=find_packages(
        include=[
            'youtube', 
            'youtube.youtube_resources',
            'youtube.youtube_resources.youtube_channel',
            'youtube.youtube_resources.youtube_comment',
            'youtube.youtube_resources.youtube_comment_thread',
            'youtube.youtube_resources.youtube_playlist',
            'youtube.youtube_resources.youtube_video',
            'youtube.youtube_resources.youtube_video_category',
            'youtube.oauth',
            'youtube.search',
            'youtube.search.category',
            'youtube.search.channel',
            'youtube.search.playlist',
            'youtube.search.video'
        ]
        ),
    version=VERSION,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    url="https://youtube.readthedocs.io/",
    author='Lyle Okoth',
    author_email='lyceokoth@gmail.com',
    license='MIT',
    install_requires=['google-api-python-client', 'google-auth-oauthlib'],
    keywords=['python', 'youtube', 'youtube api', 'youtube comments'],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
)