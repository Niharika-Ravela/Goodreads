# scraper.py
import feedparser
import re

# Your Goodreads RSS (the one you supplied)
GOODREADS_RSS = "https://www.goodreads.com/review/list_rss/190787349?key=mKAJqu4LcWuZ39ved3Zl6TSeR96ttPxU9tTZKccx1InXPVWG&shelf=surprise-random"

def clean_title_author(raw_title):
    if not raw_title:
        return ("", "")
    raw = re.sub(r"<[^>]+>", "", raw_title).strip()
    parts = re.split(r'\s+by\s+', raw, flags=re.IGNORECASE)
    if len(parts) >= 2:
        title = parts[0].strip()
        author = parts[1].strip()
        author = re.sub(r'\s+\d.*$', '', author).strip()
        return (title, author)
    return (raw, "")

def fetch_books_from_rss():
    feed = feedparser.parse(GOODREADS_RSS)
    books = []
    seen = set()
    for entry in feed.entries:
        raw = entry.get("title") or entry.get("summary") or entry.get("description") or ""
        title, author = clean_title_author(raw)
        if not title:
            continue
        key = (title.lower(), author.lower())
        if key in seen:
            continue
        seen.add(key)
        books.append({"title": title, "author": author})
    return books

if __name__ == "__main__":
    b = fetch_books_from_rss()
    print(f"Found {len(b)} books")
    for i,item in enumerate(b[:30], start=1):
        print(i, item)
