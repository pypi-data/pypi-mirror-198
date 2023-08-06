import re
import traceback

from yt_scrape.exceptions import TooManyRequests, NoVideoFound

from yt_scrape.utils import get_content, data_dict


def youtube_results(keyword):
    kw = "+".join(keyword.split())
    url = f"https://www.youtube.com/results?search_query={kw}"
    html = get_content(url)
    obj = data_dict(html)
    if not obj:
        raise TooManyRequests("Please wait 1 or 2 seconds")

    links = []
    links_json = obj["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"][
        "sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"]
    for l in links_json:
        if "videoRenderer" in l.keys():
            data = {"vid_id": "", "thumbnail": "", "title": "", "publish_time": "", "vid_length": "", "views": "",
                    "channel_url": "", "channel_name": ""}
            video_data = l["videoRenderer"]
            try:
                thumbnail = video_data["thumbnail"]["thumbnails"][0]["url"]
                title = video_data["title"]["runs"][0]["text"]
                publish_time = video_data["publishedTimeText"]["simpleText"]
                vid_length = video_data["lengthText"]["simpleText"]
                views = video_data["viewCountText"]["simpleText"]
                vid_id = video_data["videoId"]
                channel_url = video_data["longBylineText"]['runs'][0]['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url']
                channel_name = video_data["longBylineText"]['runs'][0]["text"]

                data.update({
                    "thumbnail": thumbnail,
                    "title": title,
                    "publish_time": publish_time,
                    "vid_length": vid_length,
                    "views": views,
                    "vid_id": vid_id,
                    "channel_url": channel_url,
                    "channel_name": channel_name
                })
            except KeyError:
                pass
            links.append(data)

    return links


def channels_videos(channel_id):
    url = f"https://www.youtube.com/{channel_id}/videos"
    html = get_content(url)
    obj = data_dict(html)
    if not obj:
        raise TooManyRequests("Please wait 1 or 2 seconds")
    videos = []
    try:
        links_json = obj.get("contents")
        content2 = links_json.get("twoColumnBrowseResultsRenderer")
        if content2:
            tabs = content2.get("tabs")
            for tab in tabs:
                if "tabRenderer" in tab:
                    contents = tab.get("tabRenderer").get("content")
                    if contents:
                        if contents.get("richGridRenderer"):
                            video_items = contents.get("richGridRenderer").get("contents")
                            if video_items:
                                for vid in video_items:
                                    vid_id, thumbnail, title, description_snippet, length, view_count, publish_time = [None] * 7
                                    try:
                                        c = vid["richItemRenderer"]["content"]["videoRenderer"]
                                        vid_id = c["videoId"]
                                        thumbnail = c["thumbnail"]["thumbnails"][-1]["url"]
                                        title = c["title"]["runs"][0]["text"]
                                        description_snippet = c["descriptionSnippet"]["runs"][0]["text"]
                                        length = c["lengthText"]["simpleText"]
                                        view_count = c["viewCountText"]["simpleText"]
                                        publish_time = c["publishedTimeText"]["simpleText"]

                                    except KeyError as e:
                                        pass

                                    data = {"vid_id": vid_id, "thumbnail": thumbnail, "title": title,
                                                "description_snippet": description_snippet, "length": length,
                                                "publish_time": publish_time, "view_count": view_count}
                                    if any(data.values()):
                                        videos.append(data)

                    else:
                        continue

    except TypeError as e:
        tb = traceback.format_exc()
        line = re.findall(r"(line \d+)", tb)
        print(f"Error: {e} at {line[0]}")

    except KeyError as e:
        tb = traceback.format_exc()
        line = re.findall(r"(line \d+)", tb)
        print(f"Error: {e} at {line[0]}")

    if videos:
        return videos
    else:
        raise NoVideoFound("videos not found!")

def channels_about(channel_id):
    url = f"https://www.youtube.com/{channel_id}/about"
    html = get_content(url)
    obj = data_dict(html)
    if not obj:
        raise TooManyRequests("Please wait 1 or 2 seconds")

    details = {"channel_name": "", "views_count": "", "channel_thumbnail": "", "channel_url": "", "description": "",
               "banner": "", "channel_id": "", "videos_count": "", "subscribers": "", "joined": "", "country": ""}
    try:
        channel_name_thumbnail = obj["microformat"]["microformatDataRenderer"]
        channel_url_description = obj["metadata"]["channelMetadataRenderer"]
        upper_section_data = obj["header"]["c4TabbedHeaderRenderer"]

        channel_name = channel_name_thumbnail["title"]
        details["channel_name"] = channel_name

        channel_thumbnail = channel_name_thumbnail["thumbnail"]["thumbnails"][0]["url"]
        details["channel_thumbnail"] = channel_thumbnail

        channel_url = channel_url_description["ownerUrls"][0]
        details["channel_url"] = channel_url

        description = channel_url_description["description"]
        details["description"] = description

        banner = upper_section_data["banner"]["thumbnails"][0]["url"]
        details["banner"] = banner

        channel_id = upper_section_data["channelId"]
        details["channel_id"] = channel_id

        subscribers = upper_section_data["subscriberCountText"]["simpleText"]
        details["subscribers"] = subscribers

        videos_count = upper_section_data["videosCountText"]["runs"][0]["text"]
        details["videos_count"] = videos_count

    except (KeyError, ValueError) as e:
        tb = traceback.format_exc()
        line = re.findall(r"(line \d+)", tb)
        print(f"{e} at {line[0]}")
        pass

    try:
        tabs = obj.get("contents").get("twoColumnBrowseResultsRenderer").get("tabs")
        if tabs:
            for tab in tabs:
                if tab.get("tabRenderer") and tab.get("tabRenderer").get("content"):
                    content = tab.get("tabRenderer").get("content").get("sectionListRenderer").get("contents")[0]["itemSectionRenderer"]["contents"][0]

                    joined_data_list = content["channelAboutFullMetadataRenderer"]["joinedDateText"]["runs"]
                    joined = " ".join([i["text"] for i in joined_data_list]) if isinstance(joined_data_list, list) else None
                    details["joined"] = joined

                    views_count = content["channelAboutFullMetadataRenderer"]["viewCountText"]["simpleText"]
                    details["views_count"] = views_count
                    country = content["channelAboutFullMetadataRenderer"]["country"]["simpleText"]
                    details["country"] = country

    except (KeyError, ValueError) as e:
        tb = traceback.format_exc()
        line = re.findall(r"(line \d+)", tb)
        print(f"{e} at {line[0]}")
        pass

    if any(details.values()):
        return details
    else:
        return {}
