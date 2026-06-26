from youtube_client import youtube


def extract_comments(video_id):
    response = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100
    ).execute()

    return response["items"]