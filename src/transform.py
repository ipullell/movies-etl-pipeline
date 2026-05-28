# from extract import fetchMovies
# import pandas as pd

# def transformMovies(data):
#     df = pd.DataFrame(data['results'])

#     df = df [
#         [
#             "id",
#             "title",
#             "genre_ids",
#             "popularity",
#             "vote_average",
#             "vote_count",
#             "release_date"
#         ]
#     ]

#     df["release_date"] = pd.to_datetime(df["release_date"])
#     df["popularity"] = df["popularity"].round(1)
#     df["vote_average"] = df["vote_average"].round(2)
#     df_explode = df.explode("genre_ids")
