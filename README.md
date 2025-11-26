# 🎬 Movie Recommendation System

A content-based movie recommendation system built with Python and Streamlit that suggests similar movies based on genres, keywords, cast, and crew information.

## Features

- **Content-Based Filtering**: Recommends movies based on similarities in genres, keywords, top 3 cast members, and directors
- **Interactive UI**: Clean Streamlit interface with movie selection dropdown
- **Visual Display**: Fetches and displays movie posters from TMDB API
- **Top 10 Recommendations**: Shows 10 most similar movies in a responsive grid layout
- **Error Handling**: Robust error handling for API calls and missing data

## Technologies Used

- **Python 3.x**
- **Pandas** - Data manipulation
- **NumPy** - Numerical operations
- **Scikit-learn** - TF-IDF vectorization and cosine similarity
- **Streamlit** - Web application framework
- **Requests** - API calls to TMDB
- **Pickle** - Data serialization

## Dataset

The system uses the TMDB 5000 Movie Dataset, which includes:
- `tmdb_5000_credits.csv` - Cast and crew information
- `tmdb_5000_movies.csv` - Movie metadata, genres, and keywords

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/ismailnossam01/movie_recommend_system
cd movie-recommendation-system
```

2. **Install required packages**
```bash
pip install pandas numpy scikit-learn streamlit requests
```

3. **Download the dataset**
   - Place `tmdb_5000_credits.csv` and `tmdb_5000_movies.csv` in the project directory

4. **Get TMDB API Key**
   - Sign up at [TMDB](https://www.themoviedb.org/)
   - Get your API key from account settings
   - Replace `'4c1520622edd734c21f68a0e28a235c1'` in `app.py` with your API key

## Usage

### Step 1: Process the Data

Run the preprocessing script to generate the recommendation model:

```bash
python preprocessing.py
```

This will:
- Merge the datasets
- Extract genres, keywords, cast (top 3), and directors
- Create tags for each movie
- Calculate TF-IDF vectors and cosine similarity matrix
- Save the processed data to `movie_data.pkl`

### Step 2: Launch the Streamlit App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### Step 3: Get Recommendations

1. Select a movie from the dropdown menu
2. Click the "Recommend" button
3. View the top 10 similar movies with their posters

## How It Works

1. **Data Preprocessing**: 
   - Combines movie metadata including genres, keywords, cast, and crew
   - Creates a "tags" feature by concatenating all relevant information

2. **TF-IDF Vectorization**: 
   - Converts text tags into numerical vectors
   - Removes common English stop words

3. **Cosine Similarity**: 
   - Calculates similarity scores between all movies
   - Higher scores indicate more similar movies

4. **Recommendation**: 
   - Finds the selected movie's index
   - Retrieves top 10 most similar movies based on cosine similarity
   - Fetches posters from TMDB API for visual display

## Project Structure

```
movie-recommendation-system/
│
├── preprocessing.py          # Data processing and model creation
├── app.py                    # Streamlit web application
├── movie_data.pkl           # Generated: Processed data and similarity matrix
├── tmdb_5000_credits.csv    # Dataset: Credits information
├── tmdb_5000_movies.csv     # Dataset: Movie metadata
└── README.md                # This file
```

## Features Breakdown

### Preprocessing Script
- Merges credits and movies datasets
- Extracts relevant features (genres, keywords, top 3 actors, director)
- Creates combined tags for similarity calculation
- Saves processed data for quick loading in the app

### Streamlit App
- Caching mechanism for faster data loading
- Retry logic for API calls with timeout handling
- Responsive grid layout (2 rows × 5 columns)
- Placeholder images for missing posters
- Error messages for invalid inputs

## Troubleshooting

**Issue**: "Movie not found in database!"
- **Solution**: The movie title must match exactly as it appears in the dataset. Try selecting from the dropdown instead of typing.

**Issue**: Poster images not loading
- **Solution**: Check your TMDB API key and internet connection. The app will show placeholder images if posters can't be fetched.

**Issue**: `FileNotFoundError` for pickle file
- **Solution**: Run `preprocessing.py` first to generate `movie_data.pkl`.

## Future Improvements

- Add hybrid recommendation (collaborative + content-based)
- Include movie ratings and popularity scores
- Add user authentication and watchlist features
- Implement search functionality with fuzzy matching
- Add movie details (release date, rating, overview) on click
- Deploy to cloud platform (Heroku, Streamlit Cloud)

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Dataset from [TMDB 5000 Movie Dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata)
- Movie posters and data from [The Movie Database (TMDB)](https://www.themoviedb.org/)

## Contact

For questions or suggestions, please open an issue or submit a pull request.

---

**Happy Movie Watching! 🍿**
