# Scraperrr Automation SOP

## Goal
Extract top AI articles from defined sources every 24 hours deterministically.

## Logic & Edge Cases
- **Layer 2 Navigation:** Modal's native scheduling handles the 24-hour loop seamlessly (`modal.Period(hours=24)`). This acts as our decision engine block.
- **RSS Stability Strategy:** We use direct HTTP RSS parsing (via `feedparser`). This completely bypasses DOM Structure Scraping, minimizing runtime errors when frontend structures change.
- **Fail-Safes:** Broad `except` blocks prevent a failure in the Ben Bites feed from killing the Moneycontrol output payload. 
- **Dependencies:** `feedparser` and `praw` must be injected into the underlying Modal `debian_slim` cloud image explicitly via `.pip_install("feedparser")` before execution.

## The Payloads
Follows `gemini.md` Global JSON schema strictly.
Currently dumps mapped JSON objects to Modal serverless logs as a proof-of-concept pending Database (Supabase) assignment and frontend webhook bridging.
