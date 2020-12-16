from flask import Flask, request, jsonify
from flask_cors import CORS

try:
    from .search import get_closest_tweet
except ImportError:
    from search import get_closest_tweet

app = Flask(__name__)
CORS(app)


@app.route('/similar_tweets', methods=['POST'])
def classify_sentence():
    text = request.json['text']

    tweets = get_closest_tweet(text)
    return jsonify(tweets)
#

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'result': 'hello'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
