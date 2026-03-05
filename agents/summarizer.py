import json

def summarize_news(input_file="data/news.json", output_file="data/summaries.json"):
    
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            articles = json.load(f)
    except FileNotFoundError:
        print("No news file found.")
        return

    summaries = []

    for article in articles:

        title = article.get("title", "")
        description = article.get("description", "")
        content = article.get("content", "")

        # resumen simple
        summary = (description or content or "")[:200]

        summaries.append({
            "title": title,
            "summary": summary,
            "source": article.get("source", ""),
            "url": article.get("url", "")
        })

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(summaries, f, indent=2, ensure_ascii=False)

    print(f"{len(summaries)} articles summarized.")
