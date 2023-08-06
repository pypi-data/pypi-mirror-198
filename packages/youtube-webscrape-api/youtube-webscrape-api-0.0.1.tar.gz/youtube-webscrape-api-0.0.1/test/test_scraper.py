import time
import pytest
from yt_scrape import channels_videos, channels_about, youtube_results
from yt_scrape.exceptions import TooManyRequests

channel_names = [i.strip() for i in open("test_data/channel_names.txt", 'r').readlines()]
search_keywords = [i.strip() for i in open("test_data/search_keywords.txt", 'r').readlines()]

@pytest.mark.parametrize("channel_id", channel_names)
def test_channels_videos(channel_id):
    try:
        details = channels_videos(channel_id)
        assert len(details) > 1

    except TooManyRequests:
        time.sleep(2)

@pytest.mark.parametrize("channel_id", channel_names)
def test_channels_about(channel_id):
    try:
        details = channels_about(channel_id)
        assert any(list(details.values()))

    except TooManyRequests:
        time.sleep(2)


@pytest.mark.parametrize("keyword", search_keywords)
def test_youtube_results(keyword):
    assert len(youtube_results(keyword)) > 10

