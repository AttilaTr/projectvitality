from flask import url_for
from flask_testing import TestCase
import requests_mock
from app import app, db

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///test.db',
            DEBUG=True
        )
        return app

    def setUp(self):
        db.create_all()
    def tearDown(self):
        db.drop_all()

class TestHome(TestBase):
    def test_home(self):
        with requests_mock.Mocker() as mocker:
            mocker.get('http://msdays_api:5000/get_day', text='Thursday')
            mocker.post('http://msimprovement_api:5000/get_improvement_day', text='0')
            mocker.get('http://msindoor_api:5000/get_indoor', text='sleeping 8 hours')
            mocker.post('http://msimprovement_api:5000/get_improvement_indoor', text='5')
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'On Thursday by sleeping 8 hours you would gain 5 vitality points', response.data)