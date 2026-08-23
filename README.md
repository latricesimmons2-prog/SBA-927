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

## 5. Text Preprocessing Examples

Text preprocessing prepares raw text for NLP analysis.
For example, raw customer feedback may contain punctuation, capitalization, and unnecessary words.

Example Input:
The product was AMAZING! I really loved the quality of this product.

After preprocessing, the text can be converted into individual tokens and unnecessary words can be removed.

Example Output:
['product', 'amazing', 'really', 'loved', 'quality', 'product']

Tokenization separates the text into individual words or tokens. Stopword removal removes common words that may not provide much useful information for certain NLP tasks.
Preprocessing makes the text easier for the computer to analyze.

## 6. Stemming vs. Lemmatization

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

## 7. Named Entity Recognition Results

Named Entity Recognition (NER) was performed using NLTK's named entity chunking functionality. The purpose of NER was to identify important entities within the source dataset and classify them into categories such as people, organizations, and geographic locations.

### Results from the Dataset

The NER process identified the following entities:

| Entity | NLTK Classification |
|---|---|
| Robot | PERSON |
| Detective Del Spooner | PERSON |
| Sonny | PERSON |
| Virtual Interactive Kinetic | ORGANIZATION |
| Detective | PERSON |
| Program | PERSON |
| Susan Calvin | PERSON |
| Sonny | GPE |

Some entries appeared multiple times because they occurred repeatedly in the source dataset.

### Analysis

The NER results successfully identified several important names and concepts from the dataset, including the characters Detective Del Spooner, Sonny, Susan Calvin, and the organization Virtual Interactive Kinetic.

However, the results also demonstrate that automated NER is not always completely accurate. For example, "Sonny" was classified as a GPE (geopolitical entity) in one instance even though it refers to a character rather than a geographic location. "Detective" and "Program" were also classified as PERSON in some results.

This demonstrates an important limitation of NER: the accuracy of entity classification can depend on the context of the text. Businesses using automated NER should review important results when accuracy is critical.

### Business Application

NER can help businesses extract names of people, organizations, locations, products, and other entities from large collections of customer feedback. This can make it easier to identify frequently mentioned companies, products, people, or locations and use that information for further analysis.

## 8. Part-of-Speech (POS) Tagging Results

Part-of-Speech (POS) tagging was performed using NLTK to identify the grammatical role of words within the source dataset. The tags identify categories such as nouns, verbs, adjectives, pronouns, adverbs, and proper nouns.

### Results from the Dataset

The POS tagger successfully identified grammatical categories throughout the dataset.

For example, one sentence from the dataset produced the following results:

> In the futuristic world of I, Robot, robots coexist with humans.

Selected POS results included:

| Word | POS Tag | Meaning |
|---|---|---|
| In | IN | Preposition |
| futuristic | JJ | Adjective |
| world | NN | Noun |
| Robot | NNP | Proper noun |
| robots | NNS | Plural noun |
| coexist | VBP | Verb |
| humans | NNS | Plural noun |

Another example from the dataset was:

> Sonny, an advanced robot with unique characteristics, becomes a key figure in the investigation.

Selected results included:

| Word | POS Tag | Meaning |
|---|---|---|
| Sonny | NNP | Proper noun |
| advanced | JJ | Adjective |
| robot | NN | Noun |
| characteristics | NNS | Plural noun |
| becomes | VBZ | Verb |
| key | JJ | Adjective |
| figure | NN | Noun |
| investigation | NN | Noun |

### Analysis

The POS-tagging results demonstrate that NLTK was able to identify different grammatical roles within the dataset. Proper nouns such as "Sonny" and "Robot" were identified as NNP in several instances, while descriptive words such as "futuristic," "advanced," and "key" were identified as adjectives.

The results also show that automated POS tagging is not always perfect. For example, some words were assigned tags that may not completely match their intended grammatical role based on the context. This demonstrates that POS tagging depends on the surrounding text and the accuracy of the underlying language model.

### Business Application

POS tagging can help businesses analyze customer feedback by identifying important nouns, descriptive adjectives, and action-oriented verbs. For example, nouns can identify products or services being discussed, while adjectives can provide information about how customers describe those products. POS tagging can therefore support more detailed analysis of customer opinions and business-related text.

## 9. Sentiment Analysis Results

Sentiment analysis was performed using NLTK's VADER (Valence Aware Dictionary and sEntiment Reasoner) `SentimentIntensityAnalyzer`. The analysis assigns positive, negative, neutral, and compound scores to text and uses the compound score to determine the overall sentiment.

### Results from the Dataset

Three customer-feedback examples were tested to evaluate the sentiment-analysis process.

### Positive Example

**Input:**

> The customer service was excellent and the staff was very helpful.

**VADER Results:**

- Negative: 0.000
- Neutral: 0.570
- Positive: 0.430
- Compound: 0.7778
- Overall Sentiment: Positive

