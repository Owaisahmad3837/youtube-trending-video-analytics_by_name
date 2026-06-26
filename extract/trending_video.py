from extract.youtube_client import get_youtube_client


youtube=get_youtube_client()

def extract_trending_video(country_code):
  response=youtube.videos().list(
    part="snippet,statistics",
    chart="mostPopular",
    regionCode=country_code,
    maxResults=50
  ).execute()

  return response["items"]
