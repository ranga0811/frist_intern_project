import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("h3")

print("========== BOOK TITLES ==========")

for i, book in enumerate(books, start=1):
    print(i, ".", book.get_text(strip=True))