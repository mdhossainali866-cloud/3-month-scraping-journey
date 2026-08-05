import requests
import sys 
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
url = "https://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")




first_quote = soup.find("span", class_="text").text

print("Scraped Quote :")
print(first_quote)
