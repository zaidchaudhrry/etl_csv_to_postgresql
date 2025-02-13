
This project implements an **ETL (Extract, Transform, Load) pipeline** for processing retail transaction data from an Excel file and loading it into a **PostgreSQL database**. The pipeline follows these three main steps:

- **Extract** → Read raw data from an Excel file (`retail.xlsx`).
- **Transform** → Clean and standardize the data.
- **Load** → Insert the transformed data into a PostgreSQL database.

---

## 📂 Project Structure
```📁 Automated-Sales-Dashboard/
│── etl/
│   ├── extract.py         # Extracts data from the source Excel file
│   ├── transform.py       # Cleans and transforms the extracted data
│   ├── load.py            # Loads the transformed data into PostgreSQL
│── data/                  # Stores the raw and processed data files
│── .env                   # Stores database credentials securely
│── requirements.txt       # Lists required Python dependencies
│── README.md              # Project documentation
```

---

## 🛠️ Requirements

To run this ETL pipeline, you need the following:

- **Python** (version 3.8 or later)
- **PostgreSQL** (local installation or using Docker)
- **Git** (for version control)
- **Virtual Environment** (optional but recommended)

### 📦 Required Python Libraries

The following libraries must be installed:

| Library        | Purpose                                        |
|---------------|-----------------------------------------------|
| `pandas`      | Data manipulation                            |
| `psycopg2`    | PostgreSQL connection                        |
| `python-dotenv` | Loading environment variables              |
| `openpyxl`    | Reading Excel files                          |

These dependencies are listed in `requirements.txt`.

---


### Clone the Repository

```bash
git clone https://github.com/yourusername/Automated-Sales-Dashboard.git
cd Automated-Sales-Dashboard
```

# ⚙️ Setup Instructions

## Set Up a Virtual Environment
```python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# OR
.venv\Scripts\activate     # Windows
```

## Install Required Libraries

```
pip install -r requirements.txt
```
## Configure the .env File

```
DB_HOST=localhost
DB_NAME=etl_db
DB_USER=etl_user
DB_PASSWORD=etl_pass
DB_PORT=5432
```
---
# 🚀 Running the ETL Pipeline

```
python etl/extract.py
```
```
python etl/transform.py
```
```
python etl/load.py
```
---
# 🛠️ Future Improvements
	•	Add real-time streaming ETL capabilities
	•	Integrate AI-based predictive analytics
	•	Enhance dashboard interactivity and automation
---

# 📜 License

This project is licensed under the **MIT License.**


---
# 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit a **pull request.**



---
#  📩 Contact

For questions or suggestions, reach out at:

✉️ Email: zaidchaudhrry@gmail.com
🐙 GitHub: zaidchaudhrry
