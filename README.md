# Title: Movie Recommendation System<br>
Dataset : https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

## Overview

This repository contains a Movie Recommendation System implemented using natural language processing and machine learning techniques. The system is based on content-based filtering, utilizing movie metadata such as genres, keywords, cast, and crew information to suggest similar movies. The recommendation algorithm employs cosine similarity to find movies that are closely related to a given input.

## Files

1.**Movie Recommender.ipynb:** Google Colaboratory containing the code for the Movie Recommendation System. It includes data preprocessing, feature extraction, and the recommendation algorithm.<br>
2.**tmdb_5000_movies.csv:** Dataset containing information about movies, including titles, overviews, genres, and keywords.<br>
3.**tmdb_5000_credits.csv:** Dataset containing credits information, including cast and crew details for each movie.<br>
4.**movies.pkl:** Pickle file containing preprocessed movie data, including features and tags used for recommendation.

## Usage

1.Open the Google Colaboratory `Movie Recommender.ipynb` to understand the implementation details.<br>
2.Run the notebook to generate the movie recommendation model.<br>
3.Use the `recommend(movie)` function to get movie recommendations based on a given input movie title.

python<br>
Copy code

<code>recommend('Avatar')</code>

## Dependencies

numpy<br>
pandas<br>
ast<br>
nltk<br>
sklearn

## Data Preprocessing
The provided datasets (`tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`) are merged and cleaned to create a consolidated dataset. The relevant features, such as genres, keywords, cast, and crew, are extracted and processed for further analysis.

## Feature Extraction
Text data, including overviews, genres, keywords, cast, and crew information, is processed and transformed into a feature vector using techniques such as stemming and vectorization.

## Recommendation Algorithm
The recommendation system uses cosine similarity to find movies with similar content. The `recommend(movie)` function takes a movie title as input and suggests a list of five movies that are closely related to the input movie.

## Pickle File
The preprocessed movie data, along with the recommendation model, is saved in a pickle file (`movies.pkl`). This file can be used to load the processed data and make recommendations without rerunning the entire code.

Feel free to explore and modify the code for your specific use case or dataset.

### Note: 
Ensure that the required dependencies are installed before running the code.
# Cine Vista - Personalized Movie Recommendations

Cine Vista is a Streamlit web application that provides personalized movie recommendations based on user preferences. The app utilizes a collaborative filtering algorithm to suggest movies similar to the one selected by the user. Powered by The Movie Database (TMDb) API, Cine Vista fetches movie details such as posters, genres, ratings, and overviews to offer a comprehensive view of the recommended films.

## Features

- **Movie Selection:** Users can either type the name of a movie or choose one from the dropdown menu.
  
- **Recommendation:** Upon clicking the "Recommend" button, Cine Vista displays the top 5 movie recommendations along with their posters, genres, ratings, and runtimes.

- **Detailed Information:** Each recommendation includes an expandable section with a detailed movie overview, allowing users to explore more about the suggested films.

## How to Run

1. Clone the repository: `git clone https://github.com/your-username/Cine-Vista.git`
2. Navigate to the project directory: `cd Cine-Vista`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Run the Streamlit app: `streamlit run cine_vista.py`

## Data Sources

- Movie data is sourced from The Movie Database (TMDb) API.
- Precomputed movie similarities and details are stored in pickled files (`movies_dict.pkl` and `sim.pkl`).

## Acknowledgments

- Cine Vista makes use of the Streamlit library for creating interactive web applications.
- Movie information is fetched from The Movie Database (TMDb) API.

Explore the magic of cinema with Cine Vista and discover your next favorite movie! 🍿🎬

---

**[View Cine Vista on GitHub]()** 🌐

Happy movie recommending!
