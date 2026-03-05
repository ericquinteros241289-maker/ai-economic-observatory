from agents.data_collector import collect_news
from agents.summarizer import summarize_news

def main():

    print("Collecting news...")
    collect_news()

    print("Summarizing news...")
    summarize_news()

    print("Pipeline completed.")

if __name__ == "__main__":
    main()
        run: python pipeline/run_daily_pipeline.py
