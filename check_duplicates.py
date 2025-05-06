import os
from PIL import Image
import imagehash

genres_path = "data/posters"  # make sure this matches your project path
duplicates_found = False

for genre in os.listdir(genres_path):
    print(f"\n🔍 Checking genre: {genre}")
    hashes = {}
    genre_folder = os.path.join(genres_path, genre)
    for filename in os.listdir(genre_folder):
        filepath = os.path.join(genre_folder, filename)
        try:
            with Image.open(filepath) as img:
                hash_val = imagehash.phash(img)
                if hash_val in hashes:
                    print(f"⚠️ Duplicate found in '{genre}': {filename} == {hashes[hash_val]}")
                    duplicates_found = True
                else:
                    hashes[hash_val] = filename
        except Exception as e:
            print(f"❌ Error reading {filename}: {e}")

if not duplicates_found:
    print("\n✅ No duplicate posters found in any genre.")