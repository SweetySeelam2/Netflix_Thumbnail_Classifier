
[![Live App - Try it Now](https://img.shields.io/badge/Live%20App-Streamlit-informational?style=for-the-badge&logo=streamlit)](https://netflixthumbnailclassifier-dl.streamlit.app/)

# 🎬 Netflix Thumbnail Genre Classification using DenseNet121

> An advanced deep learning solution to classify movie posters into genres — automating thumbnail labeling for personalized A/B testing at scale.

---

## 📌 Table of Contents

- [📌 Project Overview](#-project-overview)
- [🎯 Objective](#-objective)
- [📂 Dataset Information](#-dataset-information)
- [⚙️ Model Architecture](#️-model-architecture)
- [🧪 Training and Evaluation](#-training-and-evaluation)
- [📊 Results & Insights](#-results--insights)
- [💼 Business Impact](#-business-impact)
- [🚀 App Demo](#-app-demo)
- [🧠 Recommendations](#-recommendations)
- [📜 License](#-license)

---

## 📌 Project Overview

Netflix constantly tests thousands of thumbnail variations to optimize user engagement. However, genre tagging for posters is often manual, subjective, and time-consuming.

This project aims to automate poster genre classification using a **deep learning-based image classifier**. It can be deployed to support:

- Fast and scalable metadata tagging.
- Smart thumbnail suggestions based on genre.
- Visual personalization in A/B testing campaigns.

---

## 🎯 Objective

Build a reliable, unbiased, and scalable model that:

- Classifies movie posters into one of **five genres**: Action, Comedy, Drama, Romance, Thriller.
- Enables Netflix-like platforms to automate poster tagging and testing.
- Improves recommendation pipelines and engagement strategies.

---

## 📂 Dataset Information

- 📁 **Source**: Posters downloaded via TMDB API using genre filters.
- 🎬 **Genres**: Action, Comedy, Drama, Romance, Thriller.
- 🖼️ **Image Size**: Resized to 160x160 pixels.
- 📊 **Balanced Dataset**: 466 unique posters per genre.
- 🔗 **TMDB Dataset Source**: [The Movie Database API](https://developer.themoviedb.org/reference/discover-movie)

---

## ⚙️ Model Architecture

- ✅ **Base Model**: `DenseNet121` (pre-trained on ImageNet)
- 🔄 Transfer Learning: Last few layers fine-tuned for poster classification
- 📦 Additional Layers:
  - Global Average Pooling
  - Dropout (0.3)
  - Dense Softmax Output (5 classes)

This model was chosen due to its:
- Efficiency on CPU systems
- Better generalization vs. overfitting
- Performance on low-texture, high-color image datasets

---

## 🧪 Training and Evaluation

- 🧹 Preprocessing: Image resizing, normalization, augmentation
- 📊 Split: 80% training, 20% validation
- 🧠 Optimizer: Adam
- 🧮 Loss: Categorical Crossentropy
- 🔁 Epochs: 15  
- 🛑 EarlyStopping: Based on validation loss

---

## 📊 Results & Insights

### ✅ **Validation Accuracy**: `~37%`
### ✅ **Macro F1 Score**: `0.37`
### ✅ **Best Performing Genre**: Comedy (F1 = 0.47), Romance (F1 = 0.44)

#### 📈 Accuracy & Loss Curves:
- Training and validation accuracies steadily improved.
- Minimal overfitting observed due to balanced dataset and early stopping.

#### 📉 Confusion Matrix:
- Romance and Comedy show the strongest predictive power.
- Drama and Thriller are often confused, likely due to visual similarity.

#### 📑 Classification Report Snapshot:

| Genre   | Precision | Recall | F1-score |
|---------|-----------|--------|----------|
| Action  | 0.41      | 0.41   | 0.41     |
| Comedy  | 0.48      | 0.46   | 0.47     |
| Drama   | 0.25      | 0.22   | 0.23     |
| Romance | 0.39      | 0.52   | 0.44     |
| Thriller| 0.31      | 0.27   | 0.29     |

---

## 💼 Business Impact

If this model or an improved version were adopted by Netflix:

- ✅ **Automated Metadata Tagging**: 90% faster thumbnail genre classification
- 📈 **CTR Boost**: Expected uplift of 5–10% from genre-personalized thumbnails
- 💰 **Estimated Annual Impact**: $60M–$100M in engagement-driven revenue
- 🧠 **Decision Support**: Reduces subjective bias in manual labeling

---

## 🚀 App Demo

You can interactively test the model here:

👉 [**Live Streamlit App**](https://netflixthumbnailclassifier-dl.streamlit.app/)

Features:
- 📤 Upload your own poster image
- 📁 Use sample posters from our dataset
- ⚡ Instant prediction with genre + confidence
- 📊 Model architecture and overview

---

## 🧠 Recommendations for Future Work

- 🔄 **Multi-label Classification** (movies often belong to more than one genre)
- 🧩 **Multi-modal Learning**: Combine poster with movie metadata (title, synopsis)
- 🔍 **Model Upgrade**: Use hybrid CNN + Vision Transformers
- 📈 **Dataset Expansion**: Grow to 10,000+ posters using TMDB/IMDb

---

## 👩‍💼 About the Author    

**Sweety Seelam** – Business Analyst and aspiring Data Scientist                                                                                  
| Passionate about building end-to-end ML solutions for real-world problems in media and entertainment |                                                                                                                                                                      

Email: sweetyseelam2@gmail.com

🔗 **Profile Links**                                                                                                    
[Portfolio Website](https://sweetyseelam2.github.io/SweetySeelam.github.io/)
 
[LinkedIn](https://www.linkedin.com/in/sweetyrao670/)

[GitHub](https://github.com/SweetySeelam2)

---

## 📜 License

This project is licensed under the **MIT License**.

© 2025 Sweety Seelam
