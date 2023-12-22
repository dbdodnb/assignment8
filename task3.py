import pandas as pd
import matplotlib.pyplot as plt


def task3():
    file_path = 'titles.csv'
    data = pd.read_csv(file_path)

    high_rated = data[data['imdb_score'] > 8.0]

    grouped_data = high_rated.groupby('release_year')['title'].count() / data.groupby('release_year')[
        'title'].count() * 100

    plt.figure(figsize=(12, 6))
    grouped_data.plot(kind='bar')
    plt.title('Відсоток фільмів та шоу з рейтингом більше 8.0 за роками')
    plt.xlabel('Рік')
    plt.ylabel('Відсоток')

    max_year = grouped_data.idxmax()
    max_percentage = grouped_data.max()

    print(f'Найуспішніший рік: {max_year} з відсотком {max_percentage:.2f}%')

    plt.show()


