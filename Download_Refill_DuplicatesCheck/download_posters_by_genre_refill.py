import os
import requests
from tqdm import tqdm
import time
from dotenv import load_dotenv

# Step 1: Load TMDB API key from .env file
load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")

# Step 2: TMDB API URLs
BASE_URL = "https://api.themoviedb.org/3"
IMG_BASE = "https://image.tmdb.org/t/p/w500"

# Step 3: Genre IDs (official TMDB IDs)
GENRE_MAP = {
    "Action": 28,
    "Comedy": 35,
    "Drama": 18,
    "Romance": 10749,
    "Thriller": 53
}

# Step 4: Current poster counts after duplicate removal
CURRENT_COUNTS = {
    "Action": 466,    # Already full
    "Comedy": 408,
    "Drama": 365,
    "Romance": 374,
    "Thriller": 435
}

# Step 5: Target number of posters per genre
TARGET_COUNT = 466

# Step 6: Output directory for refills
OUTPUT_DIR = os.path.join("data", "new_posters")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Step 7: Create subfolders for genres
for genre in GENRE_MAP:
    genre_path = os.path.join(OUTPUT_DIR, genre)
    os.makedirs(genre_path, exist_ok=True)

# Step 8: Download posters
def download_posters(genre_name, genre_id, num_to_download):
    if num_to_download <= 0:
        print(f"✅ {genre_name} already has 466 posters.")
        return

    seen_ids = set()
    downloaded = 0
    page = 1

    print(f"\n📥 Refilling {genre_name} with {num_to_download} posters...")

    while downloaded < num_to_download:
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
            save_path = os.path.join(OUTPUT_DIR, genre_name, f"{movie_id}.jpg")

            # Skip if file already exists
            if os.path.exists(save_path):
                continue

            try:
                img_data = requests.get(f"{IMG_BASE}{poster_path}").content
                with open(save_path, 'wb') as handler:
                    handler.write(img_data)
                downloaded += 1
            except Exception:
                continue

            if downloaded >= num_to_download:
                break

        page += 1
        time.sleep(0.2)

    print(f"✅ Downloaded {downloaded} new posters for {genre_name}")

# Step 9: Start downloading only for genres that need refill
for genre_name, genre_id in GENRE_MAP.items():
    current_count = CURRENT_COUNTS[genre_name]
    missing_count = TARGET_COUNT - current_count

    if genre_name != "Action":
        download_posters(genre_name, genre_id, missing_count)