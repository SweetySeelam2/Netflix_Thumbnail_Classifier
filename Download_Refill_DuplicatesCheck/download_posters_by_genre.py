import os
import requests
from tqdm import tqdm
import time

# Step 1: Add your TMDB API key
API_KEY = "5d0cdb5570fbdb7af16b7d3089956042"  # 🔁 Replace this with your actual key

# Step 2: TMDB API URLs
BASE_URL = "https://api.themoviedb.org/3"
IMG_BASE = "https://image.tmdb.org/t/p/w500"

# Step 3: Define target genres and their TMDB IDs
GENRE_MAP = {
    "Action": 28,
    "Comedy": 35,
    "Drama": 18,
    "Romance": 10749,
    "Thriller": 53
}

# Step 4: Set output folder path
OUTPUT_DIR = r"C:\Users\sweet\Desktop\DataScience\Github projects\Deployment files\DL-Recommendation-streamlit\data\posters"

# Step 5: Create folders for each genre
for genre in GENRE_MAP:
    os.makedirs(os.path.join(OUTPUT_DIR, genre), exist_ok=True)

# Step 6: Download posters from TMDB API
def download_posters(genre_name, genre_id, max_count=500):
    page = 1
    downloaded = 0
    seen_ids = set()
    print(f"\n📥 Downloading posters for: {genre_name}")

    while downloaded < max_count:
        url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}&page={page}"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"⚠️ Failed to fetch page {page} for {genre_name}")
            break

        movies = response.json().get('results', [])

        if not movies:
            break

        for movie in movies:
            movie_id = movie['id']
            poster_path = movie.get('poster_path')

            if not poster_path or movie_id in seen_ids:
                continue

            seen_ids.add(movie_id)
            img_url = f"{IMG_BASE}{poster_path}"
            save_path = os.path.join(OUTPUT_DIR, genre_name, f"{movie_id}.jpg")

            try:
                img_data = requests.get(img_url).content
                with open(save_path, 'wb') as handler:
                    handler.write(img_data)
                downloaded += 1
            except:
                continue

            if downloaded >= max_count:
                break

        page += 1
        time.sleep(0.25)

    print(f"✅ Downloaded {downloaded} posters for {genre_name}")

# Step 7: Loop through all genres
for genre_name, genre_id in GENRE_MAP.items():
    download_posters(genre_name, genre_id, max_count=500)