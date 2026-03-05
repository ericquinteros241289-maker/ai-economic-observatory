import json
import os

def collect_news():

    news = [
        {
            "title": "Argentina inflation expectations rise",
            "content": "Economists expect inflation to remain high in Argentina."
        },
        {
            "title": "Global trade slows",
            "content": "World trade growth slows due to geopolitical tensions."
        }
    ]

    os.makedirs("data", exist_ok=True)

    with open("data/news.json", "w") as f:
        json.dump(news, f, indent=4)

    print("News collected")
