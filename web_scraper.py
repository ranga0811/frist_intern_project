# Basic Web Scraper
# Basic Web Scraper

import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

# Send request to the website
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find news headlines
headlines = soup.find_all("span", class_="titleline")

print("========== NEWS HEADLINES ==========")

for i, headline in enumerate(headlines, start=1):
    print(i, ".", headline.get_text(strip=True))