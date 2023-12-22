import pandas as pd


def task4():
    titles_df = pd.read_csv('titles.csv')
    credits_df = pd.read_csv('credits.csv')

    credits_df['person_id'] = credits_df['person_id'].astype('object')

    merged_df = pd.merge(titles_df, credits_df, left_on='id', right_on='id')

    top_1000_df = merged_df.nlargest(1000, 'imdb_score')

    actor_counts = top_1000_df['name'].str.split(',').explode().str.strip().value_counts()

    top_10_actors = actor_counts.head(10)
    print(top_10_actors)
