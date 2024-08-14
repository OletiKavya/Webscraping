import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = 'https://finance.yahoo.com/quote/AAPL?p=AAPL'

# Make a request to fetch the HTML content
response = requests.get(url)
html_content = response.text

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find the stock price
price_div = soup.find('div', {'class': 'price'})
price = price_div.find('span').text

print(f'Current stock price of Apple Inc. (AAPL): ${price}')
