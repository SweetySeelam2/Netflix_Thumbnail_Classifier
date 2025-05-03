import os
import hashlib
from collections import defaultdict

# Path to the genre folders
POSTER_DIR = "data/posters"
valid_exts = (".jpg", ".jpeg", ".png")

# Map image hash to file paths
hash_dict = defaultdict(list)

def compute_hash(filepath):
    """Generate MD5 hash of file content"""
    with open(filepath, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

# Scan and group images by hash
for genre in os.listdir(POSTER_DIR):
    genre_path = os.path.join(POSTER_DIR, genre)
    if os.path.isdir(genre_path):
        for file in os.listdir(genre_path):
            if file.lower().endswith(valid_exts):
                full_path = os.path.join(genre_path, file)
                try:
                    img_hash = compute_hash(full_path)
                    hash_dict[img_hash].append(full_path)
                except Exception as e:
                    print(f"⚠️ Error reading {full_path}: {e}")

# Remove duplicates (keep one file per hash)
removed_count = 0
for file_list in hash_dict.values():
    if len(file_list) > 1:
        # Keep the first file, delete the rest
        for duplicate_file in file_list[1:]:
            try:
                os.remove(duplicate_file)
                print(f"🗑 Removed duplicate: {duplicate_file}")
                removed_count += 1
            except Exception as e:
                print(f"❌ Failed to delete {duplicate_file}: {e}")

if removed_count == 0:
    print("✅ No duplicates to remove. Dataset is clean.")
else:
    print(f"\n✅ Removed {removed_count} duplicate images from the dataset.")