**Observation:**

The compound score of 0.7778 indicates a strongly positive sentiment. The words "excellent" and "helpful" contributed to the positive classification.

### Negative Example

**Input:**

> I had a terrible experience with the product, it broke after one use.

**VADER Results:**

- Negative: 0.396
- Neutral: 0.604
- Positive: 0.000
- Compound: -0.7096
- Overall Sentiment: Negative

**Observation:**

The compound score of -0.7096 indicates a strongly negative sentiment. The words "terrible" and "broke" contributed to the negative classification.

### Mixed/Neutral Example

**Input:**

> The product is okay, but it could be improved in terms of quality.

**VADER Results:**

- Negative: 0.000
- Neutral: 0.663
- Positive: 0.337
- Compound: 0.6808
- Overall Sentiment: Positive

**Observation:**

Although the statement contains criticism about the product's quality, VADER classified the overall sentiment as positive with a compound score of 0.6808. This demonstrates a limitation of automated sentiment analysis because the model may not fully understand mixed or nuanced customer opinions.

### Overall Analysis

The VADER results demonstrate that sentiment analysis can successfully identify strongly positive and strongly negative customer feedback. However, the mixed example shows that sentiment classification is not always accurate when a customer expresses both positive and negative ideas in the same statement.

Businesses should therefore use sentiment analysis as a tool for identifying general patterns rather than treating every classification as completely accurate. Human review may still be necessary when feedback contains sarcasm, mixed opinions, or complex context.

## 10. Pre-Trained Language Model Evaluation

A pre-trained language model was evaluated using Hugging Face Transformers. The model selected for this experiment was `distilbert/distilbert-base-uncased-finetuned-sst-2-english`, a DistilBERT model fine-tuned for sentiment classification.
The model was loaded using the Hugging Face `pipeline` function and tested with three customer-feedback examples.

### Model

**Model:** distilbert/distilbert-base-uncased-finetuned-sst-2-english

**Task:** Sentiment Analysis

### Test 1: Positive Customer Feedback

**Input:**

> I love this product. The quality is excellent and shipping was fast.

**Output:**

- Predicted Sentiment: POSITIVE
- Confidence Score: 0.9999

The model correctly identified this strongly positive customer review as positive with very high confidence.

### Test 2: Negative Customer Feedback

**Input:**

> The product arrived damaged and customer service was terrible.

**Output:**

- Predicted Sentiment: NEGATIVE
- Confidence Score: 0.9998

The model correctly identified this strongly negative customer review as negative with very high confidence.

### Test 3: Factual Customer Feedback

**Input:**

> The product arrived yesterday and it is the same color shown online.

**Output:**

- Predicted Sentiment: NEGATIVE
- Confidence Score: 0.9941

This result demonstrates a limitation of the model. The statement is primarily factual and does not clearly express positive or negative sentiment. However, the model classified it as negative with high confidence.

### Evaluation

The pre-trained DistilBERT model successfully classified strongly positive and strongly negative customer feedback. However, the third example demonstrates that the model can have difficulty interpreting neutral or factual statements.

The model used in this experiment is designed for binary sentiment classification and provides only POSITIVE or NEGATIVE classifications. It does not provide a NEUTRAL category. Therefore, businesses should not rely solely on the model's confidence score when analyzing ambiguous or factual customer feedback.

The experiment demonstrates that pre-trained language models can provide useful automated sentiment analysis without requiring the model to be trained from scratch. However, the results should be reviewed carefully when customer feedback is neutral, ambiguous, or context-dependent.

## 11. Business Applications

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

## 12. Advantages and Limitations of NLP Techniques

Each NLP technique used in this project provides different benefits, but each also has limitations that should be considered when applying the technique to real-world business data.

### Text Preprocessing and Tokenization

**Advantages:**
- Removes unnecessary characters and formatting from text.
- Converts text into a consistent format for analysis.
- Breaks large amounts of text into manageable tokens.
- Provides a foundation for other NLP techniques.

**Limitations:**
- Removing certain words or characters can sometimes remove useful context.
- Tokenization may not handle every type of language or punctuation perfectly.
- Preprocessing decisions can affect the results of later NLP techniques.

### Stemming

**Advantages:**
- Fast and computationally efficient.
- Helps group related words together.
- Useful when exact dictionary forms are not required.

**Limitations:**
- Can produce words that are not actual English words.
- May remove too much or too little of a word.
- Does not consider the meaning or context of a word.

### Lemmatization

**Advantages:**
- Produces more meaningful dictionary-based word forms.
- Generally provides better linguistic results than stemming.
- Can improve analysis when the meaning of the base word is important.

**Limitations:**
- More computationally intensive than stemming.
- May require grammatical information such as part-of-speech tags.
- Results can still depend on the context of the word.

### Part-of-Speech Tagging

