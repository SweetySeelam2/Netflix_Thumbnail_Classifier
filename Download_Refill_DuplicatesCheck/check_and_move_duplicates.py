import os
import hashlib
import shutil
from collections import defaultdict

# Path to poster folders
POSTER_DIR = "data/posters"
DUPLICATE_DIR = "data/duplicates"

# Supported formats
valid_exts = (".jpg", ".jpeg", ".png")

# Create duplicate folder if it doesn't exist
os.makedirs(DUPLICATE_DIR, exist_ok=True)

# Store hash -> list of file paths
hash_dict = defaultdict(list)

def compute_hash(filepath):
    """Return MD5 hash of the file content"""
    with open(filepath, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

# Walk through each genre folder
for genre in os.listdir(POSTER_DIR):
    genre_path = os.path.join(POSTER_DIR, genre)
    if os.path.isdir(genre_path):
        for file in os.listdir(genre_path):
            if file.lower().endswith(valid_exts):
                file_path = os.path.join(genre_path, file)
                try:
                    img_hash = compute_hash(file_path)
                    hash_dict[img_hash].append(file_path)
                except Exception as e:
                    print(f"⚠️ Error reading {file_path}: {e}")

# Process duplicates
print("\n🔍 Checking for duplicates...\n")
duplicates_found = False

for file_list in hash_dict.values():
    if len(file_list) > 1:
        duplicates_found = True
        print("❗ Duplicate found:")
        for path in file_list:
            print("   -", path)

        # Move one copy to duplicates/
        dup_file = file_list[0]
        new_name = os.path.basename(dup_file)
        target_path = os.path.join(DUPLICATE_DIR, new_name)

        counter = 1
        # Avoid overwrite
        while os.path.exists(target_path):
            name, ext = os.path.splitext(new_name)
            target_path = os.path.join(DUPLICATE_DIR, f"{name}_{counter}{ext}")
            counter += 1

        shutil.copy2(dup_file, target_path)
        print(f"   👉 Moved to: {target_path}\n")

if not duplicates_found:
    print("✅ No duplicates found. All images are unique.")
else:
    print(f"\n✅ Review moved samples inside: {DUPLICATE_DIR}")