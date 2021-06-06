from flask import url_for
from flask_testing import TestCase
from app import app
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_get_day(self):
        for _ in range(20):
            response = self.client.get(url_for('get_day'))
            self.assertIn(response.data.decode('utf-8'),['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])