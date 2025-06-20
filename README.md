# Movie Recommender System

This project is a **content-based movie recommendation system** built with **Streamlit**. It suggests movies similar to your favorites using metadata such as cast, crew, genres, and keywords from the TMDB 5000 Movies Dataset.

 **Live App**: [Try the Movie Recommender Now!](https://movierecommedersystem-josclp2gzkpxiesgj7ajld.streamlit.app)

---

##  Dataset

- **Source**: [TMDB 5000 Movie Dataset on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- **Files Used**:
  - `tmdb_5000_movies.csv`
  - `tmdb_5000_credits.csv`

---

##  Objective

Recommend similar movies based on:
- Overview (plot description)
- Cast
- Director (crew)
- Genres
- Keywords

---

## 🛠️ Tech Stack & Tools

- **Python**
- **Streamlit** – for web UI
- **Pandas, NumPy** – for data manipulation
- **Scikit-learn** – for text vectorization & similarity computation
- **NLTK** – for tokenization
- **Pickle** – for saving data and similarity matrix
- **TMDB API** – to fetch movie posters

---

##  Key Features

- Clean and professional web interface using **Streamlit**
- Search for a movie and get **top 5 similar recommendations**
- Movie **posters dynamically fetched** from TMDB using their API
- Fast and scalable with precomputed **cosine similarity matrix**
- Uses **compressed model file** (`similarity.pbz2`) to reduce file size

---

##  Project Structure

```
 movie-recommender-system/
├── main.py                  # Streamlit app script
├── movies.pkl               # Pickled DataFrame of movie metadata
├── similarity.pbz2          # Compressed similarity matrix
├── requirements.txt         # Python dependencies
└── README.md                # Project overview (this file)
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

| File                | Purpose                                          |
|---------------------|--------------------------------------------------|
| `main.py`           | Streamlit web app code                          |
| `movies.pkl`        | Pickled DataFrame with movie metadata           |
| `similarity.pbz2`   | Compressed cosine similarity matrix             |
| `requirements.txt`  | List of required Python libraries               |

---

##  API Integration

Posters are fetched using the **TMDB API**:

- API Used: [The Movie Database API](https://developers.themoviedb.org/)
- You can replace the API key in `main.py` or store it securely via Streamlit Secrets.

---

##  Example Output

![App Screenshot](https://your-screenshot-link.com/example.png) <!-- Replace with real image URL if available -->

---

##  Future Improvements

- Add collaborative filtering (user-based recommendations)
- Include genre filters or search by keyword
- Store user history & feedback
- Add ratings and reviews

---

##  Credits

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

## Author

**Kahkashan** – *Data Science & ML Enthusiast*  
💼 [LinkedIn](https://www.linkedin.com) | 📝 [Portfolio](https://your-portfolio-link.com)

