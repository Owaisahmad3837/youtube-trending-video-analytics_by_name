from config.config import database_api
import psycopg2 

def get_connection():
  conn=psycopg2.connect(
    database_api
  )

  return conn


def clear_database():

  conn=get_connection()
  cur=conn.cursor()
  cur.execute(
        "DELETE FROM videos"
    )


  conn.commit()


  cur.close()

  conn.close()