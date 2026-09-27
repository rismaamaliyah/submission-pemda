import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.extract import scrape_fashion
from utils.transform import transform_data

def test_transform_cleaning():
    raw_data = [
        {"Title": "Jacket 6", "Price": "$153.37", "Rating": "⭐ 3.3 / 5",
         "Colors": "3 Colors", "Size": "Size: S", "Gender": "Gender: Unisex", "Timestamp": "2026-06-15"}
    ]
    df = transform_data(raw_data)
    
    # Check data type
    assert "Price" in df.columns
    assert df["Price"].dtype == "float64"
    assert "Rating" in df.columns
    assert df["Rating"].dtype == "float64"
    
    # Check there is no invalid values
    assert not df["Title"].str.contains("Unknown Product").any()
    assert not df["Price"].isna().any()