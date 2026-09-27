import time
import pandas as pd
import requests

from bs4 import BeautifulSoup
from datetime import datetime

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    )
}

def fetching_content(url):
    # Fetching HTML content from the given URL.
    session = requests.Session()
    response = session.get(url, headers=HEADERS)
    try:
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"An error occured while making requests to {url}: {e}")
        return None


def safe_gate_text(element):
    return element.get_text(strip=True) if element else None


def extract_fashion_data(div):
    # Fetching fashion data such as title, price, rating, colors, size, gender from div (HTML element).
    try:
        title = safe_gate_text(div.find('h3', class_='product-title'))
        price = safe_gate_text(div.find('span', class_='price'))
        rating = safe_gate_text(div.find('p', string=lambda t: t and "Rating" in t))
        colors = safe_gate_text(div.find('p', string=lambda t: t and "Colors" in t))
        size = safe_gate_text(div.find('p', string=lambda t: t and "Size" in t))
        gender = safe_gate_text(div.find('p', string=lambda t: t and "Gender" in t))
        
        return {
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Colors": colors,
            "Size": size,
            "Gender": gender,
            "Timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        print(f"Error extracting fashion data: {e}")
        return {}
    

def scrape_fashion(base_url, start_page=1, delay=2):
    # The main function is to fetch all the data, from requests to storing it in a data variable.
    data = []
    page_number = start_page
    
    while True:
        if page_number == 1:
            url = base_url
        else:
            url = f"{base_url}/page{page_number}"
            
        print(f"Scraping page: {url}")
        
        content = fetching_content(url)
        if content:
            soup = BeautifulSoup(content, "html.parser")
            divs_element = soup.find_all('div', class_='collection-card')
            for div in divs_element:
                fashion = extract_fashion_data(div)
                data.append(fashion)
            
            next_button = soup.find('li', class_='page-item next')
            if next_button:
                page_number += 1
                time.sleep(delay) # Delay before next page
            else:
                break # Break if there is no any next button
        else:
            break # Break if there us any error
        
    return data