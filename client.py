"""
content-calendar-skill: Client SDK
Generate monthly marketing content calendars for e-commerce brands.
"""
from __future__ import annotations
import calendar
from datetime import date
from typing import Optional

CONTENT_TYPES = [
    "Product Spotlight", "Behind the Scenes", "Customer Testimonial",
    "Educational / How-To", "Trend Alert", "User Generated Content",
    "Flash Sale Announcement", "Brand Story", "Product Comparison",
    "Seasonal Content", "Poll / Question", "Giveaway / Contest",
]

CATEGORY_THEMES = {
    "beauty":   ["Glow Up Journey", "Clean Beauty", "Skincare Routine", "Ingredient Deep Dive", "Self-Care Sunday"],
    "fitness":  ["Transformation Tuesday", "Workout Wednesday", "Motivation Monday", "Nutrition Tips", "Rest and Recovery"],
    "fashion":  ["Outfit of the Day", "Style Guide", "Trend Forecast", "Capsule Wardrobe", "Sustainable Fashion"],
    "food":     ["Recipe of the Week", "Foodie Friday", "Ingredient Spotlight", "Meal Prep Monday", "Taste Test"],
    "tech":     ["Tech Tuesday", "Productivity Hacks", "Unboxing", "Feature Deep Dive", "User Review"],
    "default":  ["Product Feature", "Community Spotlight", "Expert Tips", "Customer Stories", "Behind the Brand"],
}

HASHTAG_SETS = {
    "beauty": {
        "instagram": "#skincare #beautyroutine #glowup #cleanbeauty #selfcare #skincareaddict #beautyproducts #naturalskincare",
        "tiktok": "#skincaretok #beautytok #glowup #skincareroutine #beautyreview",
        "pinterest": "#skincareroutine #beautytips #glowskin #naturalskincare #selfcareroutine",
    },
    "fitness": {
        "instagram": "#fitness #workout #gymlife #healthylifestyle #fitnessmotivation #gains #fitfam #bodybuilding",
        "tiktok": "#fitnesstok #workoutmotivation #gym #homeworkout #fitnessjourney",
        "pinterest": "#workout #fitnessgoals #healthyliving #exerciseroutine #fitnessinspiration",
    },
    "fashion": {
        "instagram": "#fashion #ootd #style #fashionista #streetstyle #wiwt #fashionblogger #outfitinspo",
        "tiktok": "#fashiontok #ootd #styletips #outfitideas #fashiontrends",
        "pinterest": "#fashioninspo #outfitideas #styleguide #capsulewardrobe #sustainablefashion",
    },
    "food": {
        "instagram": "#foodie #instafood #foodphotography #recipe #homecooking #foodlover #delicious #eeeeeats",
        "tiktok": "#foodtok #cookingtok #recipe #foodreview #homecooking",
        "pinterest": "#recipe #foodinspo #mealprep #homecooking #healthyrecipes",
    },
    "tech": {
        "instagram": "#tech #gadgets #technology #innovation #techreview #geek #techlife #productreview",
        "tiktok": "#techtok #gadgets #techreview #unboxing #newtech",
        "pinterest": "#techgadgets #productivitytools #techreview #innovations #gadgetlover",
    },
    "default": {
        "instagram": "#shopnow #newarrival #sale #brand #productlaunch #limited #exclusive #musthave",
        "tiktok": "#brandtok #newproduct #review #trending #fyp",
        "pinterest": "#newproduct #shopping #brandlove #productideas #gifts",
    },
}

POSTING_SCHEDULE = {
    "instagram": {"best_days": ["Tuesday", "Wednesday", "Friday"], "best_times": ["11:00 AM", "1:00 PM", "7:00 PM"]},
    "tiktok":    {"best_days": ["Tuesday", "Thursday", "Saturday"], "best_times": ["9:00 AM", "12:00 PM", "7:00 PM"]},
    "twitter":   {"best_days": ["Wednesday", "Thursday", "Friday"], "best_times": ["9:00 AM", "12:00 PM", "5:00 PM"]},
    "facebook":  {"best_days": ["Wednesday", "Thursday"], "best_times": ["1:00 PM", "3:00 PM"]},
    "pinterest": {"best_days": ["Saturday", "Sunday", "Monday"], "best_times": ["8:00 PM", "9:00 PM"]},
    "youtube":   {"best_days": ["Friday", "Saturday"], "best_times": ["12:00 PM", "3:00 PM"]},
}

MONTHLY_EVENTS = {
    1: ["New Year", "Winter Sale", "Dry Skin Awareness"],
    2: ["Valentine's Day", "Self-Love Month", "Winter Clearance"],
    3: ["Women's Day (Mar 8)", "Spring Launch", "Earth Hour"],
    4: ["Earth Day (Apr 22)", "Spring Sale", "Easter"],
    5: ["Mother's Day", "Mental Health Awareness", "Spring Collection"],
    6: ["Pride Month", "Father's Day", "Summer Launch"],
    7: ["Summer Sale", "Back to School Prep", "Mid-Year Review"],
    8: ["Back to School", "Summer Clearance", "Wellness Month"],
    9: ["Fall Launch", "Self-Care September", "Labor Day Sale"],
    10: ["Halloween", "Breast Cancer Awareness", "Fall Collection"],
    11: ["Black Friday", "Cyber Monday", "Movember", "Gratitude Week"],
    12: ["Holiday Season", "Christmas Sale", "Year-End Review", "New Year Prep"],
}


