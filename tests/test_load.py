import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pandas as pd
from unittest.mock import patch, MagicMock
from utils.load import load_to_csv, load_to_postgre, load_to_google_sheets

def test_load_to_csv(tmp_path):
    df = pd.DataFrame({"Title":["T-shirt"], "Price":[16000], "Rating":[4.5], "Colors":[3], "Size":["M"], "Gender":["Men"], "Timestamp":["2026-06-15T16:20:00"]})
    file = tmp_path / "test.csv"
    load_to_csv(df, file)
    assert file.exists()
    
def test_load_to_postgre():
    df = pd.DataFrame({"Title":["Hoodie"], "Price":[320000], "Rating":[4.8], "Colors":[2], "Size":["L"], "Gender":["Unisex"], "Timestamp":["2026-06-15T16:21:00"]})
    db_url = "postgresql+psycopg2://developer:supersecret@localhost:5432/fashiondb"
    load_to_postgre(df, db_url)

@patch("utils.load.build")
@patch("utils.load.Credentials.from_service_account_file")
def test_load_to_google_sheets(mock_creds, mock_build):
    # Mock DataFrame
    df = pd.DataFrame({"Title":["T-shirt"], "Price":[160000]})
    
    # Mock service
    mock_service = MagicMock()
    mock_values = MagicMock()
    mock_service.spreadsheets.return_value = mock_service
    mock_service.values.return_value = mock_values
    mock_values.update.return_value.execute.return_value = {"updatedCells": 2}
    mock_build.return_value = mock_service
    
    # Run function
    load_to_google_sheets(df)
    
    # Make sure update is called
    mock_values.update.assert_called_once()