import pandas as pd
from surprise import Reader, Dataset, SVD
from surprise.model_selection import train_test_split

def build_recommendation_engine(data):
    reader = Reader(rating_scale=(1, 5))
    dataset = Dataset.load_from_df(data[['UserId', 'Title', 'Rating']], reader)
    trainset, testset = train_test_split(dataset, test_size=0.25)
    svd = SVD()
    svd.fit(trainset)
    return svd

def recommend_top_shows(svd, user_id, data):
    all_titles = data['Title'].unique()
    user_data = data[data['UserId'] == user_id]
    user_watched_titles = user_data['Title'].unique()
    titles_to_recommend = [title for title in all_titles if title not in user_watched_titles]
    
    predictions = [svd.predict(user_id, title).est for title in titles_to_recommend]
    top_indices = sorted(range(len(predictions)), key=lambda i: predictions[i], reverse=True)[:5]
    top_recommendations = [titles_to_recommend[i] for i in top_indices]
    return top_recommendations
