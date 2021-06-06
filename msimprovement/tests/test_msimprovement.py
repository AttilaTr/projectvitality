from flask import url_for
from flask_testing import TestCase
import requests_mock
from app import app, db



def test_get_improvement(self):
            test_cases = [('Monday','3'),('Tuesday','2'),('Wednesday','1'),('Thursday','0'),('Friday','-1'),('Saturday','2'),('Sunday','4')]
            for case in test_cases:
                response = self.client.post(url_for('get_improvement'), data=case[0])
                self.assertEqual(response.data.decode('utf-8'), case[1])

def test_get_improvement(self):
            test_cases = [('sleeping 8 hours','5'),('taking quick nap after lunch','1'),('eating healthy food','3'),('eating unhealthy food','-2'),('having dissapointing sex','-3')]
            for case in test_cases:
                response = self.client.post(url_for('get_improvement'), data=case[0])
                self.assertEqual(response.data.decode('utf-8'), case[1])