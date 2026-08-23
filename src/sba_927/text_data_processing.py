import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import re

# Download required NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Function for Tokenize preprocessing
def tokenize_and_preprocess(text):

    # Remove extra whitespace
    text = text.strip()

    # Remove unwanted special characters
    text = re.sub(r'[^A-Za-z\s]', ' ', text)

    # Convert to lowercase
    text = text.lower()
    
    # Tokenize the text
    tokens= word_tokenize(text)
    
    # Remove stopwords and punctiuation
    stop_words = set(stopwords.words('english'))
    punctuation = set(string.punctuation)

    filtered_tokens = [word.lower() for word in tokens if (word.isalpha()and word.lower() not in stop_words and word not in punctuation)]
    
    return filtered_tokens

# read the external text file
file_path = 'SBA927.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    # Read the entire content of the file
    dataset = file.read().splitlines()

# Tokenize and preprocessing for the entire dataset
processed_dataset = [tokenize_and_preprocess(text) for text in dataset]

# Display the results
for i, tokens in enumerate(processed_dataset):
    print(f"Original Text {i+1}: {dataset[i]}")
    print(f"Processed Tokens {i+1}: {tokens}")
    print("/n")