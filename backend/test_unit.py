import unittest

try:
    from .search import get_closest_tweet
except ImportError:
    from search import get_closest_tweet


class TestClassifier(unittest.TestCase):
    def test_tweet_obama(self):
        self.assertRegexpMatches(
            get_closest_tweet('obama')[0]['text'],
            'President Obama missed the deadline!'
        )

    def test_tweet_florida(self):
        self.assertRegexpMatches(
            get_closest_tweet('florida')[0]['text'],
            'Great poll- Florida! Thank you!'
        )

    def test_tweet_fraud(self):
        self.assertRegexpMatches(
            get_closest_tweet('fraud')[0]['text'],
            'Snowden is a liar.and a fraud!'
        )

    def test_tweet_muslims(self):
        self.assertRegexpMatches(
            get_closest_tweet('muslims')[0]['text'],
            'In Britain, more Muslims join ISIS than join the British army.'
        )


if __name__ == '__main__':
    unittest.main()
