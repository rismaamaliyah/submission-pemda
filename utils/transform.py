import pandas as pd

def transform_data(data):
    try:
        # Making data into DataFrame
        df = pd.DataFrame(data)
        
        # Drop invalid data
        df = df[df["Title"] != "Unknown Product"]
        df = df[df["Price"] != "Price Unavailable"]
        df = df[~df["Rating"].str.contains("Not Rated|Invalid", na=False)]
    
        try:
            # Clean Price -> USD to Rupiah
            df["Price"] = df["Price"].str.replace("$", "").astype(float) * 16000
        except Exception as e:
            print(f"Error converting Price: {e}")
            df["Price"] = None
        
        try:
            # Clean Rating -> take float number
            df["Rating"] = df["Rating"].str.extract(r"(\d+\.\d+)").astype(float)
        except Exception as e:
            print(f"Error converting Rating: {e}")
            df["Rating"] = None
    
        try: 
            # Clean Colors -> take float number
            df["Colors"] = df["Colors"].str.extract(r"(\d+)").astype(int)
        except Exception as e:
            print(f"Error converting Colors: {e}")
            df["Colors"] = None
    
        # Clean Size & Gender
        df["Size"] = df["Size"].str.replace("Size: ", "")
        df["Gender"] = df["Gender"].str.replace("Gender: ", "")
        
        # Drop null and duplicate
        df = df.dropna().drop_duplicates()
        
        return df
    
    except Exception as e:
        print(f"Error transforming data: {e}")
        return pd.DataFrame() # return empty DataFrame if total failure