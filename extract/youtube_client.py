from googleapiclient.discovery import build
from config.config import youtube_api


def get_youtube_client():

 youtube =build(
   "youtube",
   "v3",
   developerKey=youtube_api
 )
 return youtube
