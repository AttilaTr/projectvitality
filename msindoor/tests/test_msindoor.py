from flask import url_for
from flask_testing import TestCase
from app import app, choices
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_get_indoor(self):
        for _ in range(20):
            response = self.client.get(url_for('get_indoor'))
            self.assertIn(response.data.decode('utf-8'), choices)

    def test_get_improvement(self):
            test_cases = [('sleeping 8 hours','5'),('taking quick nap after lunch','1'),('eating healthy food','3'),('eating unhealthy food','-2'),('having dissapointing sex','-3')]
            for case in test_cases:
                response = self.client.post(url_for('get_improvement'), data=case[0])
                self.assertEqual(response.data.decode('utf-8'), case[1])