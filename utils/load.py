import pandas as pd
from sqlalchemy import create_engine
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# ---Save to CSV---
def load_to_csv(df, filename="products.csv"):
    try:
        df.to_csv(filename, index=False)
        print(f"Data successfully saved into {filename}")
        
    except Exception as e:
        print(f"Error saving CSV: {e}")

# ---Save to PostgreSQL---
def load_to_postgre(data, db_url, table_name="fashiontoscrape"):
    try:
        # Create engine database
        engine = create_engine(db_url)
        
        # Save data to "fashiontoscrape" if tables already exists, data will added (append).
        with engine.connect() as con:
            data.to_sql(table_name, con=con, if_exists='append', index=False)
            print(f"Data successfully saved into {table_name} table")
    
    except Exception as e:
        print(f"There is something wrong while saving data: {e}")

# ---Save to Google Sheets---
def load_to_google_sheets(df):
    SERVICE_ACCOUNT_FILE = './google-sheets-api.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    credential = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    SPREADSHEET_ID = '1qTFkSxQnFpCYy1OSOhoB9yNexEHSvVOKyry97_Az3z4'
    RANGE_NAME = 'Sheet1!A1'
    
    try:
        service = build('sheets','v4', credentials=credential)
        sheet = service.spreadsheets()
        values = [df.columns.values.tolist()] + df.values.tolist()
        body = {
            'values': values
        }
        result = sheet.values().update(
            spreadsheetId=SPREADSHEET_ID,
            range=RANGE_NAME,
            valueInputOption='RAW',
            body=body
        ).execute()
        
        print("Data successfully saved into Google Sheets!")
    
    except Exception as e:
        print(f"Error saving to Google Sheets: {e}")