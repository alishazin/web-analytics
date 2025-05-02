import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://quotes.toscrape.com/"

# Send HTTP request to the URL
response = requests.get(url)

# Parse the content with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find all quote blocks
quotes = soup.find_all("div", class_="quote")

# Extract author name and bio link
for quote in quotes:
    author = quote.find("small", class_="author").text
    text = quote.find("span", class_="text").text
    print(f"Author: {author}")
    print(f"Quote: {text}")
    print("-" * 40)
