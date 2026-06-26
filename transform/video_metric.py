def video_metrics(video):


    data = {}


    data["video_id"] = video["id"]


    data["title"] = (
        video["snippet"]["title"]
    )


    data["channel_id"] = (
        video["snippet"]["channelId"]
    )


    stats = video.get(
        "statistics",
        {}
    )


    views = int(
        stats.get("viewCount",0)
    )


    likes = int(
        stats.get("likeCount",0)
    )


    comments = int(
        stats.get("commentCount",0)
    )



    data["views"] = views

    data["likes"] = likes

    data["comments"] = comments



    # metrics

    if views > 0:


        like_ratio = likes / views


        comment_ratio = comments / views


        engagement_rate = (
            likes + comments
        ) / views


    else:


        like_ratio = 0

        comment_ratio = 0

        engagement_rate = 0



    data["like_ratio"] = like_ratio

    data["comment_ratio"] = comment_ratio

    data["engagement_rate"] = engagement_rate



    # IMPORTANT

    data["trend_score"] = (

        engagement_rate * 70

        +

        like_ratio * 30

    )



    return data