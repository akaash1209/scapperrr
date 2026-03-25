# Data Schema & Maintenance Log

## Global Data Schema

### `Article` Payload
This is the core JSON structure representing scraped articles from Ben Bites, The AI Rundown, and Reddit.

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
(Pending trigger and deployment)
