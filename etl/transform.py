import pandas as pd
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

CLEANED_FILE_PATH = os.path.join(BASE_DIR, "data", "cleaned_retail.csv")

TRANSFORMED_FILE_PATH = os.path.join(BASE_DIR, "data", "transformed_retail.csv")
def transform_data(file_path):
    try:
        print("Loading cleaned CSV file...")
        df = pd.read_csv(file_path)
        print(f"Loaded {len(df)} rows")




        df["InvoiceNo"] = df["InvoiceNo"].astype(str)

        df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce")  
        df = df[df["UnitPrice"] >= 0]  


        df["Quantity"] = df["Quantity"].astype(int)


        df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")

        print("Data transformations applied successfully!")
        return df
    
    except Exception as e:
        print("Error during transformation:", e)
        return None
    
def save_transformed_data(df, file_path):
    try:
        df.to_csv(file_path, index = False)
        print(f"Transformed data saved at {file_path}")
    except Exception as e:
        print("Error saving:", e)

transformed_data = transform_data(CLEANED_FILE_PATH)

if transformed_data is not None:
    save_transformed_data(transformed_data, TRANSFORMED_FILE_PATH)