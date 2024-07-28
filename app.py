from flask import Flask, request, render_template, redirect, url_for
import os
from src.data_preprocessing import load_data, preprocess_data
from src.data_analysis import plot_most_watched_shows
from src.recommendation import build_recommendation_engine, recommend_top_shows

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'data/'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'NetflixViewingHistory.csv')
            file.save(filepath)
            return redirect(url_for('process'))
    return render_template('index.html')

@app.route('/process')
def process():
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'NetflixViewingHistory.csv')
    netflix_data = load_data(file_path)
    netflix_data = preprocess_data(netflix_data)

    plot_most_watched_shows(netflix_data)

    svd = build_recommendation_engine(netflix_data)

    user_id = 1  # Example user_id
    top_recommendations = recommend_top_shows(svd, user_id, netflix_data)

    return f"Top 5 Recommendations: {top_recommendations}"

if __name__ == '__main__':
    app.run(debug=True)
