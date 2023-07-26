import os

from googleapiclient.discovery import build

api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=self.channel_id
                                               ).execute()['items'][0]
        # ['items'][0]
        # printj(video_response)
        self.video_title: str = video_response['snippet']['title']
        self.view_count: int = video_response['statistics']['viewCount']
        self.like_count: int = video_response['statistics']['likeCount']
        self.comment_count: int = video_response['statistics']['commentCount']

# class Channel_1:
#     """Класс для ютуб-канала"""
#
#     def __init__(self, channel_id: str, name_channel: str, discription_channel: str, link_channel: str,
#                  quantity_user: int, quantity_video: int, quantity_watch: int) -> None:
#         self.channel_id = channel_id
#         self.name_channel = name_channel
#         self.discription_channel = discription_channel
#         self.link_channel = link_channel
#         self.quantity_user = quantity_user
#         self.quantity_video = quantity_video
#         self.quantity_watch = quantity_watch
#
#
# @classmethod
# def get_service():
#     pass
#
#
# def to_json():
#     json_str = 'asd'
#     json_obj = json.loads(json_str)
#
#     with open('homework.json', 'w') as file:
#         json.dump(json_obj, file, indent=2)
