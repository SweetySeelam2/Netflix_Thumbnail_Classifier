import os
import shutil
import hashlib
from tqdm import tqdm

# Define paths
POSTERS_DIR = os.path.join("data", "posters")
REFILL_DIR = os.path.join("data", "new_posters")
TARGET_COUNT = 466

# Step 1: Get all existing hashes from main poster dataset (across all genres)
def get_existing_hashes():
    hashes = set()
    for genre_folder in os.listdir(POSTERS_DIR):
        genre_path = os.path.join(POSTERS_DIR, genre_folder)
        for filename in os.listdir(genre_path):
            file_path = os.path.join(genre_path, filename)
            if os.path.isfile(file_path):
                with open(file_path, "rb") as f:
                    hash_val = hashlib.md5(f.read()).hexdigest()
                    hashes.add(hash_val)
    return hashes

# Step 2: Merge only unique posters from refill into main
def merge_unique_posters():
    existing_hashes = get_existing_hashes()

    for genre in os.listdir(REFILL_DIR):
        src_folder = os.path.join(REFILL_DIR, genre)
        dest_folder = os.path.join(POSTERS_DIR, genre)

        current_count = len(os.listdir(dest_folder))
        needed = TARGET_COUNT - current_count

        print(f"\n📂 Merging for {genre} → Needs {needed} more")

        added = 0
        for file in tqdm(os.listdir(src_folder)):
            if added >= needed:
                break

            src_path = os.path.join(src_folder, file)
            with open(src_path, "rb") as f:
                file_hash = hashlib.md5(f.read()).hexdigest()

            if file_hash in existing_hashes:
                continue  # Skip duplicate

            shutil.copy2(src_path, os.path.join(dest_folder, file))
            existing_hashes.add(file_hash)
            added += 1

        print(f"✅ {genre} now has {current_count + added} posters.")

# Run the merge process
if __name__ == "__main__":
    merge_unique_posters()