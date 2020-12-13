try:
    from .vectorizer import load_model, process, data
except ImportError:
    from vectorizer import load_model, process, data

model = load_model()


def get_closest_tweet(user_text):
    tokens = process(user_text)
    vector = model.infer_vector(tokens)

    result = []
    for tweet_id, confidence in model.docvecs.most_similar([vector])[:3]:
        tweet = data.iloc[tweet_id].to_dict()
        result.append({**tweet, 'confidence': confidence})

    return result


if __name__ == '__main__':
    print(get_closest_tweet('very embarrassed'))