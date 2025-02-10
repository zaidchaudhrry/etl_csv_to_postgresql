This project implements an ETL (Extract, Transform, Load) pipeline for processing retail transaction data from an Excel file and loading it into a PostgreSQL database. The pipeline follows these three main steps:

Extract → Read raw data from an Excel file (retail.xlsx).
Transform → Clean and standardize the data.
Load → Insert the transformed data into a PostgreSQL database.

Project Structure
The project is organized as follows:

etl/extract.py → Extracts data from the source Excel file.
etl/transform.py → Cleans and transforms the extracted data.
etl/load.py → Loads the transformed data into PostgreSQL.
data/ → Stores the raw and processed data files.
.env → Stores database credentials securely.
requirements.txt → Lists required Python dependencies.


Requirements
To run this ETL pipeline, you need the following:

Python (version 3.8 or later)
PostgreSQL (local installation or using Docker)
Git (for version control)
Virtual Environment (optional but recommended)
Required Python Libraries
The following libraries must be installed:

pandas → For data manipulation
psycopg2 → For connecting to PostgreSQL
python-dotenv → For loading environment variables
openpyxl → For reading Excel files
These dependencies are listed in requirements.txt.

Setup Instructions
1️⃣ Clone the Repository
First, download the project from GitHub and navigate to the project folder.

2️⃣ Set Up a Virtual Environment (Optional)
It is recommended to create a virtual environment to manage dependencies.

3️⃣ Install Required Libraries
Use pip to install the required dependencies listed in requirements.txt.

4️⃣ Set Up the PostgreSQL Database
Ensure you have PostgreSQL installed and create a new database named etl_db.
If using Docker, set up a PostgreSQL container.

5️⃣ Configure the .env File
Inside the root directory, create a file named .env and add your PostgreSQL credentials in this format:
DB_HOST=localhost
DB_NAME=etl_db
DB_USER=etl_user
DB_PASSWORD=etl_pass
DB_PORT=5432

Running the ETL Pipeline
The pipeline consists of three scripts: extract, transform, and load.

1️⃣ Extract Data
Run the extraction script to read data from the source Excel file.

2️⃣ Transform Data
After extraction, the data is cleaned and formatted properly.

3️⃣ Load Data into PostgreSQL
Once transformed, the cleaned data is inserted into the PostgreSQL database.