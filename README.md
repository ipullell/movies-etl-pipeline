# 🎬 Movie ETL Pipeline

A Python-based ETL (Extract, Transform, Load) pipeline that retrieves popular movie data from **The Movie Database (TMDB) API**, performs data cleaning and transformation using **Pandas**, and loads the processed dataset into **PostgreSQL**.

This project was built to practice real-world Data Engineering concepts such as API integration, data transformation, database loading, logging, environment variable management, and modular pipeline design.

---

# 📌 Project Goals

* Extract movie data from a public REST API
* Store raw API responses for auditing and backup purposes
* Clean and transform raw JSON data into a structured format
* Load processed data into PostgreSQL
* Implement logging and error handling
* Organize code using a modular ETL architecture

---

# 🏗️ Pipeline Architecture

```text
TMDB API
    │
    ▼
┌─────────────┐
│   Extract   │
└─────────────┘
    │
    ├── API Request
    ├── Authentication (Bearer Token)
    └── Raw JSON Backup
    │
    ▼
┌─────────────┐
│ Transform   │
└─────────────┘
    │
    ├── Column Selection
    ├── Missing Value Handling
    ├── Date Conversion
    ├── Data Standardization
    └── Validation
    │
    ▼
┌─────────────┐
│    Load     │
└─────────────┘
    │
    └── PostgreSQL Database
    │
    ▼
┌─────────────┐
│   Logging   │
└─────────────┘
```

---

# ⚙️ Features

### Extract

* Connects to the TMDB API
* Uses Bearer Token authentication
* Retrieves popular movie data
* Stores raw API responses as timestamped JSON files
* Handles API request failures

### Transform

* Converts JSON data into a Pandas DataFrame
* Selects only relevant movie attributes
* Handles missing values
* Standardizes numerical columns
* Converts release dates into datetime format
* Validates list-based genre information

### Load

* Connects to PostgreSQL using SQLAlchemy
* Inserts transformed data into a database table
* Handles database loading errors

### Logging

* Tracks pipeline execution status
* Logs extraction, transformation, and loading activities
* Records errors for troubleshooting

---

# 📂 Project Structure

```text
movie-etl-pipeline/
│
├── data/
│   └── raw_movies_*.json
│
├── logs/
│   └── app.log
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── main.py
├── .env
├── README.md
├── requirements.txt
└── LICENSE
```

---

# 🛠️ Tech Stack

| Category                 | Technology            |
| ------------------------ | --------------------- |
| Language                 | Python                |
| API                      | TMDB API              |
| Data Processing          | Pandas                |
| Database                 | PostgreSQL            |
| ORM / Database Connector | SQLAlchemy            |
| Environment Variables    | python-dotenv         |
| Logging                  | Python Logging Module |

---

# 🔄 ETL Workflow

## 1. Extract

The pipeline requests movie data from the TMDB API.

Raw responses are stored locally in the `data/` directory using timestamped filenames:

```text
raw_movies_31-05-2026_20-30-15.json
```

This allows future auditing and debugging of source data.

---

## 2. Transform

The following transformations are applied:

### Selected Columns

```text
id
title
genre_ids
popularity
vote_average
vote_count
release_date
```

### Data Cleaning

* Fill missing movie titles with `"unknown"`
* Fill missing popularity values with `0`
* Fill missing vote averages with `0`
* Fill missing vote counts with `0`
* Ensure `genre_ids` is always a valid list

### Type Conversion

```text
release_date → datetime
```

### Standardization

```text
vote_average → rounded to 2 decimal places
popularity   → rounded to 1 decimal place
```

---

## 3. Load

The cleaned dataset is loaded into PostgreSQL.

Target table:

```sql
data_movies
```

Insertion method:

```python
df.to_sql(
    "data_movies",
    engine,
    if_exists="append",
    index=False
)
```

---

# 🔐 Environment Variables

Create a `.env` file in the project root:

```env
TMDB_TOKEN=your_tmdb_bearer_token

DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=movies_db
```

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/movie-etl-pipeline.git
cd movie-etl-pipeline
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run The Pipeline

Execute:

```bash
python main.py
```

Successful execution:

```text
==================================================
✅ PIPELINE EXECUTION SUCCESS!
==================================================
Status       : COMPLETED
Message      : All ETL processes executed successfully.
Total Rows   : XX rows processed.
==================================================
```

---

# 📝 Logging

Pipeline activities are stored in:

```text
logs/app.log
```

Example:

```text
2026-05-31 20:15:32 - MAIN_PIPELINE - INFO - Starting the movie ETL pipeline...
2026-05-31 20:15:34 - src.extract - INFO - Extraction process completed successfully.
2026-05-31 20:15:35 - src.transform - INFO - Transformation process completed successfully.
2026-05-31 20:15:36 - src.load - INFO - Database load completed successfully.
```

---

# 🎯 Skills Demonstrated

This project demonstrates practical experience with:

* REST API Integration
* Data Extraction
* Data Transformation
* Data Cleaning
* PostgreSQL
* SQLAlchemy
* ETL Pipeline Design
* Logging
* Error Handling
* Environment Variable Management
* Modular Python Development

---

# 🔮 Future Improvements

Potential enhancements for future versions:

* Retry mechanism for failed API requests
* Data quality validation checks
* Incremental loading strategy
* Docker containerization
* Apache Airflow orchestration
* Unit testing
* CI/CD integration
* Data warehouse integration

---

# 📚 Learning Outcome

```
This project was developed as part of a Data Engineering learning journey to gain hands-on experience building production-style ETL pipelines using Python, PostgreSQL, and external APIs.
```

# License

This project is licensed under the [MIT License](LICENSE).