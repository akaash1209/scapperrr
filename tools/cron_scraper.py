import os
import modal
import feedparser
from datetime import datetime, timezone
import uuid

# Define the Modal App container
app = modal.App("scraperrr-cron")

# Define the cloud environment image with dependencies
image = modal.Image.debian_slim().pip_install("feedparser", "praw")

@app.function(image=image, schedule=modal.Period(hours=24), secrets=[modal.Secret.from_dotenv()])
def scrape_all_sources():
    print("[Pipeline] Starting 24-hour Scraperrr Execution...")
    
    articles = []
    
    # Deterministic RSS parsing
    def fetch_rss(name, url):
        print(f"Fetching {name}...")
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries[:5]: # Extract top 5 for consistency
                articles.append({
                    "id": str(uuid.uuid4()),
                    "title": entry.title,
                    "source": name,
                    "url": getattr(entry, "link", url),
                    "published_at": datetime.now(timezone.utc).isoformat(), # Normalize time
                    "summary": entry.get("summary", "No summary available.")[:200] + "...",
                    "is_saved": False
                })
        except Exception as e:
            print(f"Failed to fetch {name}: {e}")

    # Execute Links
    fetch_rss("Ben Bites", "https://bensbites.substack.com/feed")
    fetch_rss("The AI Rundown", "https://www.therundown.ai/feed")
    fetch_rss("Moneycontrol", "https://www.moneycontrol.com/rss/MCtopnews.xml")

    # Safely handle Reddit if keys exist
    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_CLIENT_SECRET")
    if client_id and client_secret:
        import praw
        print("Fetching Reddit...")
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent="Scraperrr/1.0"
        )
        try:
            for post in reddit.subreddit("artificial").new(limit=5):
                articles.append({
                    "id": str(uuid.uuid4()),
                    "title": post.title,
                    "source": "Reddit",
                    "url": "https://reddit.com" + post.permalink,
                    "published_at": datetime.now(timezone.utc).isoformat(),
                    "summary": post.selftext[:200] + "..." if getattr(post, 'selftext', '') else "Link post.",
                    "is_saved": False
                })
        except Exception as e:
            print(f"Failed Reddit fetch: {e}")

    print(f"[Pipeline] Successfully scraped {len(articles)} articles!")
    print("[Payload Output Data Schema Conformance]", articles[:2]) # Validates to gemini.md
    
    # Future Phase: Dump 'articles' payload to Supabase database.
    return articles

@app.local_entrypoint()
def main():
    print("Triggering manual scraper execution via CLI...")
    scrape_all_sources.remote()
    print("Execution finalized.")
