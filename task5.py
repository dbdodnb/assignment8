import pandas as pd
import matplotlib.pyplot as plt


def task5():
    titles_df = pd.read_csv('titles.csv')
    credits_df = pd.read_csv('credits.csv')

    merged_df = pd.merge(titles_df, credits_df, left_on='id', right_on='id')

    top_1000_df = merged_df.nlargest(1000, 'imdb_score')

    genres = top_1000_df['genres'].str.split(',').explode().str.strip()

    genre_counts = genres.value_counts()

    plt.figure(figsize=(12, 6))
    genre_counts.plot(kind='bar')
    plt.title('Кількість фільмів та шоу за жанрами (Топ-1000 IMDb)')
    plt.xlabel('Жанр')
    plt.ylabel('Кількість')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
