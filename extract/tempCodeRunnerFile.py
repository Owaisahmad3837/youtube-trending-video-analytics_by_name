from extract.youtube_client import get_youtube_client


def extract_trending_video(country_code):

    youtube = get_youtube_client()


    response = youtube.videos().list(

        part="snippet,statistics",

        chart="mostPopular",

        regionCode=country_code,

        maxResults=50

    ).execute()


    return response["items"]



if __name__ == "__main__":

    trending = extract_trending_video("PK")


    for video in trending:

        print(
            video["snippet"]["title"],
            video["snippet"]["likes"]
        )