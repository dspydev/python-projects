from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from IPython.display import display, Markdown
import pandas as pd

# Fetch the data and split it into training and test sets
all_emails = fetch_20newsgroups(categories=['rec.sport.baseball', 'rec.sport.hockey'], subset='all', shuffle=True, random_state=108)
train_emails, test_emails, train_labels, test_labels = train_test_split(all_emails.data, all_emails.target, test_size=0.2, random_state=108)

# Create a pipeline with a CountVectorizer and a MultinomialNB
pipeline = make_pipeline(CountVectorizer(), MultinomialNB())

# Train the pipeline on the training data
pipeline.fit(train_emails, train_labels)

# Test the pipeline on the test data and print the accuracy score
score = pipeline.score(test_emails, test_labels)

# Display accuracy score
display(Markdown(f"## Sports News Classifier Results"))
display(Markdown(f"### Accuracy: {score:.2%}"))

# Use GridSearchCV to tune hyperparameters of the pipeline
parameters = {
    'countvectorizer__max_features': [5000, 10000, None],
    'countvectorizer__ngram_range': [(1, 1), (1, 2)],
    'multinomialnb__alpha': [0.1, 1, 10]
}

grid = GridSearchCV(pipeline, parameters, cv=5)
grid.fit(train_emails, train_labels)

# Print the best hyperparameters and score
df = pd.DataFrame.from_dict(grid.cv_results_)
df = df[['params', 'mean_test_score', 'rank_test_score']]
df = df.sort_values('rank_test_score')

# Display best hyperparameters and score
display(Markdown("<h2 style='color: blue;'>Model Performance</h2>"))
display(Markdown("<h3 style='color: blue;'>Best Hyperparameters</h3>"))
display(df.head(1).style.set_properties(**{'background-color': 'lightgreen', 'color': 'black'}))
display(Markdown(f"<h3 style='color: blue;'>Best Score:</h3>"))
display(Markdown(f"<p style='font-size: 14px;'>{grid.best_score_:.2%}</p>"))

# Provide some context and explanation for the output
display(Markdown("<p>The model's performance is shown above. The best hyperparameters are shown in green, and the corresponding mean test score and rank test score are displayed. The best score achieved by the model is also shown.</p>"))
