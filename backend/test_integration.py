import json
import unittest

try:
    import server
except ImportError:
    from . import server


class MyTestCase(unittest.TestCase):

    def setUp(self):
        server.app.testing = True
        self.app = server.app.test_client()

    def get_similar_tweets(self, text: str):
        return self.app.post('/similar_tweets', headers={'Content-Type': 'application/json'}, data=json.dumps({
            'text': text
        })).json

    def test_amount_tweets(self):
        self.assertEqual(len(self.get_similar_tweets('test')), 20)
        self.assertEqual(len(self.get_similar_tweets('this is a very long sentence for the test')), 20)

    def test_tweet_format(self):
        tweet = self.get_similar_tweets('test')[0]
        self.assertEqual(type(tweet['text']), str)
        self.assertEqual(type(tweet['link']), str)
        self.assertEqual(type(tweet['id']), int)
        self.assertEqual(type(tweet['author']), str)


if __name__ == '__main__':
    unittest.main()
