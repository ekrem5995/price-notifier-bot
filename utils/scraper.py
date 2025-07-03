import requests
from bs4 import BeautifulSoup

def get_product_price(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
import requests
from bs4 import BeautifulSoup

def get_product_price(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.find("h1").text.strip()  # <-- You forgot this line
    price = soup.find("p", class_="price_color").text.strip()
    price = price.replace('Â', '')  # Clean weird character

    return title, price


    return title, price
