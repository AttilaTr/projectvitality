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
