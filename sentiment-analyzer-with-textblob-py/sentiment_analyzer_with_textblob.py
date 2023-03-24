!pip install textblob
!pip install textblob-fr

from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer

# Set the language of the input text
while True:
    language = input("Enter the language of the input text (fr/en): ")
    if language.lower() in ["fr", "en"]:
        break
    print("Invalid language entered. Please enter either 'fr' for French or 'en' for English.")

# Initialize the sentiment analyzer
if language.lower() == "fr":
    analyzer = PatternAnalyzer()
else:
    analyzer = None

# Get input text from the user
text = input("Enter some text to analyze (separate phrases/paragraphs by newline or '.'): ")

# Analyze the sentiment of each phrase or paragraph
phrases = text.split('\n')
for i, phrase in enumerate(phrases):
    if phrase.strip() == "":
        continue
    if language.lower() == "fr":
        blob = TextBlob(phrase, pos_tagger=PatternTagger(), analyzer=analyzer)
    else:
        blob = TextBlob(phrase, analyzer=analyzer)
    sentiment = blob.sentiment

    # Customize sentiment analysis thresholds (optional)
    polarity_threshold = 0.1
    subjectivity_threshold = 0.5
    if sentiment[0] > polarity_threshold:
        polarity_label = "Positive"
        polarity_explanation = "The opinion expressed in the text is generally positive."
    elif sentiment[0] < -polarity_threshold:
        polarity_label = "Negative"
        polarity_explanation = "The opinion expressed in the text is generally negative."
    else:
        polarity_label = "Neutral"
        polarity_explanation = "The text expresses a neutral opinion."

    if sentiment[1] > subjectivity_threshold:
        subjectivity_label = "Subjective"
        subjectivity_explanation = "The opinion expressed in the text is based on personal feelings or opinions."
    else:
        subjectivity_label = "Objective"
        subjectivity_explanation = "The opinion expressed in the text is based on objective facts or observations."

    # Print the sentiment scores and explanations for each phrase or paragraph
    print(f"\nSENTIMENT ANALYSIS RESULTS FOR PHRASE/PARAGRAPH {i+1}:")
    print(f"Input text: {phrase}\n")
    print("\033[1mPolarity (positive/negative opinion):\033[0m")
    print("\033[1mA value of 0 means neutral, a value > 0 means positive, and a value < 0 means negative.\033[0m")
    print(f"Value: {sentiment[0]:.2f} ({polarity_label})")
    print(polarity_explanation + "\n")
    print("\033[1mSubjectivity (personal/objective opinion):\033[0m")
    print("\033[1mA value of 0 means objective, and a value of 1 means very subjective.\033[0m")
    print(f"Value: {sentiment[1]:.2f} ({subjectivity_label})")
    print(subjectivity_explanation)
