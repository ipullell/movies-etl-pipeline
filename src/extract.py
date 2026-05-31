import requests
import os
import json
from datetime import datetime
from dotenv import load_dotenv
import logging
load_dotenv()

logger = logging.getLogger(__name__)

def fetchMovies():
    logger.info("Starting extract process...")
    bearer_token = os.getenv("TMDB_TOKEN")
    url = "https://api.themoviedb.org/3/movie/popular"
    time_stamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    file_name = f"data/raw_movies_{time_stamp}.json"

    if not bearer_token:
        raise ValueError("TMDB_TOKEN is missing from the .env file.")

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)

        logger.info("Extraction process completed successfully.")
        return data
    except requests.exceptions.RequestException as e:
        logger.error(f"Data retrieval failed Error: [{type(e).__name__}]")
        raise RuntimeError(f"Data retrieval failed Error: [{type(e).__name__}]")

if __name__ == "__main__":
    fetchMovies()