**Advantages:**
- Identifies grammatical roles of words.
- Helps distinguish nouns, verbs, adjectives, and other word types.
- Can provide additional information for more advanced text analysis.

**Limitations:**
- POS tags may be incorrect when the context is ambiguous.
- Informal language, unusual names, and specialized terminology can reduce accuracy.
- The same word can have different grammatical roles depending on context.

### Named Entity Recognition

**Advantages:**
- Automatically identifies important entities in large amounts of text.
- Can identify people, organizations, locations, and other named entities.
- Helps businesses extract structured information from unstructured text.

**Limitations:**
- Entity classification is not always accurate.
- The NER results from this project showed examples such as "Sonny" being classified as GPE even though it referred to a character.
- NER accuracy depends heavily on context and the quality of the underlying model.

### Sentiment Analysis

**Advantages:**
- Can quickly analyze large amounts of customer feedback.
- Helps businesses identify general positive and negative trends.
- Can support customer satisfaction monitoring and product improvement.

**Limitations:**
- May have difficulty with sarcasm, mixed opinions, and complex language.
- The VADER analysis in this project classified a mixed customer statement as positive.
- Sentiment scores do not always represent the complete meaning or context of a customer's opinion.

### Pre-Trained Language Model

**Advantages:**
- Can provide useful NLP predictions without training a model from scratch.
- Requires less development time than building a model from the beginning.
- Can produce highly confident predictions on strongly expressed text.

**Limitations:**
- The DistilBERT model used in this project only provides POSITIVE or NEGATIVE sentiment labels.
- It does not provide a neutral category.
- The experiment showed that a factual statement was classified as NEGATIVE with 99.41% confidence.
- High confidence does not necessarily mean that a prediction is correct.
- Model performance can vary depending on the type and context of the text being analyzed.

## 13. Business Insights from the NLP Analysis

The results of the NLP analysis demonstrate how businesses can use text analytics to extract useful information from unstructured text.

### Customer Sentiment

The VADER sentiment analysis successfully identified strongly positive and strongly negative customer feedback. The positive example received a compound score of 0.7778, while the negative example received a compound score of -0.7096.

These results demonstrate that sentiment analysis can help businesses quickly identify customers who are satisfied or dissatisfied. A company could use this information to monitor customer satisfaction and identify areas that may require attention.

### Mixed Customer Feedback

The statement:

> The product is okay, but it could be improved in terms of quality.

was classified as positive by VADER with a compound score of 0.6808. However, the statement also contains criticism about product quality.

This demonstrates that businesses should not rely entirely on an automated sentiment label. A positive classification can sometimes contain important negative feedback that needs to be reviewed separately.

### Named Entities

The NER analysis identified entities such as Detective Del Spooner, Sonny, Susan Calvin, and Virtual Interactive Kinetic. Although these entities come from the project's source dataset rather than real customer reviews, the results demonstrate how NER can extract important names and organizations from unstructured text.

In a business environment, a similar process could be used to identify frequently mentioned products, companies, people, or locations in customer feedback.

### Text and Language Patterns

The POS-tagging results identified nouns, verbs, adjectives, proper nouns, and other grammatical categories throughout the dataset. This information can help businesses understand how customers describe products and services.

For example, adjectives can provide information about descriptions or opinions, while nouns can identify products, services, or topics being discussed.

### Pre-Trained Model Insights

The DistilBERT experiment demonstrated that a pre-trained language model can classify strongly positive and negative customer feedback with very high confidence. However, the model classified a factual statement as negative with 99.41% confidence.

This result demonstrates an important business consideration: automated models can process large amounts of text quickly, but high-confidence predictions should not automatically be treated as correct. Businesses should consider human review for ambiguous or neutral feedback.

### Overall Business Insight

Combining multiple NLP techniques provides a more complete understanding of text than relying on a single technique. Preprocessing prepares the data, stemming and lemmatization normalize words, POS tagging identifies grammatical patterns, NER extracts important entities, and sentiment analysis identifies emotional patterns.

Together, these techniques can help businesses process large amounts of unstructured text, identify patterns, monitor customer opinions, and support data-driven decision-making. However, the limitations observed in this project demonstrate that automated NLP results should be interpreted carefully and validated when important business decisions depend on the analysis.

## 14. Final Analysis and Conclusion

SBA-927 demonstrated how Natural Language Processing can transform unstructured business text into useful information. Using Python and NLTK, the project covered multiple NLP techniques including preprocessing, tokenization, stemming, lemmatization, POS tagging, Named Entity Recognition, and sentiment analysis.
The project showed that each technique provides a different type of information about text. When these techniques are combined, businesses can better understand customer feedback, identify important patterns, and evaluate customer sentiment.
Overall, this project provided practical experience using NLP to solve real-world business text analysis problems and demonstrated how automated text analysis can support business decision-making.
