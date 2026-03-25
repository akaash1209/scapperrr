# Findings & Research

## Discovery Phase Answers
1. **North Star:** Build a beautiful interactive dashboard displaying the latest articles (last 24 hours) from various AI sources.
2. **Integrations:** Initial focus is building web scrapers for newsletters (Ben Bites, AI Rundown) and Reddit. Later phase will integrate Supabase for database and dashboard backend.
3. **Source of Truth:** The scraper will compile the data locally to start, which will eventually be hosted on the website and synced with Supabase.
4. **Delivery Payload:** An interactive UI dashboard presenting the collected daily articles.
5. **Behavioral Rules:** Build the scrapers first. Do not proceed to dashboard or Supabase integrations until the data scraping pipeline is robust.

## Scraping Targets
- Ben Bites (Newsletter)
- The AI Rundown (Newsletter)
- Reddit (AI Subreddits, exact targets TBD)

## Additional Design & Logic Constraints
- **Automation:** The system must run every 24 hours to fetch new data. Ignore if no new articles exist.
- **State Management:** Users must be able to "Save" articles. Saved articles must persist across page refreshes.
- **Priority Execution:** The user explicitly prioritized designing a "gorgeous and interactive-looking beautiful website" first.

## Phase 1 Research Findings
- **Newsletters (Ben Bites & AI Rundown):** Substack/Beehiiv newsletters provide deterministic RSS feeds (e.g., `bensbites.substack.com/feed`). Using the `feedparser` Python library will be the most reliable way to extract data (avoiding brittle HTML DOM scraping, perfectly aligning with B.L.A.S.T reliability goals). For parsing markdown/links, we can reference open-source approaches like `transitive-bullshit/bens-bites-ai-search`.
- **Reddit:** The industry standard is `PRAW` (Python Reddit API Wrapper). It requires `client_id`, `client_secret`, and `user_agent` credentials from a Reddit App. We will fetch recent posts using `subreddit.new(limit=N)`.
