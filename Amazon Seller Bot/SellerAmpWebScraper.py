import requests
from bs4 import BeautifulSoup

# Start a session
session = requests.Session()

# Login page URL
login_page_url = 'https://sas.selleramp.com/site/login'

# Get the login page
response = session.get(login_page_url)

# Parse the response to extract CSRF token
soup = BeautifulSoup(response.text, 'html.parser')
csrf_token = soup.find('input', {'name': '_csrf-sasend'})['value']

# Login URL for the POST request
login_url = 'https://sas.selleramp.com/site/login?src='

# Login credentials and form data
login_data = {
    '_csrf-sasend': csrf_token,
    'LoginForm[email]': '',
    'LoginForm[password]': '',
    'LoginForm[rememberMe]': '1'
}

# Send a POST request to the login URL
response = session.post(login_url, data=login_data)

# Check if login was successful
if 'https://sas.selleramp.com/' in response.url:
    print("Login successful")
else:
    print("Login failed")


# import libraries
import time
import datetime
import pandas as pd
import csv
import datetime

from SellerAmpLogin import session

# Connect to Website

URL = 'https://sas.selleramp.com/sas/lookup?SasLookup%5Bsearch_term%5D=https%3A%2F%2Fwww.amazon.com%2Fs%3Fi%3Dmerchant-items%26me%3DA1E9FT1UFOTH9W%26s%3Ddate-desc-rank%26marketplaceID%3DATVPDKIKX0DER%26qid%3D1701616861%26ref%3Dsr_st_date-desc-rank%26ds%3Dv1%253AGzn1vwAGjtH%252BTwKii4ODl1iaZypL38ff7cXuD0%252FCiMw'


# Use the session to get the page content
page = session.get(URL)


soup = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup.prettify(), "html.parser")

# Find all product listings
products = soup.find_all('div', class_='pl-item-container')

# Loop through each product and extract information
for product in products:
    title = product.find('a', class_='productList-title').text.strip()
    image_url = product.find('img', class_='pl-image')['src']
    price = product.find('div', class_='productList-price').text.strip()
    asin = product.find('input', class_='pl-asin')['value']
    category = product.find('div', class_='productList-category').text.strip()
    bsr = product.find('span', class_='productList-bsr').text.strip()
    buy_box = product.find('span', class_='qi-buy-box').text.strip()
    today = datetime.date.today()

    print(today)
    print(f"Title: {title}")
    print(f"Image URL: {image_url}")
    print(f"Price: {price}")
    print(f"ASIN: {asin}")
    print(f"Category: {category}")
    print(f"BSR: {bsr}")
    print(f"Buy Box: {buy_box}")
    print("\n---\n")


header = ['Product Image', 'Date', 'Price', 'Title', 'ASIN', 'Category', 'Buy Box']
data = [image_url, today, price, title, asin, category, buy_box]

with open('SellerAmpWebScraper.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


today = datetime.date.today()

print(today)

df = pd.read_csv(r'C:\Users\Desktop\Amazon Seller Bot\SellerAmpWebScraper.csv')

print(df)

#Now we are appending data to the csv

with open('SellerAmpWebScraper.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data) 

def check_price():
    URL = 'https://sas.selleramp.com/sas/lookup?SasLookup%5Bsearch_term%5D=https%3A%2F%2Fwww.amazon.com%2Fs%3Fi%3Dmerchant-items%26me%3DA1E9FT1UFOTH9W%26s%3Ddate-desc-rank%26marketplaceID%3DATVPDKIKX0DER%26qid%3D1701616861%26ref%3Dsr_st_date-desc-rank%26ds%3Dv1%253AGzn1vwAGjtH%252BTwKii4ODl1iaZypL38ff7cXuD0%252FCiMw'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    # Find all product listings
    products = soup.find_all('div', class_='pl-item-container')

    # Loop through each product and extract information
    for product in products:
        title = product.find('a', class_='productList-title').text.strip()
        image_url = product.find('img', class_='pl-image')['src']
        price = product.find('div', class_='productList-price').text.strip()
        asin = product.find('input', class_='pl-asin')['value']
        category = product.find('div', class_='productList-category').text.strip()
        bsr = product.find('span', class_='productList-bsr').text.strip()
        buy_box = product.find('span', class_='qi-buy-box').text.strip()

        print(f"Title: {title}")
        print(f"Image URL: {image_url}")
        print(f"Price: {price}")
        print(f"ASIN: {asin}")
        print(f"Category: {category}")
        print(f"BSR: {bsr}")
        print(f"Buy Box: {buy_box}")
        print("\n---\n")
    import datetime

    today = datetime.date.today()

    
    print(today)
    
    import csv

    header = ['Product Image', 'Date', 'Price', 'Title', 'ASIN', 'Category', 'Buy Box']
    data = [image_url, today, price, title, asin, category, buy_box]

    with open('SellerAmpWebScraper.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data) 

while(True):
    check_price()
    time.sleep(5)
    
df = pd.read_csv(r'C:\Users\Desktop\Amazon Seller Bot\SellerAmpWebScraper.csv')

print(df)