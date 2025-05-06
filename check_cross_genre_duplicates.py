import os
import cv2
import hashlib

DATA_DIR = "data/posters"  # Relative path from the script

def compute_hash(image_path):
    try:
        img = cv2.imread(image_path)
        if img is None:
            return None
        img = cv2.resize(img, (64, 64))  # Standard size to reduce processing
        return hashlib.md5(img.tobytes()).hexdigest()
    except:
        return None

hash_dict = {}
duplicates = []

for genre in os.listdir(DATA_DIR):
    genre_path = os.path.join(DATA_DIR, genre)
    for file in os.listdir(genre_path):
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            path = os.path.join(genre_path, file)
            img_hash = compute_hash(path)
            if img_hash:
                if img_hash in hash_dict:
                    duplicates.append((path, hash_dict[img_hash]))
                else:
                    hash_dict[img_hash] = path

# Report
if duplicates:
    print("❌ Cross-genre duplicate posters found:\n")
    for dup1, dup2 in duplicates:
        print(f"- {dup1}  ==  {dup2}")
else:
    print("✅ No cross-genre duplicates found.")