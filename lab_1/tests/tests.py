import unittest
import requests
from lab_1.lr1.crawl import valid

class TestCrawler(unittest.TestCase):
    def setUp(self):
        self.url = 'https://3dnews.ru/'
        self.invalid_url = 'https://3dnews.ru/assalamusalla'

    def test_valid(self):
        self.assertEqual(valid(self.url).status_code, 200)

    def test_404(self):
        res = valid(self.url)
        self.assertNotEqual(res, 404)
