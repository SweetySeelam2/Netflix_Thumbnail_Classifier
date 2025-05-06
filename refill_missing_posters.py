import os
import requests
import time
from tqdm import tqdm
from dotenv import load_dotenv
from PIL import Image
import hashlib

# Load TMDB API Key
load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")

BASE_URL = "https://api.themoviedb.org/3"
IMG_BASE = "https://image.tmdb.org/t/p/w500"

GENRE_MAP = {
    "Thriller": 53
}

POSTER_DIR = os.path.join("data", "posters")
REFILL_DIR = os.path.join("data", "new_posters")
TARGET_COUNT = 466

# Create new_posters folders if not exist
for genre in GENRE_MAP:
    os.makedirs(os.path.join(REFILL_DIR, genre), exist_ok=True)

# Hashing for uniqueness
def get_image_hash(image_path):
    with Image.open(image_path) as img:
        img = img.convert("RGB").resize((64, 64))
        return hashlib.md5(img.tobytes()).hexdigest()

def get_all_existing_hashes():
    all_hashes = set()
    for genre_folder in [POSTER_DIR, REFILL_DIR]:
        for genre in os.listdir(genre_folder):
            genre_path = os.path.join(genre_folder, genre)
            for file in os.listdir(genre_path):
                file_path = os.path.join(genre_path, file)
                if file_path.lower().endswith(".jpg"):
                    try:
                        hash_val = get_image_hash(file_path)
                        all_hashes.add(hash_val)
                    except:
                        continue
    return all_hashes

def download_unique_posters(genre_name, genre_id, need_count):
    print(f"\n📥 Refilling {genre_name} → Need {need_count} more unique posters")
    existing_hashes = get_all_existing_hashes()
    refill_path = os.path.join(REFILL_DIR, genre_name)

    page = 1
    added = 0
    seen_ids = set()

    while added < need_count:
        url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}&page={page}"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"⚠️ API error for {genre_name} page {page}")
            break

        results = response.json().get("results", [])
        if not results:
            break

        for movie in results:
            poster_path = movie.get("poster_path")
            movie_id = movie["id"]

            if not poster_path or movie_id in seen_ids:
                continue

            seen_ids.add(movie_id)
            img_url = f"{IMG_BASE}{poster_path}"
            save_path = os.path.join(refill_path, f"{movie_id}.jpg")

            try:
                img_data = requests.get(img_url).content
                with open(save_path, "wb") as f:
                    f.write(img_data)

                hash_val = get_image_hash(save_path)
                if hash_val in existing_hashes:
                    os.remove(save_path)
                    continue

                existing_hashes.add(hash_val)
                added += 1

                if added >= need_count:
                    break
            except:
                continue

        page += 1
        time.sleep(0.25)

    print(f"✅ Added {added} unique posters to {genre_name}")

# Manually force refill for just 1 poster
for genre, genre_id in GENRE_MAP.items():
    print(f"⚙️ Forcing refill of 1 poster for {genre}")
    download_unique_posters(genre, genre_id, 1)