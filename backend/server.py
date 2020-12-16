from flask import Flask, request, jsonify
from flask_cors import CORS
from prometheus_flask_exporter import PrometheusMetrics

try:
    from .search import get_closest_tweet
except ImportError:
    from search import get_closest_tweet

app = Flask(__name__)
CORS(app)
metrics = PrometheusMetrics(app)

total = 1


@app.route('/similar_tweets', methods=['POST'])
@metrics.counter('total_requests', 'Number of total requests', labels={'amount': total})
def classify_sentence():
    text = request.json['text']

    global total
    total += 1
    tweets = get_closest_tweet(text)
    return jsonify(tweets)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
