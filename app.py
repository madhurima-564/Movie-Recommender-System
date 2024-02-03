import streamlit as st
import pickle
import pandas as pd
import requests

st.set_page_config(page_title='Cine Vista', page_icon="venv/log.png",
                   layout="wide")


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=659eeaed5330610f20dc9937c9a1d3d1'
                            '&language '
                            '=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def fetch_vote_average(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=659eeaed5330610f20dc9937c9a1d3d1'
                            '&language '
                            '=en-US'.format(movie_id))
    data = response.json()
    return data['vote_average']


def fetch_runtime(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=659eeaed5330610f20dc9937c9a1d3d1'
                            '&language '
                            '=en-US'.format(movie_id))
    data = response.json()
    return data['runtime']


def fetch_movies_overview(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=659eeaed5330610f20dc9937c9a1d3d1'
                            '&language '
                            '=en-US'.format(movie_id))
    data = response.json()
    return data['overview']


def fetch_genres(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=659eeaed5330610f20dc9937c9a1d3d1'
                            '&language '
                            '=en-US'.format(movie_id))
    data = response.json()
    return [genre['name'] for genre in data['genres']]


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = sim[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    recommended_movies_overview = []
    recommended_vote_average = []
    recommended_runtime = []
    recommended_genres = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        # fetch poster and description from API
        poster_path = fetch_poster(movie_id)
        overview = fetch_movies_overview(movie_id)
        vote_average = fetch_vote_average(movie_id)
        runtime = fetch_runtime(movie_id)
        genres = fetch_genres(movie_id)[:2]

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(poster_path)
        recommended_movies_overview.append(overview)
        recommended_vote_average.append(vote_average)
        recommended_runtime.append(runtime)
        recommended_genres.append(genres)

    return recommended_movies, recommended_movies_poster, recommended_movies_overview, \
           recommended_vote_average, recommended_runtime, recommended_genres


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

sim = pickle.load(open('sim.pkl', 'rb'))
st.markdown("<h1 style='text-align: center;'>Cine Vista</h1>", unsafe_allow_html=True)

st.markdown("<div style='text-align: center;'>"
            "<h7>Explore the magic of cinema with personalized recommendations!</h7>"
            "</div><br>", unsafe_allow_html=True)

selected_movie_name = st.selectbox(
    'Type or select a movie from the dropdown',
    movies['title'].values)

st.markdown("<style>div.Widget.row-widget.stButton {justify-content: center;}</style>", unsafe_allow_html=True)

if st.button('Recommend', key="recommend_button", help="Click to get recommendations"):
    st.markdown("<h3 style='text-align: center;'>Top 5 Recommendations</h3><br>", unsafe_allow_html=True)

    names, posters, overview, vote_average, runtime, genres = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5, gap="large")

    with col1:
        st.image(posters[0])
        st.markdown(f"<h6 style='text-align: center;'>{names[0]}</h6><hr>", unsafe_allow_html=True)
        st.write(f"Genres: {', '.join(genres[0])}")
        st.write(f"Rating: {round(vote_average[0], 1)} ⭐")
        st.write(f"Runtime: {runtime[0]} minutes")
        with st.expander("Overview"):
            st.write(overview[0])

    with col2:
        st.image(posters[1])
        st.markdown(f"<h6 style='text-align: center;'>{names[1]}</h6><hr>", unsafe_allow_html=True)
        st.write(f"Genres: {', '.join(genres[1])}")
        st.write(f"Rating: {round(vote_average[1], 1)} ⭐")
        st.write(f"Runtime: {runtime[1]} minutes")
        with st.expander("Overview"):
            st.write(overview[1])

    with col3:
        st.image(posters[2])
        st.markdown(f"<h6 style='text-align: center;'>{names[2]}</h6><hr>", unsafe_allow_html=True)
        st.write(f"Genres: {', '.join(genres[2])}")
        st.write(f"Rating: {round(vote_average[2], 1)} ⭐")
        st.write(f"Runtime: {runtime[2]} minutes")
        with st.expander("Overview"):
            st.write(overview[2])

    with col4:
        st.image(posters[3])
        st.markdown(f"<h6 style='text-align: center;'>{names[3]}</h6><hr>", unsafe_allow_html=True)
        st.write(f"Genres: {', '.join(genres[3])}")
        st.write(f"Rating: {round(vote_average[3], 1)} ⭐")
        st.write(f"Runtime: {runtime[3]} minutes")
        with st.expander("Overview"):
            st.write(overview[3])

    with col5:
        st.image(posters[4])
        st.markdown(f"<h6 style='text-align: center;'>{names[4]}</h6><hr>", unsafe_allow_html=True)
        st.write(f"Genres: {', '.join(genres[4])}")
        st.write(f"Rating: {round(vote_average[4], 1)} ⭐")
        st.write(f"Runtime: {runtime[4]} minutes")
        with st.expander("Overview"):
            st.write(overview[4])
