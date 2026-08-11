import csv 
import sys
import requests 
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding="utf-8")

with open ('books_data.csv','w',newline='',encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['Title','Price','Availability'])
    print("🚀 Book Scraping Started...\n")
    for page in range(1,6):
        url= (f'https://books.toscrape.com/catalogue/page-{page}.html')
        response= requests.get(url)
        response.encoding='utf-8'
        if response.status_code== 200 : 
            soup = BeautifulSoup(response.text,'html.parser')
            books= soup.find_all('article', class_='product_pod')
            for book in books:
                title=book.find('h3').find('a')['title']
                price=book.find('p',class_='price_color').text
                availability=book.find('p',class_='instock availability').text.strip()
                writer.writerow([title,price,availability])
            print(f"✅ Page {page} scraped successfully!")
        else:
            print(
                f"❌ Failed to load Page {page} (Status: {response.status_code})"
            )
print("\n🎉 All Done! Data saved in 'books_data.csv'")
            
            
