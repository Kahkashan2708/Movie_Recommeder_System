#  Movie Recommender System

This project is a **content-based movie recommendation system** built with **Streamlit**. It suggests movies similar to your favorites using metadata such as cast, crew, genres, and keywords from the TMDB 5000 Movies Dataset.

**Live App**: [Try the Movie Recommender Now!](https://movierecommedersystem-josclp2gzkpxiesgj7aljd.streamlit.app/)

---

##  Dataset

- **Source**: [TMDB 5000 Movie Dataset on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- **Files Used**:
  - `tmdb_5000_movies.csv`
  - `tmdb_5000_credits.csv`

---

## Objective

Recommend similar movies based on:
- Overview (plot description)
- Cast
- Director (crew)
- Genres
- Keywords

---

## Data Analysis (EDA)

The project includes an in-depth analysis notebook:

 **Notebook**: `Movie_recommender_system.ipynb`

Key insights covered:
- Distribution of movies by genre
- Most common actors, directors, and production companies
- Trends in release years
- Preprocessing of text data and construction of "tags"

Run the notebook locally or on Google Colab to understand the logic behind the system and preprocessing techniques.

---

##  Tech Stack & Tools

- **Python**
- **Streamlit** – for web UI
- **Pandas, NumPy** – for data manipulation
- **Scikit-learn** – for text vectorization & similarity computation
- **NLTK** – for tokenization
- **Pickle** – for saving data and similarity matrix
- **TMDB API** – to fetch movie posters
- **Matplotlib, Seaborn, WordCloud** – for visualization (in the notebook)

---

##  Key Features

- Clean and professional web interface using **Streamlit**
- Search for a movie and get **top 5 similar recommendations**
- Movie **posters dynamically fetched** from TMDB using their API
- Fast and scalable with precomputed **cosine similarity matrix**
- Includes **analysis notebook** explaining EDA and model building

---

##  Project Structure

```
 Movie_Recommender_System/
├── main.py                       # Streamlit app script
├── Movie_recommender_system.ipynb # Notebook for EDA and model building
├── movies.pkl                    # Pickled DataFrame of movie metadata
├── similarity.pbz2               # Compressed similarity matrix
├── requirements.txt              # Python dependencies
└── README.md                     # Project overview (this file)
```

---

##  How to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/movie-recommender-system.git
   cd movie-recommender-system
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**:
   ```bash
   streamlit run main.py
   ```

---

##  Files Explained

| File                          | Purpose                                          |
|-------------------------------|--------------------------------------------------|
| `main.py`                     | Streamlit web app code                          |
| `Movie_recommender_system.ipynb` | Jupyter notebook for EDA and model pipeline   |
| `movies.pkl`                  | Pickled DataFrame with movie metadata           |
| `similarity.pbz2`             | Compressed cosine similarity matrix             |
| `requirements.txt`            | List of required Python libraries               |

---

##  API Integration

Posters are fetched using the **TMDB API**:

- API Used: [The Movie Database API](https://developers.themoviedb.org/)
- You can replace the API key in `main.py` or store it securely via Streamlit Secrets.

---




## Credits

- Dataset: [Kaggle - TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- Poster API: [TMDB API](https://www.themoviedb.org/)
- UI: Built with [Streamlit](https://streamlit.io/)

---

##  Show Your Support

If you like this project:
-  Star the repo
-  Share it with friends
-  Fork and build on top of it!

---

##  Author

**Kahkashan** – *Data Science & ML Enthusiast*  
 [LinkedIn](https://www.linkedin.com/in/kahkashan-manzoor-663384287/)
