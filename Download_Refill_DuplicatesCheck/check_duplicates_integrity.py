import os
import hashlib

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
                duplicates.append((file_path, hashes[file_hash]))
            else:
                hashes[file_hash] = file_path
        except:
            continue

# ✅ Print Results
print(f"🔍 Total duplicate files found across all genres: {len(duplicates)}")
for dup in duplicates[:10]:  # First 10 only
    print(f"🛑 Duplicate: {dup[0]} == {dup[1]}")