import pandas as pd
import os

# Get the absolute path to the project folder
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

DATA_FILE_PATH = os.path.join(BASE_DIR, "data", "retail.xlsx")

print(f"📂 Looking for file at: {DATA_FILE_PATH}")

CLEANED_FILE_PATH = os.path.join(BASE_DIR, "data", "cleaned_retail.csv")


def extract_data(file_path):
    try:
        print("Loading excel file...")
        df = pd.read_excel(file_path, engine = "openpyxl")
        print ("Loaded {} rows".format(len(df)))

        return df
    
    except Exception as e:
        print("Error during extraction: ", e)
        return None
    
def clean_data(dataFrame):
    print("Begining cleaning job...")
    dataFrame.dropna(subset=["CustomerID", "Description"], inplace = True)
    dataFrame["InvoiceDate"] = pd.to_datetime(dataFrame["InvoiceDate"])
    dataFrame = dataFrame[dataFrame["Quantity"] >= 0]
    print ("Data after cleaning {} rows".format(len(dataFrame)))
    return dataFrame


def save_cleaned_data(df, file_path):
    try:
        df.to_csv(file_path, index = False)
        print(f"Cleaned data saved at: {file_path}")
    except Exception as e:
        print("Error saving data:", e)

extracted_data = extract_data(DATA_FILE_PATH)

cleaned_data = clean_data(extracted_data)

if cleaned_data is not None:
    save_cleaned_data(cleaned_data, CLEANED_FILE_PATH)