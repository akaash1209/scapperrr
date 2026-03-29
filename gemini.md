# Data Schema & Maintenance Log

## Global Data Schema

### `Article` Payload
```json
{
  "articles": [
    {
      "id": "string (UUID)",
      "title": "string",
      "source": "string (e.g., 'Ben Bites', 'The AI Rundown', 'Reddit')",
      "url": "string (Source URL)",
      "published_at": "string (ISO-8601 timestamp)",
      "summary": "string (Brief description or extracted text)",
      "is_saved": "boolean (Default: false)"
    }
  ]
}
```

## Maintenance Log
- **Automation Trigger:** Modal.com serverless cron triggers function `scrape_all_sources()` every 24 hours natively.
- **Deployment Protocol:** Automatic branch pushes to `main` trigger GitHub Actions. The Action safely spins up Python 3.11, validates `feedparser`, and pushes to Modal securely.
- **Repo Health Keys:** Requires `MODAL_TOKEN_ID`, `MODAL_TOKEN_SECRET` mapped seamlessly via Repository Secrets.
