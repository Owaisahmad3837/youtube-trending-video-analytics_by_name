from extract.youtube_client import get_youtube_client



youtube=get_youtube_client()
def extract_regions():


  response=youtube.i18nRegions().list(
    part="snippet"
  ).execute()

  countries=[]


  for item in response["items"]:
    country={
      "country_code": item["id"],
      "country_name": item["snippet"]["name"]

    }
    countries.append(country)


  return countries