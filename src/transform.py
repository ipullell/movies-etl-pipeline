from extract import fetchMovies
import pandas as pd

def transformMovies(data):
    df = pd.DataFrame(data['results']) # mengubah menjadi dataframe(tabel)

    df = df [ # menyaring data yg akan di ambil
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

    df["release_date"] = pd.to_datetime(df["release_date"]) # mengubah tipe data menjadi datetime
    df["popularity"] = df["popularity"].round(1) # mengubah data menjadi desimal dan mengambil 1 angka di belakang koma
    df["vote_average"] = df["vote_average"].round(2)  # mengubah data menjadi desimal dan mengambil 2 angka di belakang koma
    df_explode = df.explode("genre_ids") # memecah data array menjadi baris
