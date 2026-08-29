import csv
from datetime import datetime
import sys
import time
from bs4 import BeautifulSoup
import requests

sys.stdout.reconfigure(encoding="utf-8")


def get_hacker_news():
    news_list = []
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    response = requests.get(url)
    story_ids = response.json()[:10]

    for story_id in story_ids:
        item_url = (
            f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        )
        data = requests.get(item_url).json()
        news = {
            "Title": data.get("title", "N/A"),
            "URL": data.get("url", "N/A"),
            "Points": data.get("score", 0),
        }
        news_list.append(news)
        time.sleep(0.1)
    return news_list


def get_dev_to():
    dev_list = []
    url = "https://dev.to/"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            " (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    cards = soup.find_all("div", class_="crayons-story", limit=10)

    for card in cards:
        title_tag = card.find("h2", class_="crayons-story__title")
        if title_tag and title_tag.find("a"):
            title = title_tag.find("a").text.strip()
            raw_link = title_tag.find("a")["href"]

            if not raw_link.startswith("http"):
                link = "https://dev.to" + raw_link
            else:
                link = raw_link
        else:
            title, link = "N/A", "N/A"

        dev_list.append(
            {"Title": title, "URL": link, "Points": "Dev.to Article"}
        )

    return dev_list


def save_to_csv(data):
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"tech_news_{today}.csv"
    headers = ["Title", "URL", "Points"]

    with open(filename, mode="w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

    print(f"\n🎉 Saved {len(data)} items to {filename} successfully!")


if __name__ == "__main__":
    hn_data = get_hacker_news()
    dev_data = get_dev_to()

    all_news = hn_data + dev_data

    print(f"Total News Collected: {len(all_news)}")
    save_to_csv(all_news)