import pytest
import sys, os
import requests
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from bs4 import BeautifulSoup
from utils.extract import fetching_content, safe_gate_text, extract_fashion_data,scrape_fashion

def test_fetching_content_success():
    soup = fetching_content("https://fashion-studio.dicoding.dev")
    assert soup is not None

def test_fetching_content_fail():
    with pytest.raises(requests.exceptions.ConnectionError):
        fetching_content("https://invalid-url.test")
        
def test_safe_gate_text_normal():
    soup = BeautifulSoup("<p> Hoodie </p>", "html.parser")
    tag = soup.find("p")
    assert safe_gate_text(tag) == "Hoodie"

def test_safe_gate_text_none():
    assert safe_gate_text(None) is None

def test_extract_fashion_data():
    html = """
    <div class="collection-card">
        <div style="position: relative;">
            <img src="https://picsum.photos/280/350?random=6" class="collection-image" alt="Jacket 6">
        </div>
        <div class="product-details">
            <h3 class="product-title">Jacket 6</h3>
            <div class="price-container">
                <span class="price">$153.37</span>
            </div>
            <p style="font-size: 14px; color: #777;">Rating: ⭐ 3.3 / 5</p>
            <p style="font-size: 14px; color: #777;">3 Colors</p>
            <p style="font-size: 14px; color: #777;">Size: S</p>
            <p style="font-size: 14px; color: #777;">Gender: Unisex</p>
        </div>
    </div>
    """
    soup = BeautifulSoup(html, "html.parser")
    div = soup.find("div", class_="collection-card")
    data = extract_fashion_data(div)
    assert data["Title"] == "Jacket 6"
    assert data["Price"] == "$153.37"
    assert data["Rating"] == "Rating: ⭐ 3.3 / 5"

def test_scrape_fashion_not_empty():
    BASE_URL = "https://fashion-studio.dicoding.dev"
    data = scrape_fashion(BASE_URL)
    assert len(data) > 0
    assert "Title" in data[0]
    assert "Timestamp" in data[0]