from sqlalchemy import create_engine
from dotenv import load_dotenv
import logging
import os
load_dotenv()

logger = logging.getLogger(__name__)

def saveMovies(df):
    logger.info("Loading data into the database...")

    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    name = os.getenv("DB_NAME")

    try:
        engine = create_engine(
            f"postgresql://{user}:{password}@{host}:{port}/{name}"
        )

        df.to_sql(
            "data_movies",
            engine,
            if_exists="append",
            index=False
        )
        logger.info("Database load completed successfully.")

    except Exception as e:
        logger.error(f"Database load failed. Detail: [{type(e).__name__}]")
        raise RuntimeError(f"Failed to save data to PostgreSQL. Detail: [{type(e).__name__}]")
