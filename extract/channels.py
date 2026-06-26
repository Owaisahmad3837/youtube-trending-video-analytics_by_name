from extract.youtube_client import get_youtube_client


youtube=get_youtube_client()

def extract_channels(channel_id):
  response=youtube.videos().list(
    part="snippet,statistics",
    id=",".join(channel_id)
  ).execute()

  return response["items"]