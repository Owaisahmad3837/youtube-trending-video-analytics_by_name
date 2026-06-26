from load.database import get_connection



def create_tables():


    conn = get_connection()

    cur = conn.cursor()



    cur.execute("""

    CREATE TABLE IF NOT EXISTS videos(

        video_id TEXT PRIMARY KEY,

        title TEXT,

        channel_id TEXT,

        views BIGINT,

        likes BIGINT,

        comments BIGINT,

        like_ratio FLOAT,

        comment_ratio FLOAT,

        engagement_rate FLOAT,

        trend_score FLOAT,

        country TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )

    """)



    conn.commit()


    cur.close()

    conn.close()


    print("Table created")



if __name__ == "__main__":

    create_tables()