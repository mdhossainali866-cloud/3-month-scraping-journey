import requests
import sys 
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
url = "https://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
quote_box=soup.find_all('div',class_='quote')

print("=== 🚀 WEEK 1 PROJECT: QUOTES & TAGS SCRAPER ===\n")

for box in quote_box:
    quote = box.find('span', class_='text').text
    author = box.find('small', class_='author').text
    tags =', '.join([tag.text for tag in box.find_all('a', class_='tag')])
    print(f'quote   :{quote}')
    print(f"Author  : {author}")
    print(f"Tags    : {tags}")
    print("-" * 60)
    
