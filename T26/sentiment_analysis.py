# Please read all the comments in this example file and all others.

import spacy  # importing spacy
import pandas as pd # importing panda for dataframe

from spacytextblob.spacytextblob import SpacyTextBlob
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

nlp = spacy.load('en_core_web_sm') # specifying the model we want to use. Remember to install this model by typing python -m spacy download en_core_web_md into your command line
nlp.add_pipe('spacytextblob')

# Text Preprocessing
def preprocess_text(text):
    # Create a spaCy document
    doc = nlp(text)
    
    
    # Remove stopwords and punctuation
    filtered_tokens = [token for token in doc if not token.is_stop and not token.is_punct]
    
    # Lemmatize the tokens
    lemmatized_tokens = [token.lemma_ for token in filtered_tokens]
    
    # Join the lemmatized tokens back into a string
    preprocessed_text = ' '.join(lemmatized_tokens)
    
    return preprocessed_text

# Sentiment Analysis
def analyze_sentiment(text):
    # Create a spaCy document
    doc = nlp(text)
    
    # Get the sentiment polarity and subjectivity
    polarity = doc._.blob.polarity
    subjectivity = doc._.blob.subjectivity
    
    # Determine the sentiment label
    if polarity > 0:
        sentiment = 'Positive'
    elif polarity < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    return sentiment, polarity, subjectivity

# Import the dataset, I choose the one with 5000 records only to reduce the time of calculation
df = pd.read_csv('amazon_product_reviews.csv')

print(f'Total Data Size:{df.shape}')

# Clean Data with drop NA values from reviews.text
clean_data = df.dropna(subset='reviews.text')
print(f'Clean Data Size:{clean_data.shape}')

# Select only necessary data
reviews_data = clean_data[['reviews.title','reviews.text']]

# Preprocess the text column
reviews_data['preprocessed_text'] = reviews_data['reviews.text'].apply(preprocess_text)

print(f'Preprocessed Reviews Data Size:{reviews_data.shape}')

# Analyze the sentiment of the preprocessed text
reviews_data['sentiment'], reviews_data['polarity'], reviews_data['subjectivity']= zip(*reviews_data['preprocessed_text'].apply(analyze_sentiment))


# Show text of top 10 most positive reviews along with their polarity, preprocessed text, and sarcasm detection

print('---------------- Show Positive Review ---------------- ')

for index, row in reviews_data.sort_values('polarity', ascending=False).head(10).iterrows():
    print(f'Index:{index}')
    print(f"Positive Review: {row['reviews.text']}")
    print(f"Preprocessed Text: {row['preprocessed_text']}")
    print(f"Sentiment: {row['sentiment']}")
    print(f"Polarity: {row['polarity']}")
    print(f"Subjectivity: {row['subjectivity']}")
    print()


print('---------------- Show Negative Review ---------------- ')

# Show text of top 10 most negative reviews along with their polarity, preprocessed text, and sarcasm detection
for index, row in reviews_data.sort_values('polarity').head(10).iterrows():
    print(f'Index:{index}')
    print(f"Negative Review: {row['reviews.text']}")
    print(f"Preprocessed Text: {row['preprocessed_text']}")
    print(f"Sentiment: {row['sentiment']}")
    print(f"Polarity: {row['polarity']}")
    print(f"Subjectivity: {row['subjectivity']}")
    print()