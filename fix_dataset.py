import os

# Your poster dataset folder
POSTER_DIR = r"C:\Users\sweet\Desktop\DataScience\Github projects\Deployment files\DL-Recommendation-streamlit\data\posters"
MAX_IMAGES = 466

print("\n🔧 Fixing poster folders...")

for genre in os.listdir(POSTER_DIR):
    genre_path = os.path.join(POSTER_DIR, genre)
    if not os.path.isdir(genre_path):
        continue

    images = sorted([f for f in os.listdir(genre_path) if f.lower().endswith('.jpg')])

    total = len(images)
    if total > MAX_IMAGES:
        print(f"⚠️ {genre}: {total} images → trimming to {MAX_IMAGES}")
        extras = images[MAX_IMAGES:]
        for file in extras:
            os.remove(os.path.join(genre_path, file))
        print(f"✅ {genre}: Trimmed to {MAX_IMAGES} images.")
    elif total < MAX_IMAGES:
        print(f"❌ {genre}: Only {total} images! You'll need to refill to reach {MAX_IMAGES}.")
    else:
        print(f"✅ {genre}: Already clean with {MAX_IMAGES} posters.")

print("\n✅ All folders checked and fixed.")