import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string
import re

# Define a function for stemming and lemmatization
def stem_and_lemmatize(tokens):
    # Initialize the stemmer and lemmatizer
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()

    # Apply stemming and lemmatization to each token
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

    return stemmed_tokens, lemmatized_tokens

# Function for Tokenize preprocessing
def tokenize_and_preprocess(text):

    # Remove extra whitespace
    text = text.strip()

    # Remove unwanted special characters
    text = re.sub(r'[^A-Za-z\s]', ' ', text)

    # Convert to lowercase
    text = text.lower()
    
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    punctuation = set(string.punctuation)

    filtered_tokens = [word.lower() for word in tokens if word not in stop_words]

    return filtered_tokens

# read the external text file
file_path = 'SBA927.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    # Read the entire content of the file
    dataset = file.read().splitlines()

# Tokenize and preprocessing for the entire dataset
processed_dataset = [tokenize_and_preprocess(text) for text in dataset]

# Apply stemming and lemmatization to the processed dataset
stemmed_and_lemmatized_dataset = [stem_and_lemmatize(tokens) for tokens in processed_dataset]

# Display the results
for i, (stemmed_tokens, lemmatized_tokens) in enumerate(stemmed_and_lemmatized_dataset):
    print(f"Original Text {i+1}: {dataset[i]}")
    print(f"Stemmed Tokens {i+1}: {stemmed_tokens}")
    print(f"Lemmatized Tokens {i+1}: {lemmatized_tokens}")
    print("/n")