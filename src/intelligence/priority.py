def priority_score(sentiment_score, frequency):
    return (1 - sentiment_score) * 0.7 + frequency * 0.3
