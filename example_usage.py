"""
example_usage.py -- Demonstrates the ContentCalendarClient SDK.
"""
from client import ContentCalendarClient

def main():
    client = ContentCalendarClient()

    print("[Content Calendar Generator]")
    result = client.generate(
        brand_name="GlowBeauty",
        product_category="beauty",
        channels=["instagram", "tiktok"],
        month=8,
        year=2026,
        posts_per_week=4,
    )
    print(f"Brand: {result['brand']} | Month: {result['month']} {result['year']}")
    print(f"Channels: {result['channels']} | Total Posts Planned: {result['total_posts_planned']}")
    print(f"Monthly Events: {result['monthly_events']}")
    print(f"Content Themes: {result['themes']}")
    print(f"\nFirst 5 scheduled days:")
    for entry in result["calendar"][:5]:
        print(f"\n  {entry['date']} ({entry['day']})")
        for post in entry["posts"]:
            print(f"    [{post['channel'].upper()}] {post['posting_time']} | {post['content_type']}")
            print(f"    Idea: {post['post_idea'][:80]}...")
    print(f"\nHashtags:")
    for ch, tags in result["hashtag_sets"].items():
        print(f"  {ch}: {tags[:60]}...")
    print(f"\nBest Posting Times:")
    for ch, sched in result["posting_schedule"].items():
        print(f"  {ch}: {sched['best_days']} at {sched['best_times']}")

if __name__ == "__main__":
    main()
