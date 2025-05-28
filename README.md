#  Movie Recommender System

This project builds a **content-based movie recommendation system** using the TMDB 5000 Movies Dataset. It helps users find movies similar to their favorites based on metadata such as cast, crew, genres, and keywords.

##  Dataset

- **Files Used**:
  - `tmdb_5000_movies.csv`
  - `tmdb_5000_credits.csv`
- Dataset source: [Kaggle - TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

## Objective

To recommend movies that are similar in content using features such as:
- Overview
- Cast
- Crew
- Genres
- Keywords

##  Tools & Libraries

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **NLTK** (Natural Language Toolkit)
- **Jupyter Notebook**

##  Features

- Merges movie metadata and credits into a single DataFrame.
- Extracts relevant features for content-based filtering.
- Performs preprocessing (e.g., parsing JSON-like columns).
- Converts text data into vectors using **TF-IDF** or **CountVectorizer**.
- Computes **cosine similarity** to find and rank similar movies.
- Provides a simple function to return top recommended movies.

##  Data Preprocessing

- Extracts director and top 3 cast members.
- Cleans and tokenizes keywords and genres.
- Constructs a combined "tags" column for vectorization.

##  How to Run

1. Clone this repository or download the notebook.
2. Ensure you have the required libraries installed:
   ```bash
   pip install numpy pandas scikit-learn nltk
   ```
3. Download the dataset from [this Kaggle link](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).
4. Place both CSV files (`tmdb_5000_movies.csv`, `tmdb_5000_credits.csv`) in the same directory as the notebook.
5. Open `Movie_recommender_system.ipynb` in Jupyter Notebook and run all cells.

##  Example Usage

```python
recommend("Inception")
```

Returns the top 5 movies similar to **Inception**.
