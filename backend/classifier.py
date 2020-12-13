from typing import Literal

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

classifier = SentimentIntensityAnalyzer()

Sentiment = Literal['positive', 'neutral', 'negative']


def get_sentiment_from_compound(compound_score: float) -> Sentiment:
    """ Return the sentiment from a compound score. """
    if compound_score >= 0.05:
        return 'positive'
    if compound_score <= -0.05:
        return 'negative'

    return 'neutral'


def predict(text: str) -> Sentiment:
    """ Predict the sentiment of a given text. """
    predictions = classifier.polarity_scores(text)
    return get_sentiment_from_compound(predictions['compound'])


def benchmark_model(verbose=True):
    """ Test the Vader model on the Tweets dataset. Returns the accuracy. """

    total = 0
    correct = 0

    with open('tweets_GroundTruth.txt') as f:
        for line in f.readlines():
            _, score, text = line.strip().split('\t')

            score = float(score)
            sentiment = get_sentiment_from_compound(score)
            predicted_sentiment = predict(text)

            total += 1
            if sentiment == predicted_sentiment:
                correct += 1
    
    accuracy = correct / total
    if verbose:
        print(f'Accuracy score: {accuracy:.2%}')

    return accuracy


def main():
    # Run the demo
    benchmark_model()


if __name__ == '__main__':
    main()
