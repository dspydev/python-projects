# Introduction

In this case study, I developed a content-based movie recommendation system for horror movies available on a streaming platform, using the netflixData.csv dataset from Kaggle (https://www.kaggle.com/datasets/satpreetmakhija/netflix-movies-and-tv-shows-2021). The goal was to provide personalized recommendations for users based on their input movie choice. I performed data cleaning, feature extraction, and computed similarity scores to recommend movies.

# Problems

The major problems I addressed in this code include:

- Cleaning and preprocessing the raw movie dataset to make it suitable for further analysis.
- Identifying relevant features that can help in building a recommendation system.
- Calculating similarity scores between the input movie and other movies in the dataset.
- Visualizing the top recommended movies along with their similarity scores.

# Solutions

I implemented the following solutions to tackle the problems mentioned above:

- I created a clean_dataframe function to clean the dataset by removing special characters, converting data types, and handling duplicates and missing values.
- I combined the 'Genres' and 'Description' columns to create a single text feature, which was then converted into a TF-IDF matrix using the TfidfVectorizer class from the sklearn library.
- I calculated cosine similarity scores between all the movies in the dataset using the linear_kernel function from the sklearn library. The top 10 movies with the highest similarity scores were recommended.
- I plotted a horizontal bar chart to visualize the top 10 recommended movies along with their similarity scores. I also provided a short explanation of the graph in a separate subplot.

<p align="center">
  <img src="https://user-images.githubusercontent.com/115745200/225913214-d3ae3a30-ea4e-4997-990a-bc5e20445dda.png" alt="Your image description">
</p>

A similarity score measures how alike two items are, such as movies, based on their features. In this project, the similarity score compares movies using genres and descriptions.

Cosine similarity is used to calculate the score, which ranges from -1 (completely dissimilar) to 1 (identical). It measures the angle between two vectors, in this case, the TF-IDF vectors of movie features.

Higher similarity scores mean the recommended movies are more similar to the input movie in terms of genre and description.

# Conclusion

This case study demonstrates my implementation of a content-based movie recommendation system using Python and the sklearn library. The code successfully recommends the top 10 movies based on the input movie and provides a visualization of the recommendations along with their similarity scores.

# Next steps

To improve the recommendation system, I can take the following actions:

- Experiment with different text preprocessing techniques, such as stemming or lemmatization, to improve the quality of the TF-IDF matrix.
- Incorporate additional features, such as actors, directors, and movie ratings, to enhance the recommendation quality.
- Evaluate the performance of the recommendation system using appropriate evaluation metrics, such as precision, recall, or F1 score.
- Implement a hybrid recommendation system that combines content-based and collaborative filtering methods to provide even more accurate recommendations.
- Incorporate user feedback to refine the recommendation model over time.
