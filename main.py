import streamlit as st
import pickle
import requests


def fetch_poster(movie_id):
    try:
        url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=ea8b296fb9fc874fd6610631f650a42a&language=en-US'
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raises HTTPError for bad responses
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster"
    except Exception as e:
        print(f"[ERROR] Failed to fetch poster for movie ID {movie_id}: {e}")
        return "https://via.placeholder.com/500x750?text=Error"



# Load the data
movies = pickle.load(open("movies.pkl", "rb"))  # This is a DataFrame
similarity = pickle.load(open("similarity.pkl", "rb"))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters=[]
    for i in movie_list:
        movie_id = movies.iloc[i[0]]['movie_id']

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API:   ea8b296fb9fc874fd6610631f650a42a
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


# Streamlit UI
st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    "Select a movie you like:",
    movies['title'].values  # Use the original DataFrame
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)
    
    col1, col2, col3, col4, col5 =st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])


    with col5:
        st.text(names[4])
        st.image(posters[4])            