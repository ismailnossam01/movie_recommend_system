import streamlit as st
import pandas as pd
import requests
import pickle
import time

# Load the processed data and similarity matrix
@st.cache_resource
def load_data():
    with open('movie_data.pkl', 'rb') as file:
        movies, cosine_sim = pickle.load(file)
    return movies, cosine_sim

movies, cosine_sim = load_data()

# Function to get movie recommendations
def get_recommendations(title, cosine_sim=cosine_sim):
    try:
        idx = movies[movies['title'] == title].index[0]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]  # Get top 10 similar movies
        movie_indices = [i[0] for i in sim_scores]
        return movies[['title', 'movie_id']].iloc[movie_indices]
    except IndexError:
        st.error("Movie not found in database!")
        return pd.DataFrame()

# Fetch movie poster from TMDB API with error handling and retry logic
def fetch_poster(movie_id, retries=3, delay=1):
    api_key = '4c1520622edd734c21f68a0e28a235c1'  # Replace with your actual TMDB API key
    
    if not api_key or api_key == 'YOUR_API_KEY_HERE':
        return "https://via.placeholder.com/500x750?text=No+API+Key"
    
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()  # Raise an error for bad status codes
            data = response.json()
            
            if 'poster_path' in data and data['poster_path']:
                poster_path = data['poster_path']
                full_path = f"https://image.tmdb.org/t/p/w500{poster_path}"
                return full_path
            else:
                return "https://via.placeholder.com/500x750?text=No+Poster"
                
        except requests.exceptions.ConnectionError:
            if attempt < retries - 1:
                time.sleep(delay)
                continue
            else:
                st.warning(f"Connection error for movie ID {movie_id}")
                return "https://via.placeholder.com/500x750?text=Connection+Error"
                
        except requests.exceptions.Timeout:
            if attempt < retries - 1:
                time.sleep(delay)
                continue
            else:
                st.warning(f"Timeout for movie ID {movie_id}")
                return "https://via.placeholder.com/500x750?text=Timeout"
                
        except requests.exceptions.RequestException as e:
            st.warning(f"Error fetching poster: {str(e)}")
            return "https://via.placeholder.com/500x750?text=Error"
    
    return "https://via.placeholder.com/500x750?text=No+Poster"

# Streamlit UI
st.title("🎬 Movie Recommendation System")
st.write("Select a movie to get personalized recommendations!")

# Movie selection
selected_movie = st.selectbox("Select a movie:", movies['title'].values)

if st.button('Recommend', type="primary"):
    with st.spinner('Finding recommendations...'):
        recommendations = get_recommendations(selected_movie)
        
        if not recommendations.empty:
            st.success(f"Top 10 movies similar to **{selected_movie}**:")
            
            # Create a 2x5 grid layout
            for i in range(0, 10, 5):  # Loop over rows (2 rows, 5 movies each)
                cols = st.columns(5)  # Create 5 columns for each row
                for col, j in zip(cols, range(i, i+5)):
                    if j < len(recommendations):
                        movie_title = recommendations.iloc[j]['title']
                        movie_id = recommendations.iloc[j]['movie_id']
                        
                        with col:
                            poster_url = fetch_poster(movie_id)
                            st.image(poster_url, use_container_width=True)
                            st.markdown(f"**{movie_title}**")
        else:
            st.error("Could not generate recommendations. Please try another movie.")

# Add footer
st.markdown("---")
st.markdown("*Powered by TMDB API*")