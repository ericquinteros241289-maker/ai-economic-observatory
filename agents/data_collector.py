import requests

def collect_news():

    url = "https://newsapi.org/v2/top-headlines?category=business&language=en&pageSize=10&apiKey=demo"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data["articles"]

    return []
