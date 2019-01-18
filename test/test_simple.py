import unittest
import run
import requests

class test(unittest.TestCase):
    def test_random(self):
        r = requests.get('http://localhost:5000/api/random')
        



if __name__ == '__main__':
    unittest.main()