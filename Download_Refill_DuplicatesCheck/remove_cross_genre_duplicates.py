import os
import hashlib
from collections import defaultdict

genres_path = "../data/posters"
hash_dict = defaultdict(list)
deleted_count = 0

def get_image_hash(file_path):
    with open(file_path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

# STEP 1: Build hash map
for genre in sorted(os.listdir(genres_path)):
    genre_path = os.path.join(genres_path, genre)
    for file in os.listdir(genre_path):
        file_path = os.path.join(genre_path, file)
        if file_path.endswith(".jpg"):
            img_hash = get_image_hash(file_path)
            hash_dict[img_hash].append(file_path)

# STEP 2: Delete duplicates beyond first occurrence
for img_hash, paths in hash_dict.items():
    if len(paths) > 1:
        keep = paths[0]  # Keep the first one
        for duplicate in paths[1:]:
            try:
                os.remove(duplicate)
                print(f"🗑️ Removed duplicate: {duplicate}")
                deleted_count += 1
            except Exception as e:
                print(f"⚠️ Error deleting {duplicate}: {e}")

print(f"\n✅ Finished. Total duplicates removed: {deleted_count}")