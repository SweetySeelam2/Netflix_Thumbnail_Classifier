# check_and_remove_duplicates.py
import os
import hashlib

# Update this path to your local folder path
poster_dir = r"C:\Users\sweet\Desktop\DataScience\Github projects\Deployment files\DL-Recommendation-streamlit\data\posters"
hashes = {}
duplicates = []

for genre in os.listdir(poster_dir):
    genre_path = os.path.join(poster_dir, genre)
    if not os.path.isdir(genre_path):
        continue
    for filename in os.listdir(genre_path):
        file_path = os.path.join(genre_path, filename)
        try:
            with open(file_path, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
            if file_hash in hashes:
                duplicates.append(file_path)
            else:
                hashes[file_hash] = file_path
        except:
            continue

print(f"🧹 Removing {len(duplicates)} duplicate images...")
for file_path in duplicates:
    try:
        os.remove(file_path)
        print(f"❌ Removed: {file_path}")
    except:
        print(f"⚠️ Could not remove: {file_path}")

print("✅ Duplicate cleanup completed.")