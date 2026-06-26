from extract.trending_video import extract_trending_video
from extract.regions import extract_regions
from transform.video_metric import video_metrics
from load.database import clear_database
from load.insert import insert_video




def main():


    print("ETL Started")



    # remove old data

    clear_database()



    # get all countries

    countries = extract_regions()


    print(
        "Countries:",
        len(countries)
    )



    # loop countries

    for country in countries:


        code = country["country_code"]


        name = country["country_name"]


        print(
            "Processing:",
            name,
            code
        )



        try:


            videos = extract_trending_video(code)



            print(
                "Videos:",
                len(videos)
            )



            for video in videos:


                clean_video = video_metrics(video)


                # add country information

                clean_video["country"] = code



                insert_video(clean_video)



        except Exception as e:


            print(
                "Error:",
                code,
                e
            )



    print(
        "ETL Finished"
    )




if __name__ == "__main__":

    main()