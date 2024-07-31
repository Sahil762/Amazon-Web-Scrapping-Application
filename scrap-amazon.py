import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


url = 'https://www.amazon.in/s?k=shoes'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Successfully fetched the webpage")
else:
    print(f"Failed to fetch webpage. Status code: {response.status_code}")
    exit()

soup = BeautifulSoup(response.content, 'html.parser')


products = []
for item in soup.find_all('div', {'data-component-type': 's-search-result'}):
    try:
        name = item.find('span', class_='a-text-normal').text.strip()
    except AttributeError:
        name = 'N/A'
        
    try:
        price_whole = item.find('span', class_='a-price-whole')
        price_symbol = item.find('span', class_='a-price-symbol')
        if price_whole and price_symbol:
            price = price_whole.text.strip() + price_symbol.text.strip()
        else:
            price = 'N/A'
    except AttributeError:
        price = 'N/A'
        
    try:
        link = 'https://www.amazon.in' + item.find('a', class_='a-link-normal')['href']
    except (AttributeError, TypeError):
        link = 'N/A'
    
    products.append({
        'Name': name,
        'Price': price,
        'Link': link
    })


df = pd.DataFrame(products)


try:
    df.to_excel('amazon_shoes_data.xlsx', index=False)
    print("Data saved to amazon_shoes_data.xlsx")
except Exception as e:
    print(f"Failed to save data to Excel: {e}")
