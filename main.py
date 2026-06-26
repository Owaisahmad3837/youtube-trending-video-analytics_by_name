from extract.trending_video import extract_trending_video
from extract.regions import extract_regions

from transform.video_metric import video_metrics

from load.database import clear_database
from load.insert import insert_video
from load.create_tables import create_tables



def main():


    print("ETL Started")


    # create database table

    create_tables()



    # remove old data

    clear_database()



    # get all countries

    countries = extract_regions()


    print(
        "Total Countries:",
        len(countries)
    )



    total_inserted = 0



    for country in countries:


        code = country["country_code"]

        name = country["country_name"]



        print(
            "\nCountry:",
            name,
            code
        )



        try:


            videos = extract_trending_video(code)



            print(
                "Trending videos:",
                len(videos)
            )



            for video in videos:



                # transform

                clean_video = video_metrics(video)



                # add country

                clean_video["country"] = code



                # insert database

                status = insert_video(
                    clean_video
                )



                if status:

                    total_inserted += 1



        except Exception as e:


            print(
                "Failed:",
                code,
                e
            )



    print(
        "\nTotal inserted:",
        total_inserted
    )


    print(
        "ETL Finished"
    )




if __name__ == "__main__":

    main()