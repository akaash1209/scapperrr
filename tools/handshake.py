import os
import requests
import feedparser
from dotenv import load_dotenv

load_dotenv()

def verify_rss(name, url):
    print(f"[{name}] Verifying RSS connection to {url}...")
    try:
        feed = feedparser.parse(url)
        if feed.entries:
            print(f"  ✓ SUCCESS: Retrieved {len(feed.entries)} entries.")
            print(f"  ✓ Latest: {feed.entries[0].title}")
            return True
        else:
            print("  ! WARNING: No entries found or feed invalid.")
            return False
    except Exception as e:
        print(f"  X ERROR: Failed to parse feed. {e}")
        return False

def verify_reddit():
    print("[Reddit] Checking PRAW credentials in .env...")
    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_CLIENT_SECRET")
    
    if not client_id or not client_secret:
        print("  ! WARNING: Reddit credentials missing from .env. Skipping Reddit handshake.")
        return False
        
    try:
        import praw
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=os.getenv("REDDIT_USER_AGENT", "Scraperrr/1.0")
        )
        # Attempt to read a subreddit
        subs = list(reddit.subreddit("artificial").new(limit=1))
        print(f"  ✓ SUCCESS: Reddit API authenticated. Latest 'artificial' post: {subs[0].title}")
        return True
    except Exception as e:
        print(f"  X ERROR: Reddit handshake failed. {e}")
        return False

def verify_modal():
    print("[Modal] Checking credentials in .env...")
    token_id = os.getenv("MODAL_TOKEN_ID")
    token_secret = os.getenv("MODAL_TOKEN_SECRET")
    if token_id and token_secret:
        print("  ✓ SUCCESS: Modal credentials are secure in `.env`.")
        print("  ✓ CI/CD Bypasser: We will deploy to Modal using GitHub Actions (Python 3.11 environment) to bypass the local Windows Py3.13 crash.")
        return True
    else:
        print("  X ERROR: Modal credentials not found in env.")
        return False

if __name__ == "__main__":
    print("-" * 50)
    print("Phase 2: Link (Connectivity/Handshake Verification)")
    print("-" * 50)
    
    verify_modal()
    print("")
    verify_rss("Ben Bites", "https://bensbites.substack.com/feed")
    verify_rss("The AI Rundown", "https://www.therundown.ai/feed")
    verify_rss("Moneycontrol AI", "https://www.moneycontrol.com/rss/MCtopnews.xml") # Using Top News for verification currently
    print("")
    verify_reddit()
    
    print("-" * 50)
    print("Handshake process complete.")
