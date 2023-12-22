import pandas as pd
import matplotlib.pyplot as plt


def task2():
    data = pd.read_csv('titles.csv')

    data = data.dropna(subset=['genres'])

    data['genres'] = data['genres'].apply(eval)

    genres_list = [genre for genres in data['genres'] for genre in genres]

    genres_series = pd.Series(genres_list)

    genre_counts = genres_series.value_counts()

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%', startangle=90, labeldistance=1.1, pctdistance=0.85)
    ax.axis('equal')
    ax.set_title('Distribution of Genres')
    plt.show()



