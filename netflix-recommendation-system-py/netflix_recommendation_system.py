!pip install pandas
!pip install matplotlib
!pip install scikit-learn

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def clean_dataframe(data):
    # Remove special characters and convert data types
    # Replace '#' in Title and '/10' in Imdb Score with an empty string
    data.replace({'Title': {'#': ''},
                  'Imdb Score': {'/10': ''}}, inplace=True, regex=True)
    # Convert Date Added to datetime format and keep only the date part
    data['Date Added'] = pd.to_datetime(data['Date Added']).dt.strftime('%Y-%m-%d')
    # Convert Imdb Score to float data type
    data['Imdb Score'] = data['Imdb Score'].astype(float)
    # Remove duplicate rows
    data.drop_duplicates(inplace=True)
    # Remove rows with missing values
    data.dropna(inplace=True)

    return data

def create_content_based_recommendation_with_scores(data, title, top_n=10):
    # Filter data to keep only horror movies and series
    horror_data = data[data['Genres'].str.contains('Horror', na=False)].copy()

    # Initialize a TF-IDF vectorizer with English stop words
    tfidf = TfidfVectorizer(stop_words='english')
    # Fill missing Genre and Description values with empty strings
    horror_data['Genres'] = horror_data['Genres'].fillna('')
    horror_data['Description'] = horror_data['Description'].fillna('')
    # Combine Genres and Descriptions into a single text
    combined_text = horror_data['Genres'] + " " + horror_data['Description']
    # Compute TF-IDF vectors for the combined text
    tfidf_matrix = tfidf.fit_transform(combined_text)

    # Compute cosine similarity scores between all movies in the horror_data DataFrame
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    # Create a mapping between movie titles and their indices in the DataFrame
    indices = pd.Series(horror_data.index, index=horror_data['Title']).drop_duplicates()

    # Get the index of the movie with the given title
    idx = indices[title]

    # Get similarity scores for the movie with all other movies in the DataFrame
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort movies based on their similarity scores in descending order
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the indices of the most similar movies
    sim_indices = [i[0] for i in sim_scores]

    # Return the top_n most similar movies, excluding the input movie, with their similarity scores
    return horror_data['Title'].iloc[sim_indices].drop(idx).head(top_n).reset_index(drop=True), [score for _, score in sim_scores[:top_n]]

# Generate top 10 content-based recommendations using the cleaned movie data
recommended_movies, similarity_scores = create_content_based_recommendation_with_scores(data_cleaned, title, top_n=10)

# Create a DataFrame with recommended movie titles and their similarity scores
recommended_movies_with_scores = pd.DataFrame({'Title': recommended_movies, 'Similarity Score': similarity_scores})

# Create a figure with two subplots
fig = plt.figure(figsize=(14, 6))

# Create a horizontal bar chart to visualize the recommendations in the left subplot
ax1 = fig.add_subplot(121)
bars = ax1.barh(recommended_movies_with_scores['Title'][::-1], recommended_movies_with_scores['Similarity Score'][::-1], color='dodgerblue')
ax1.set_xlabel('Similarity Score')
ax1.set_ylabel('Recommended Movies')
ax1.set_title(f"Top 10 Recommended Movies for '{title}'")
ax1.set_xlim(0, max(recommended_movies_with_scores['Similarity Score']) * 1.3)

# Add value labels to the bars
for bar in bars:
    ax1.text(bar.get_width() + 0.005, bar.get_y() + bar.get_height() / 2, f"{bar.get_width():.2f}", va='center')

# Add a short explanation to the right subplot
ax2 = fig.add_subplot(122)
ax2.axis('off')
explanation_text = (
    "This graph shows the top 10\n"
    "recommended movies for the\n"
    f"input title '{title}'. The\n"
    "similarity scores indicate\n"
    "how closely the recommended\n"
    "movies match the content of\n"
    f"'{title}'."
)
ax2.text(0, 0.5, explanation_text, fontsize=12, ha="left", va="center")

plt.tight_layout()
plt.show()
