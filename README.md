# genpark-content-calendar-skill

> **GenPark AI Agent Skill** -- Generate monthly marketing content calendars with post ideas, themes, hashtags, and scheduling for e-commerce brands.

## Features

- Full month-by-month content calendar generation
- 12 content types (Product Spotlight, UGC, Giveaway, etc.)
- Category-specific themes (beauty, fitness, fashion, food, tech)
- Monthly event tie-ins (Black Friday, Valentine's Day, etc.)
- Platform-optimized posting schedules (Instagram, TikTok, Pinterest, etc.)
- Hashtag sets per channel and category

## Quick Start

```python
from client import ContentCalendarClient

client = ContentCalendarClient()
result = client.generate(
    brand_name="MyBrand",
    product_category="beauty",
    channels=["instagram", "tiktok"],
    month=9, year=2026,
)
print(f"{result['total_posts_planned']} posts planned for {result['month']}")
for day in result["calendar"][:3]:
    for post in day["posts"]:
        print(f"{day['date']} [{post['channel']}]: {post['post_idea']}")
```

## Installation

```bash
python example_usage.py  # No external dependencies
```

---
Built by [GenPark](https://genpark.ai) | [alphaparkinc](https://github.com/alphaparkinc)
