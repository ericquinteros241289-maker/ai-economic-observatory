def detect_trends(articles):

    trends = []

    for article in articles:

        title = article["title"]

        trend = f"Potential economic trend detected: {title}"

        trends.append(trend)

    return trends