class ContentCalendarClient:
    """
    SDK for generating monthly marketing content calendars for e-commerce brands.
    """

    def generate(
        self,
        brand_name: str,
        product_category: str,
        channels: Optional[list[str]] = None,
        month: int = 1,
        year: int = 2026,
        posts_per_week: int = 3,
    ) -> dict:
        """
        Generate a full monthly content calendar.

        Args:
            brand_name:       Brand name.
            product_category: beauty / fitness / fashion / food / tech / default.
            channels:         Social platforms to schedule for.
            month:            Month (1-12).
            year:             Year.
            posts_per_week:   Target posts per week per channel.

        Returns:
            dict with calendar, themes, hashtag_sets, posting_schedule
        """
        channels = channels or ["instagram", "tiktok"]
        cat = product_category.lower()

        themes = CATEGORY_THEMES.get(cat, CATEGORY_THEMES["default"])
        events = MONTHLY_EVENTS.get(month, [])

        # Get all days in the month
        _, days_in_month = calendar.monthrange(year, month)
        month_name = calendar.month_name[month]

        cal_entries = []
        post_idx = 0
        content_type_idx = 0

        for day in range(1, days_in_month + 1):
            d = date(year, month, day)
            weekday = d.strftime("%A")

            # Determine if posting today
            # Post on days matching the channel schedule
            day_entries = []
            for ch in channels:
                sched = POSTING_SCHEDULE.get(ch, POSTING_SCHEDULE["instagram"])
                if weekday in sched["best_days"] and post_idx % max(1, 7 // posts_per_week) < len(channels):
                    content_type = CONTENT_TYPES[content_type_idx % len(CONTENT_TYPES)]
                    theme = themes[post_idx % len(themes)]
                    event_ref = events[post_idx % len(events)] if events else ""

                    # Generate post idea
                    idea = self._generate_idea(brand_name, content_type, theme, event_ref, cat)
                    day_entries.append({
                        "channel": ch,
                        "content_type": content_type,
                        "theme": theme,
                        "post_idea": idea,
                        "posting_time": sched["best_times"][post_idx % len(sched["best_times"])],
                        "event_tie_in": event_ref,
                    })
                    content_type_idx += 1

            if day_entries:
                cal_entries.append({
                    "date": str(d),
                    "day": weekday,
                    "posts": day_entries,
                })
                post_idx += 1

        hashtags = {
            ch: HASHTAG_SETS.get(cat, HASHTAG_SETS["default"]).get(ch, "")
            for ch in channels
        }

        schedule = {ch: POSTING_SCHEDULE.get(ch, POSTING_SCHEDULE["instagram"]) for ch in channels}

        return {
            "brand": brand_name,
            "month": month_name,
            "year": year,
            "product_category": product_category,
            "channels": channels,
            "total_posts_planned": sum(len(e["posts"]) for e in cal_entries),
            "monthly_events": events,
            "themes": themes,
            "calendar": cal_entries,
            "hashtag_sets": hashtags,
            "posting_schedule": schedule,
        }

    @staticmethod
    def _generate_idea(brand: str, content_type: str, theme: str, event: str, cat: str) -> str:
        event_suffix = f" | Tie-in: {event}" if event else ""
        templates = {
            "Product Spotlight": f"Highlight your best-selling {cat} product. Show before/after or key benefit.{event_suffix}",
            "Behind the Scenes": f"Show how {brand} creates/sources its products. Authenticity builds trust.{event_suffix}",
            "Customer Testimonial": f"Feature a real customer review or transformation story.{event_suffix}",
            "Educational / How-To": f"Share a {cat} tip, tutorial, or routine your audience can apply today.{event_suffix}",
            "Trend Alert": f"Comment on a trending {cat} topic and tie it back to {brand}.{event_suffix}",
            "User Generated Content": f"Repost a customer photo using your product. Ask for permission first.{event_suffix}",
            "Flash Sale Announcement": f"Tease or launch a limited-time {brand} promotion.{event_suffix}",
            "Brand Story": f"Share the mission and values behind {brand}. Why do you exist?{event_suffix}",
            "Product Comparison": f"Compare your product to the category norm. Highlight your advantage.{event_suffix}",
            "Seasonal Content": f"Connect {brand} to the current season or upcoming holiday.{event_suffix}",
            "Poll / Question": f"Ask your audience a question about their {cat} preferences or challenges.{event_suffix}",
            "Giveaway / Contest": f"Run a {brand} giveaway. Ask followers to tag a friend or share a post.{event_suffix}",
        }
        return templates.get(content_type, f"{content_type} post for {brand} ({theme}){event_suffix}")
