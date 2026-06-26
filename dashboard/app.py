import sys
import os


# add project root path
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.insert(0, BASE_DIR)



import streamlit as st
import pandas as pd
import plotly.express as px


from load.database import get_connection

import streamlit as st
import pandas as pd
import plotly.express as px

from load.database import get_connection



# page config

st.set_page_config(

    page_title="YouTube World Analytics",

    layout="wide"

)



st.title("🌎 YouTube World Analytics Dashboard")



# database function

def get_data(query):

    conn = get_connection()


    df = pd.read_sql(

        query,

        conn

    )


    conn.close()


    return df




# =====================
# LOAD DATA
# =====================


videos = get_data("""

SELECT *

FROM videos

""")




# =====================
# TOP CARDS
# =====================


total_videos = len(videos)


total_views = videos["views"].sum()


total_likes = videos["likes"].sum()


total_comments = videos["comments"].sum()



c1,c2,c3,c4 = st.columns(4)



with c1:

    st.metric(

        "🎬 Videos",

        f"{total_videos:,}"

    )



with c2:

    st.metric(

        "👁 Views",

        f"{total_views:,}"

    )



with c3:

    st.metric(

        "👍 Likes",

        f"{total_likes:,}"

    )



with c4:

    st.metric(

        "💬 Comments",

        f"{total_comments:,}"

    )





# =====================
# TRENDING
# =====================


st.divider()


st.header("🔥 Global Trending Videos")



trending = videos.sort_values(

    "trend_score",

    ascending=False

).head(10)



st.dataframe(

    trending[

    [

    "title",

    "country",

    "views",

    "likes",

    "trend_score"

    ]

    ],

    use_container_width=True

)





# =====================
# TOP LIKES
# =====================


st.header("👍 Top Like Videos")



likes = videos.sort_values(

    "likes",

    ascending=False

).head(10)



st.dataframe(

    likes[

    [

    "title",

    "likes",

    "country"

    ]

    ],

    use_container_width=True

)






# =====================
# TOP COMMENTS
# =====================


st.header("💬 Top Comment Videos")



comments = videos.sort_values(

    "comments",

    ascending=False

).head(10)



st.dataframe(

    comments[

    [

    "title",

    "comments",

    "country"

    ]

    ],

    use_container_width=True

)





# =====================
# TOP VIEWS
# =====================


st.header("👁 Most Viewed Videos")



views = videos.sort_values(

    "views",

    ascending=False

).head(10)



st.dataframe(

    views[

    [

    "title",

    "views",

    "country"

    ]

    ],

    use_container_width=True

)





# =====================
# COUNTRY ANALYSIS
# =====================


st.divider()


st.header("🌎 Country Analysis")



country = (

videos

.groupby("country")

.size()

.reset_index(

name="videos"

)

)



fig = px.bar(

country,

x="country",

y="videos",

title="Videos by Country"

)



st.plotly_chart(

fig,

use_container_width=True

)






# =====================
# VIEWS VS LIKES
# =====================


st.header("📈 Views vs Likes")



fig2 = px.scatter(

videos.head(200),

x="views",

y="likes",

size="comments",

hover_name="title",

title="Engagement Analysis"

)



st.plotly_chart(

fig2,

use_container_width=True

)





# =====================
# SIDEBAR FILTER
# =====================


st.sidebar.header("Filter")


country_filter = st.sidebar.selectbox(

"Select Country",

["All"] +

list(videos["country"].unique())

)



if country_filter != "All":


    filtered = videos[

        videos["country"] == country_filter

    ]


    st.subheader(

        f"Videos in {country_filter}"

    )


    st.dataframe(

        filtered,

        use_container_width=True

    )