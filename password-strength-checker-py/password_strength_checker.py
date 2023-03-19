# Step 1: Import the file to Google Colab
from google.colab import files
uploaded = files.upload()

# Step 2: Read the uncleaned csv file
import pandas as pd
df_original = pd.read_csv(io.BytesIO(uploaded['password_strength_classifier.csv']), on_bad_lines='skip')
print(df_original.head())

# Step 3: Clean the csv file, replace values in the strength column, and save the cleaned file
df_cleaned = df_original.drop_duplicates()
df_cleaned.dropna(inplace=True)
df_cleaned["strength"] = df_cleaned["strength"].replace({0: "weak", 1: "medium", 2: "strong"})
df_cleaned.to_csv("password_strength_classifier_cleaned.csv", index=False)
print(df_cleaned.head())

# Step 4: Load the cleaned csv file into a DataFrame
import pandas as pd
df = pd.read_csv("password_strength_classifier_cleaned.csv")

# Step 5: Prepare data for learning
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(1,3))
X = vectorizer.fit_transform(df['password'])
y = df['strength']

# Step 6: Split data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 7: Train a machine learning model
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 8: Evaluate model performance on the test set
from sklearn.metrics import accuracy_score
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Step 9: Use the trained model to predict password strength
passwords = ["123456", "password", "p@ssw0rd", "myverystrongpassword123!"]
passwords_transformed = vectorizer.transform(passwords)
passwords_pred = model.predict(passwords_transformed)
print("Predictions:", passwords_pred)

'''

Output:

Accuracy: 0.9272892897676364
Predictions: ['weak' 'medium' 'strong' 'strong']

'''
