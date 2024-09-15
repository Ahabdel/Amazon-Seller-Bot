import requests
from bs4 import BeautifulSoup
import datetime


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
    'LoginForm[email]': '',  # Replace with your email
    'LoginForm[password]': '',        # Replace with your password
    'LoginForm[rememberMe]': '1'
}

# Send a POST request to the login URL
response = session.post(login_url, data=login_data)

# Parse the response to extract the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the dropdown that likely contains the username
dropdowns = soup.find_all('li', class_='dropdown')

# Extract the username if found
for dropdown in dropdowns:
    account_link = dropdown.find('a', {'class': 'dropdown-toggle'})
    if account_link and 'My Account - ' in account_link.text:
        username = account_link.text.split('My Account - ')[-1].strip()
        print("Logged in as:", username)
        break
    else:
        print("Username not found in dropdown")
else:
    print("Login failed or dropdown not found")



# URL to scrape data from
data_url = 'https://sas.selleramp.com/sas/lookup?SasLookup%5Bsearch_term%5D=https%3A%2F%2Fwww.amazon.com%2Fs%3Fi%3Dmerchant-items%26me%3DA1E9FT1UFOTH9W%26s%3Ddate-desc-rank%26marketplaceID%3DATVPDKIKX0DER%26qid%3D1701616861%26ref%3Dsr_st_date-desc-rank%26ds%3Dv1%253AGzn1vwAGjtH%252BTwKii4ODl1iaZypL38ff7cXuD0%252FCiMw'

# Make a GET request to the URL
response = session.get(data_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all product listings
    products = soup.find_all('div', class_='pl-item-container')

    # Loop through each product and extract information
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
    # Extract the desired data
    # Note: You need to adjust the following lines according to the actual structure of the webpage and the data you need
    data = soup.find_all('div', class_='your-target-class')  # Replace 'your-target-class' with the actual class or identifier of the data

    # Process and print the extracted data
    for item in data:
        print(item.text)  # Or any other processing you need
else:
    print("Failed to retrieve data from the URL")
