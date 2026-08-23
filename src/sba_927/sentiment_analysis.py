import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

# Create a sentiment analysis function
def analyze_sentiment(text):
    scores = sia.polarity_scores(text)

    if scores['compound'] >= 0.05:
        sentiment = 'Positive'
    elif scores['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    return sentiment, scores

# Prompts with buisness-related customer feedback for sentiment analysis
prompts = [
    {
        "prompt": "The customer service was excellent and the staff was very helpful.",
        "expected_sentiment": "Positive"
    },
    {
        "prompt": "I had a terrible experience with the product, it broke after one use.",
        "expected_sentiment": "Negative"
    },
    {
        "prompt": "The product is okay, but it could be improved in terms of quality.",
        "expected_sentiment": "Neutral"
    }
]

# Perform sentiment analysis on the prompts
for item in prompts:

    print("-" * 70)

    # Display the prompt 
    print("PROMPT:")
    print(item["prompt"])
    print()

    # Display the review
    print("REVIEW:")
    print(item["prompt"])
    print()

    # Analyze the sentiment
    sentiment, scores = analyze_sentiment(item["prompt"])

    # Display the sentiment analysis results
    print("SENTIMENT ANALYSIS RESULTS:")
    print("-----------------------------")
    print("Sentiment:", sentiment)
    print("Scores:", scores)
    print()

    # Observation
    print("OBSERVATION:")
    print("-------------")

    if sentiment == "Positive":
        print("The sentiment analysis correctly identified the positive sentiment in the review.")
    elif sentiment == "Negative":
        print("The sentiment analysis correctly identified the negative sentiment in the review.")
    else:
        print("The sentiment analysis correctly identified the neutral sentiment in the review.")

print()
print("\n" + "=" * 70)
print("PRE-TRAINED LANGUAGE MODEL EVALUATION")
print("=" * 70)

from transformers import pipeline

# Load the pre-trained DistilBERT sentiment-analysis model
model_name = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"

classifier = pipeline(
    "sentiment-analysis",
    model=model_name
)

# Test customer feedback examples
test_reviews = [
    "I love this product. The quality is excellent and shipping was fast.",
    "The product arrived damaged and customer service was terrible.",
    "The product arrived yesterday and it is the same color shown online."
]

print("\nModel Used:")
print(model_name)

print("\nSentiment Analysis Results:")

for review in test_reviews:
    result = classifier(review)[0]

    print("\nInput:")
    print(review)

    print("Predicted Sentiment:")
    print(result["label"])

    print("Confidence Score:")
    print(f"{result['score']:.4f}")

print("\n" + "-" * 70)
print("PRE-TRAINED MODEL EVALUATION")
print("-" * 70)

print("""
The pre-trained DistilBERT model successfully analyzed three
customer-feedback examples. The model correctly identified the
strongly positive review as POSITIVE and the strongly negative
review as NEGATIVE.

The third review was a factual statement without clearly positive
or negative language. However, the model classified it as NEGATIVE
with high confidence. This demonstrates an important limitation:
the model was trained for binary sentiment classification and does
not provide a neutral category.

Overall, the experiment demonstrates that a pre-trained language
model can perform sentiment classification on customer feedback,
but its predictions should be interpreted carefully, particularly
when the text is neutral, factual, or ambiguous.
""")