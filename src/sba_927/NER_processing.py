import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string
import re

# Function for tokenize text into sentences
def tokenize_sentences(text):
    sentences = nltk.sent_tokenize(text)
    return sentences

# Function to extract named entites from POS-tagged sentences
def part_of_speech_tagging(sentences):
    pos_tagged_sentences = [nltk.pos_tag(word_tokenize(sentence)) for sentence in sentences]
    return pos_tagged_sentences

# Function to perform part-of-speech tagging on sentences
def extract_named_entity_recognition(pos_tagged_sentences):
    named_entities = []
    for sentence in pos_tagged_sentences:
        tree = nltk.ne_chunk(sentence)
        for subtree in tree:
            if hasattr(subtree, 'label'): # Check if subtree is a named entity
                entity = ' '.join([token for token, pos in subtree.leaves()])
                named_entities.append((entity, subtree.label()))
    return named_entities

# Define a function for named Entity recognition
def named_entity_recognition(text):
   
   # Tokenize and process the text
   sentences = tokenize_sentences(text)
   pos_tagged_sentences = part_of_speech_tagging(sentences)
   named_entities = extract_named_entity_recognition(pos_tagged_sentences)
   return named_entities

# Define a function for stemming and lemmatization
def stem_and_lemmatize(tokens):

    # Initialize the stemmer and lemmatizer
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()

    # Apply stemming and lemmatization to each token
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

    return stemmed_tokens, lemmatized_tokens

# Function for tokenize and Preprocessing
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

# Apply stemming and lemmatization to the entire dataset
stemmed_and_lemmatized_dataset = [stem_and_lemmatize(tokens) for tokens in processed_dataset]

# Apply named entity recognition to the entire dataset
ner_results = [named_entity_recognition(text) for text in dataset]

# Display the results
for i, results in enumerate(ner_results):
    print(f"Named Entities {i+1}: {results}")
    print()