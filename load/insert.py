from load.database import get_connection




def insert_video(video):


    conn = get_connection()

    cur = conn.cursor()



    try:


        cur.execute("""

        INSERT INTO videos(

            video_id,

            title,

            channel_id,

            views,

            likes,

            comments,

            like_ratio,

            comment_ratio,

            engagement_rate,

            trend_score,

            country

        )


        VALUES(

            %s,%s,%s,%s,%s,

            %s,%s,%s,%s,%s,%s

        )


        ON CONFLICT(video_id)

        DO UPDATE SET


        views = EXCLUDED.views,

        likes = EXCLUDED.likes,

        comments = EXCLUDED.comments,

        trend_score = EXCLUDED.trend_score,

        country = EXCLUDED.country


        """,

        (

        video["video_id"],

        video["title"],

        video["channel_id"],

        video["views"],

        video["likes"],

        video["comments"],

        video["like_ratio"],

        video["comment_ratio"],

        video["engagement_rate"],

        video["trend_score"],

        video["country"]

        ))



        conn.commit()


        return True



    except Exception as e:


        print(
            "Insert error:",
            e
        )


        conn.rollback()


        return False



    finally:


        cur.close()

        conn.close()