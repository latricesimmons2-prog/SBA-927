import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag, ne_chunk, sent_tokenize
import string
import re

# Function for tokenize text into sentences
def tokenize_sentences(text):
    sentences = sent_tokenize(text)
    return sentences

# Function to extract named entites from POS-tagged sentences
def part_of_speech_tagging(sentences):
    pos_tagged_sentences = [pos_tag(word_tokenize(sentence)) for sentence in sentences]
    return pos_tagged_sentences

# Define a function for POS tagging
def pos_tagging(text):
    # Tokenize and process the text
    sentences = sent_tokenize(text)
    pos_tags = []
    for sentence in sentences:
        tokens = word_tokenize(sentence)
        tagged_tokens = pos_tag(tokens)
        pos_tags.extend(tagged_tokens)
    return pos_tags

# Function to perform part-of-speech tagging on sentences
def extract_named_entity_recognition(pos_tagged_sentences):
    named_entities = []
    for sentence in pos_tagged_sentences:
        tree = ne_chunk(sentence)
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

    filtered_tokens =[word.lower() for word in tokens if word not in stop_words]

    return filtered_tokens

# read the external file
file_path = 'SBA927.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    # Read the entire content of the file 
    dataset = file.read().splitlines()

# Tokenize and preprocess the entire dataset
processed_dataset = [tokenize_and_preprocess(text) for text in dataset]

# Apply stemming and lemmatization to the entire dataset
stemmed_and_lemmatized_dataset = [stem_and_lemmatize(tokens) for tokens in processed_dataset]

# Apply named entity recognition to the entire dataset
ner_results_dataset = [named_entity_recognition(text) for text in dataset]

# Apply POS tagging to the entire dataset
pos_tagged_dataset = [pos_tagging(text) for text in dataset]

# Display the results
for i, pos_tags in enumerate(pos_tagged_dataset):
    print(f"POS Tags in Text {i+1}: {pos_tags}")
    print()

