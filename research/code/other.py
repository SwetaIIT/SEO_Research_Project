import os
import requests
from bs4 import BeautifulSoup
import feedparser

# Output folder
OUTPUT_DIR = "research/blogs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

#  Example RSS feeds (SEO blogs)
BLOG_FEEDS = [
    "https://ahrefs.com/blog/feed/",
    "https://backlinko.com/feed",
]

def save_blog_post(title, content, index):
    file_path = f"{OUTPUT_DIR}/blog_{index}.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(title + "\n\n")
        f.write(content)
    print("Saved:", file_path)

def scrape_rss():
    index = 1

    for feed_url in BLOG_FEEDS:
        feed = feedparser.parse(feed_url)

        for entry in feed.entries[:3]:  # limit for assignment
            try:
                title = entry.title
                link = entry.link

                # fetch page content
                response = requests.get(link, timeout=10)
                soup = BeautifulSoup(response.text, "html.parser")

                paragraphs = soup.find_all("p")
                content = "\n".join([p.get_text() for p in paragraphs[:20]])

                save_blog_post(title, content, index)
                index += 1

            except Exception as e:
                print("Error:", e)

scrape_rss()
