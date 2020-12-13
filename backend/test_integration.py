import json
import unittest

import server


class MyTestCase(unittest.TestCase):

    def setUp(self):
        server.app.testing = True
        self.app = server.app.test_client()

    def predict(self, text: str):
        return self.app.post('/classify_sentence', headers={'Content-Type': 'application/json'}, data=json.dumps({
            'sentence': text
        })).json['sentiment']

    def test_server_classification_format(self):
        response = self.app.post('/classify_sentence', headers={'Content-Type': 'application/json'}, data=json.dumps({
            'sentence': 'I love you'
        })).json

        self.assertEqual(response, {
            'sentiment': 'positive'
        })

    def test_positive_server_classification(self):
        self.assertEqual(self.predict('I love you'), 'positive')
        self.assertEqual(self.predict('Thanks for the meal!'), 'positive')

    def test_neutral_server_classification(self):
        self.assertEqual(self.predict('I will buy two oranges.'), 'neutral')
        self.assertEqual(self.predict('How is the weather today?'), 'neutral')

    def test_negative_server_classification(self):
        self.assertEqual(self.predict('I hate you'), 'negative')
        self.assertEqual(self.predict('The meal was terrible!'), 'negative')


if __name__ == '__main__':
    unittest.main()
