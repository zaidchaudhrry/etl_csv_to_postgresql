import psycopg2
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ✅ Get PostgreSQL credentials from .env
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")

# ✅ Get the path to the transformed data file
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TRANSFORMED_FILE_PATH = os.path.join(BASE_DIR, "data", "transformed_retail.csv")

# ✅ Function to Connect to PostgreSQL
def connect_to_db():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        print("✅ Connected to PostgreSQL")
        return conn
    except Exception as e:
        print("❌ Error connecting to PostgreSQL:", e)
        return None

# ✅ Function to Insert Data into PostgreSQL
def insert_data():
    conn = connect_to_db()
    if conn is None:
        return

    try:
        cur = conn.cursor()
        print(f"📥 Loading data from: {TRANSFORMED_FILE_PATH}")

        # Read the transformed CSV file
        df = pd.read_csv(TRANSFORMED_FILE_PATH)

        # ✅ Insert query
        insert_query = """
        INSERT INTO retail_transactions (invoice_no, stock_code, description, quantity, invoice_date, unit_price, customer_id, country)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT DO NOTHING;
        """

        # ✅ Convert DataFrame to list of tuples for insertion
        data_to_insert = df.to_records(index=False).tolist()

        # ✅ Insert rows into PostgreSQL
        cur.executemany(insert_query, data_to_insert)
        conn.commit()
        print(f"✅ Inserted {len(df)} rows into `retail_transactions`.")

        # Close connections
        cur.close()
        conn.close()

    except Exception as e:
        print("❌ Error inserting data:", e)

# ✅ Run Data Insertion
if __name__ == "__main__":
    insert_data()
