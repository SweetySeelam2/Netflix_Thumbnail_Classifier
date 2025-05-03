import os
from download_posters_by_genre import download_poster_images

# ✅ 1. Set your poster root directory
poster_root = r"C:\Users\sweet\Desktop\DataScience\Github projects\Deployment files\DL-Recommendation-streamlit\data\posters"

# ✅ 2. Set genre names and their TMDB genre IDs
genre_ids = {
    'Action': 28,
    'Comedy': 35,
    'Drama': 18,
    'Romance': 10749,
    'Thriller': 53
}

# ✅ 3. Define your target count per genre
target_count = 500

# ✅ 4. Loop through each genre and check how many more images are needed
for genre, genre_id in genre_ids.items():
    genre_path = os.path.join(poster_root, genre)
    if os.path.exists(genre_path):
        current_count = len([f for f in os.listdir(genre_path) if f.endswith(('.jpg', '.jpeg', '.png'))])
    else:
        current_count = 0
        os.makedirs(genre_path, exist_ok=True)

    remaining = target_count - current_count

    if remaining > 0:
        print(f"\n📥 Downloading {remaining} posters for {genre} (genre_id: {genre_id})")
        download_poster_images(genre, genre_id, count=remaining)
    else:
        print(f"✅ {genre} already has {current_count} posters (no action needed)")
