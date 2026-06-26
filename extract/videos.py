from extract.youtube_client import get_youtube_client


youtube=get_youtube_client()

def extract_videos(video_id):
  response=youtube.videos().list(
    part="snippet,statistics",
    id=",".join(video_id)
  ).execute()

  return response["items"]