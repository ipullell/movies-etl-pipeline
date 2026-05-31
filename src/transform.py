import pandas as pd
import logging

logger = logging.getLogger(__name__)

def transformMovies(data):
    logger.info("Starting the transformation process...")

    if not data or 'results' not in data:
        logger.info("Transformation failed: Input data is empty or missing 'results' key.")
        return pd.DataFrame()

    try:
        df = pd.DataFrame(data['results'])

        df = df [
            [
                "id",
                "title",
                "genre_ids",
                "popularity",
                "vote_average",
                "vote_count",
                "release_date"
            ]
        ]

        df["title"] = df["title"].fillna('unknown')
        df["genre_ids"] = df["genre_ids"].apply(lambda x:x if isinstance(x, list) else [])
        df["vote_average"] = df["vote_average"].fillna(0).round(2)
        df["vote_count"] = df["vote_count"].fillna(0) 
        df["release_date"] = pd.to_datetime(df["release_date"], errors='coerce')
        df["popularity"] = df["popularity"].fillna(0).round(1)

        logger.info("Transformation process completed successfully.")
        return df
    except Exception as e:
        logger.exception(f"Transformation process failed. Detail: {type(e).__name__}")