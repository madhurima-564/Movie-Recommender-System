# Title : Cine Vista

## Overview

This GitHub repository contains the implementation of a Movie Recommendation System built using Streamlit, a web application framework for Python. The system leverages content-based filtering to provide personalized movie recommendations based on user preferences. The recommendation algorithm utilizes movie metadata such as genres, keywords, cast, and crew information to suggest similar movies. The application fetches movie details and posters from The Movie Database (TMDb) API.

## Files

- **app.py**: Python script containing the Streamlit web application code.
- **movies.pkl**: Pickle file containing preprocessed movie data, including features and tags used for recommendation.
- **sim.pkl**: Pickle file containing the cosine similarity matrix for movie recommendations.
- **movies_dict.pkl**: Pickle file containing a dictionary representation of the movie data.

## Features

- **Web Application**: The Movie Recommendation System is implemented as a web application using Streamlit, allowing users to interact with the recommendation engine through a user-friendly interface.

- **Personalized Recommendations**: The recommendation algorithm suggests the top 5 movies similar to the user's selected movie, considering various features such as genres, cast, and crew.

- **Dynamic Movie Details**: Movie details, including posters, genres, rating, runtime, and overview, are dynamically fetched from the TMDb API.

## Usage

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the Streamlit app using the command `streamlit run app.py`.
4. Open the provided URL in your web browser to access the Movie Recommendation System.

## Dependencies

- Streamlit
- Pandas
- Requests

## Note

Ensure that you have an active internet connection to fetch movie details and posters from the TMDb API. The TMDb API key used in the code may have usage limitations; consider obtaining your own API key for extended usage.

Feel free to explore and customize the code for your specific requirements.

**Happy movie exploring!**
