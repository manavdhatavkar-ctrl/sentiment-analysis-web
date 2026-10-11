
from textblob import TextBlob


def analyze_sentiment(text):
    """
    Analyze text and return its sentiment,
    polarity, and subjectivity.
    """

    if not isinstance(text, str) or not text.strip():
        raise ValueError("Text cannot be empty.")

    blob = TextBlob(text)

    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {
        "sentiment": sentiment,
        "polarity": round(polarity, 3),
        "subjectivity": round(subjectivity, 3),
    }
