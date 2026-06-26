def transform_channel(channel):

    data = {}


    data["channel_id"] = channel["id"]


    data["channel_name"] = (
        channel["snippet"]["title"]
    )


    stats = channel["statistics"]


    data["subscribers"] = int(
        stats.get(
            "subscriberCount",
            0
        )
    )


    data["total_views"] = int(
        stats.get(
            "viewCount",
            0
        )
    )


    data["video_count"] = int(
        stats.get(
            "videoCount",
            0
        )
    )


    return data