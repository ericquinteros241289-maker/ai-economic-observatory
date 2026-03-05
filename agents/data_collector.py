import json
import os

def collect_news():

    news = [
        {
            "title": "Argentina inflation expectations rise",
            "content": "Economists expect inflation to remain high in Argentina due to fiscal adjustments."
        },
        {
            "title": "Global trade slows in 2026",
            "content": "World trade growth is expected to slow due to geopolitical tensions."
        },
        {
            "title": "China increases imports of soybeans",
            "content": "China increases soybean imports impacting Latin American exporters."
        }
    ]

    os.makedirs("data", exist_ok=True)

    with open("data/news.json", "w") as f:
        json.dump(news, f, indent=4)

    print("News collected successfully")
