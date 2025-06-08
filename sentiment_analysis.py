from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(texts):
    analyzer = SentimentIntensityAnalyzer()
    sentiments = [analyzer.polarity_scores(t)["compound"] for t in texts]
    return sentiments