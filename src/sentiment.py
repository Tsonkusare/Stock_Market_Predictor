from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def get_sentiment_score(headlines):
    total_compound = 0
    count = 0

    for headline in headlines:
        vs = analyzer.polarity_scores(headline)
        total_compound += vs["compound"]
        count += 1

    if count == 0:
        return 0

    avg_compound = total_compound / count  # Range: -1 to +1
    scaled = avg_compound * 5              # Range: -5 to +5
    return round(scaled)
