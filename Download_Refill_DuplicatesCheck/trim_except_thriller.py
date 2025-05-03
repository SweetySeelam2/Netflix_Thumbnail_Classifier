import os
import random

# ✅ Your poster root directory
poster_dir = r"C:\Users\sweet\Desktop\DataScience\Github projects\Deployment files\DL-Recommendation-streamlit\data\posters"
TARGET_COUNT = 466

for genre in os.listdir(poster_dir):
    if genre.lower() == "thriller":
        print(f"✅ Skipping {genre} (already has 466)")
        continue

    genre_path = os.path.join(poster_dir, genre)
    if not os.path.isdir(genre_path):
        continue

    images = [f for f in os.listdir(genre_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

    if len(images) > TARGET_COUNT:
        to_delete = random.sample(images, len(images) - TARGET_COUNT)
        for filename in to_delete:
            os.remove(os.path.join(genre_path, filename))
        print(f"✂️ Trimmed {genre} to {TARGET_COUNT} images.")
    elif len(images) < TARGET_COUNT:
        print(f"⚠️ {genre} has only {len(images)} images — skipping.")
    else:
        print(f"✅ {genre} already has exactly {TARGET_COUNT} images.")