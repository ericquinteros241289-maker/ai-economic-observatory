[import json

def summarize_news():
    with open("data/news.json", "r") as f:
        articles = json.load(f)

    summaries = []

    for article in articles:
        summaries.append({
            "title": article["title"],
            "summary": article["title"][:120]
        })

    with open("data/summaries.json", "w") as f:
        json.dump(summaries, f, indent=2)
