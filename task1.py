import pandas as pd
import matplotlib.pyplot as plt


def task1():
    file_path = 'titles.csv'
    data = pd.read_csv(file_path)

    data = data.dropna(subset=['imdb_score'])

    plt.figure(figsize=(10, 6))
    plt.hist(data['imdb_score'], bins=round((max(data['imdb_score']) - min(data['imdb_score'])) / 0.2), color='skyblue',
             edgecolor='black')
    plt.title('Розподіл оцінок IMDB')
    plt.xlabel('IMDB оцінка')
    plt.ylabel('Кількість фільмів/серіалів')
    plt.grid(True)
    plt.show()

    return data


if __name__ == "__main__":
    task1()
