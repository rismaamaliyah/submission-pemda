from utils.extract import scrape_fashion
from utils.transform import transform_data
from utils.load import load_to_csv, load_to_postgre, load_to_google_sheets

def main():
    # The main function for the whole scraping process all the way to saving it.
    BASE_URL = 'https://fashion-studio.dicoding.dev'
    all_fashion_data = scrape_fashion(BASE_URL)
    if all_fashion_data:
        try:
            DataFrame = transform_data(all_fashion_data)
            
            load_to_csv(DataFrame)
            
            db_url = 'postgresql+psycopg2://developer:supersecret@localhost:5432/fashiondb'
            load_to_postgre(DataFrame, db_url)
            
            load_to_google_sheets(DataFrame)
        
        except Exception as e:
            print(f"There is something wrong in this process: {e}")
    
    else:
        print("No data found")


if __name__ == '__main__':
    main()