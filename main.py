from src.extract import fetchMovies
from src.transform import transformMovies
from src.load import saveMovies
import logging
import os

os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/app.log",
    filemode="a",
    format=("%(asctime)s - %(name)s - %(levelname)s - %(message)s"),
    level=logging.INFO
)

logger = logging.getLogger("MAIN_PIPELINE")

def pipeline():
    logger.info("==================================")
    logger.info("Starting the movie ETL pipeline...")
    logger.info("==================================")

    try:
        raw_data = fetchMovies()

        clean_data = transformMovies(raw_data)

        saveMovies(clean_data)
        logger.info("=========================================")
        logger.info("Movie ETL pipeline finished successfully!")
        logger.info("=========================================")

        print("\n" + "="*50)
        print("✅ PIPELINE EXECUTION SUCCESS!")
        print("="*50)
        print("Status       : COMPLETED")
        print("Message      : All ETL processes executed successfully.")
        print(f"Total Rows   : {len(clean_data)} rows processed.")
        print("-"*50)
        print("Data is now available in your PostgreSQL database.")
        print("="*50 + "\n")

    except Exception as e:
        error_name = type(e).__name__
        error_message = str(e)
        logger.error(f"Movie ETL pipeline execution failed. Reason: [{type(e).__name__}]")

        print("\n" + "="*50)
        print("🚨 PIPELINE EXECUTION FAILED!")
        print("="*50)
        print(f"Error Type   : {error_name}")
        print(f"Description  : {error_message}")
        print("-"*50)
        print("Please check '../logs/app.log' for more details.")
        print("="*50 + "\n")
    
if __name__ == "__main__":
    pipeline()