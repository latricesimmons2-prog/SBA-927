# SBA-927: Business Text Analytics – Natural Language Processing

## 1. Project Purpose

The purpose of SBA-927 is to demonstrate how Natural Language Processing (NLP) techniques can be used to analyze and process business-related text data. The project uses Python and the Natural Language Toolkit (NLTK) to perform several NLP tasks, including text preprocessing, tokenization, stopword removal, stemming, lemmatization, Part-of-Speech (POS) tagging, Named Entity Recognition (NER), and sentiment analysis.

These techniques demonstrate how unstructured text, such as customer reviews and feedback, can be transformed into useful information that businesses can use to understand customers and make better decisions.

## 2. Dataset

The project uses a collection of customer/product review text as the primary data for the NLP exercises.
The dataset contains written customer feedback that can be processed to identify words, important terms, entities, grammatical patterns, and overall customer sentiment.
The text data provides an example of the type of unstructured information that businesses commonly collect from customers through online reviews and feedback.

## 3. Installation and Running the Project with UV

This project uses UV for Python environment and package management.

### Prerequisites


Make sure Python and UV are installed on your computer.

Clone the repository:

git clone https://github.com/latricesimmons2-prog/SBA-927.git
cd SBA-927

Create and activate the virtual environment:

uv venv

On Windows PowerShell:

.venv\Scripts\activate

Install the project dependencies:

uv sync

If the required packages need to be added manually, NLTK can be installed with:

uv add nltk

Run the individual Python files from the project directory using:

uv run python filename.py

For example:

uv run python SBA-927-p2.py

The project can also be opened in VS Code and executed from the integrated terminal.

## 4. Python Files and Assignment Requirements
The Python files are organized within the src/sba_927 package. Each file is responsible for a specific Natural Language Processing (NLP) technique required for the SBA.

Python File	Assignment Requirement:

* text_data_processing.py -> Text preprocessing and tokenization
* stemming_lemmatization.py -> Stemming and lemmatization
* NER_processing.py	-> Named Entity Recognition (NER)
* POS_tagging.py -> Part-of-Speech (POS) tagging
* sentiment_analysis.py -> Sentiment analysis

File Descriptions: 

* text_data_processing.py – Processes the raw text data and prepares it for NLP analysis through techniques such as tokenization and text cleaning.
* stemming_lemmatization.py – Demonstrates the differences between stemming and lemmatization by reducing words to their root or base forms.
* NER_processing.py – Uses Named Entity Recognition to identify entities within text, such as people, organizations, and locations.
* POS_tagging.py – Uses Part-of-Speech tagging to identify the grammatical role of words within sentences.
* sentiment_analysis.py – Analyzes text to determine whether the sentiment expressed is positive, negative, or neutral.

Each file focuses on a specific NLP technique and demonstrates how that technique can be applied to analyze business and customer-related text.

## Part 5 - Text Preprocessing Examples

Text preprocessing prepares raw text for NLP analysis.
For example, raw customer feedback may contain punctuation, capitalization, and unnecessary words.

Example Input:
The product was AMAZING! I really loved the quality of this product.

After preprocessing, the text can be converted into individual tokens and unnecessary words can be removed.

Example Output:
['product', 'amazing', 'really', 'loved', 'quality', 'product']

Tokenization separates the text into individual words or tokens. Stopword removal removes common words that may not provide much useful information for certain NLP tasks.
Preprocessing makes the text easier for the computer to analyze.

## Part 6 – Stemming vs. Lemmatization

Stemming and lemmatization are both techniques used to reduce words to a simpler form.

### Stemming

Stemming removes word endings to produce a root-like form.

Example:

playing → play
played → play
studies → studi

The result from stemming does not always have to be an actual English word.

### Lemmatization

Lemmatization attempts to return a word to its proper dictionary form.

Example:

running → running/run
better → better

Lemmatization generally produces a more linguistically meaningful result than stemming, although it can require additional information such as the word's grammatical role.

### Difference

Stemming is generally faster but can produce incomplete words.
Lemmatization is more linguistically accurate because it attempts to identify the actual base or dictionary form of a word.

## Part 7 – Named Entity Recognition Results

Named Entity Recognition (NER) identifies important entities within text.

Examples of entities that can be identified include:

* People
* Organizations
* Locations
* Dates
* Companies
* Other proper nouns

For example, a sentence such as:

Apple released a new product in California.

could identify:
* Apple → Organization
* California → Location

NER is useful because businesses can use it to automatically identify important names, companies, locations, and other entities from large amounts of text.

## Part 8 – Part-of-Speech (POS) Tagging Results

Part-of-Speech tagging identifies the grammatical role of words in a sentence.

For example:

The customer loved the product.

The words can be classified as:

* The → Determiner
* customer → Noun
* loved → Verb
* the → Determiner
* product → Noun

POS tagging helps a computer understand how words are being used within a sentence.
This can be useful when analyzing customer feedback because businesses can identify actions, descriptions, products, and other important information within written comments.

## Part 9 – Sentiment Analysis Results

Sentiment analysis determines whether text expresses a positive, negative, or neutral opinion.
The project uses NLTK's sentiment analysis tools to evaluate customer feedback.

### Positive Example

The product was excellent and I loved the quality.

Result: Positive

### Negative Example

The product was terrible and stopped working after one day.

Result: Negative

### Neutral Example

The product arrived on Tuesday.
Result: Neutral

Sentiment analysis allows businesses to process large amounts of customer feedback and quickly identify how customers feel about their products or services.

## Part 10 – Business Applications

The NLP techniques used in this project can be applied to several business situations.

### Tokenization

Tokenization can be used to break customer reviews into individual words so they can be analyzed by other NLP techniques.

### Stopword Removal

Stopword removal can reduce unnecessary words and help focus analysis on more meaningful terms.

### Stemming

Stemming can group similar words together, making it easier to identify common topics or patterns.

### Lemmatization

Lemmatization can improve text analysis by converting words into meaningful base forms.

### POS Tagging

POS tagging can help businesses understand how words are being used and identify important actions, descriptions, and subjects within customer feedback.

### Named Entity Recognition

NER can identify people, companies, locations, products, and other important entities in large collections of text.

### Sentiment Analysis

Sentiment analysis can help businesses determine whether customers have positive, negative, or neutral opinions about their products or services.
Together, these techniques can help businesses analyze customer feedback, identify trends, monitor customer satisfaction, improve products, and make data-driven decisions.

## Part 11 – Final Analysis and Conclusion
SBA-927 demonstrated how Natural Language Processing can transform unstructured business text into useful information. Using Python and NLTK, the project covered multiple NLP techniques including preprocessing, tokenization, stemming, lemmatization, POS tagging, Named Entity Recognition, and sentiment analysis.
The project showed that each technique provides a different type of information about text. When these techniques are combined, businesses can better understand customer feedback, identify important patterns, and evaluate customer sentiment.
Overall, this project provided practical experience using NLP to solve real-world business text analysis problems and demonstrated how automated text analysis can support business decision-making.