# Netflix Data Analysis and Recommendation Engine

This project analyzes personal Netflix data and provides a recommendation engine to suggest top shows. The project is built using Flask for the web interface, pandas for data manipulation, and scikit-surprise for the recommendation engine.

## Project Structure

![image](https://github.com/user-attachments/assets/5513302a-38bc-4227-9f62-7b6c8b4bab1f)


## Installation

1. Clone the repository:

git clone https://github.com/yourusername/netflix-data-analysis.git
cd netflix-data-analysis

2. Create and activate a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install the dependencies:
pip install -r requirements.txt

## Usage
1. Run the Flask application:
python app.py

2. Open your web browser and go to http://127.0.0.1:5000.

3. Upload your NetflixViewingHistory.csv file to analyze the data and get recommendations.

## Explanation of Components
app.py
This is the main Flask application file. It handles the web interface and routes:
index(): Handles file upload and redirects to the processing page.
process(): Processes the uploaded file, generates data analysis, and provides recommendations.

src/data_preprocessing.py
Contains functions for loading and preprocessing the Netflix data:
load_data(file_path): Loads the Netflix viewing history CSV file.
preprocess_data(data): Preprocesses the data for analysis and recommendation.

src/data_analysis.py
Contains functions for analyzing and plotting the data:
plot_most_watched_shows(data): Plots the most-watched shows from the data.

src/recommendation.py
Contains functions for building and using the recommendation engine:
build_recommendation_engine(data): Builds the recommendation engine using the SVD algorithm.
recommend_top_shows(svd, user_id, data): Recommends top shows for a given user.

## Contribution
Feel free to fork this repository, make improvements, and submit pull requests. Any contributions are welcome!

License
This project is licensed under the MIT License
