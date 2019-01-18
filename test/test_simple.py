import unittest
import requests
import pytest
from run import app as create_app

class test(unittest.TestCase):

    @pytest.fixture
    def client(self):
        create_app.testing = True
        client = create_app.test_client()
        yield client

    def test_create(client):
        res = requests.get('http://localhost:5000/api/random')
        print(res.json())
        assert "randomNumber" in res.json()


    def test_random(client):
        res = requests.get('http://localhost:5000/api/random')
        print(res.json())
        print(res.json()['randomNumber'])
        assert res.json()['randomNumber'] <= 100
        assert res.json()['randomNumber'] >= 1



if __name__ == '__main__':
    unittest.main()