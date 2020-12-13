from flask import Flask, request, jsonify
from flask_cors import CORS

from classifier import predict

app = Flask(__name__)
CORS(app)


@app.route('/classify_sentence', methods=['POST'])
def classify_sentence():
    text = request.json['sentence']

    return jsonify({
        'sentiment': predict(text)
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
