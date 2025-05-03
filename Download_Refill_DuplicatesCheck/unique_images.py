import os

poster_root = r"C:\Users\sweet\Desktop\DataScience\Github projects\Deployment files\DL-Recommendation-streamlit\data\posters"
genres = os.listdir(poster_root)

for genre in genres:
    genre_path = os.path.join(poster_root, genre)
    if os.path.isdir(genre_path):
        count = len([f for f in os.listdir(genre_path) if f.endswith(('.jpg', '.jpeg', '.png'))])
        print(f"{genre}: {count} images")