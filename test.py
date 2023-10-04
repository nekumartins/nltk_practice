import pandas as pd
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

# Read the data
df = pd.read_csv('WhatsApp Chat with Favour.txt', sep='\n', header=None, names=['text'])

# Remove metadata and keep only the message
df['text'] = df['text'].str.replace('\[.*\]', '')


# Remove empty messages
df = df[df['text'].str.strip().astype(bool)]

# Initialize the sentiment analyze
sia = SentimentIntensityAnalyzer()


# Apply sentiment analysis to each message
df['sentiment_scores'] = df['text'].apply(lambda text: sia.polarity_scores(text))

