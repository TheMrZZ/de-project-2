import json
import time
import unittest

try:
    import server
except ImportError:
    from . import server


class MyTestCase(unittest.TestCase):

    def setUp(self):
        server.app.testing = True
        self.app = server.app.test_client()

    def test_thousand_requests_in_a_minute(self):
        data = json.dumps({
            'text': 'obama'
        })
        headers = {'Content-Type': 'application/json'}

        start = time.time()

        for i in range(1000):
            self.app.post('/similar_tweets', headers=headers, data=data)

        end = time.time()

        total = end - start
        print('Took', total, 'seconds.')

        self.assertLess(total, 60)


if __name__ == '__main__':
    unittest.main()
