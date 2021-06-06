  
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests
from os import getenv
from sqlalchemy import desc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
db = SQLAlchemy(app)


class Days(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(50), nullable=False)
    indoor = db.Column(db.String(50), nullable=False)
    improvement = db.Column(db.Integer, nullable=False)
    message = db.Column(db.String(100), nullable=False)


@app.route('/')
def home():
    day = requests.get('http://msdays_api:5000/get_day')
    improvementday = requests.post('http://msimprovement_api:5000/get_improvement_day', data=day.text)
    indoor = requests.get('http://msindoor_api:5000/get_indoor')
    improvementindoor = requests.post('http://msimprovement_api:5000/get_improvement_indoor', data=indoor.text)
    improvement = int(improvementday.text) + int(improvementindoor.text)

    if improvement >= 5:
        message = 'This activity is much recommended to you.'
    elif improvement <= 0:
        message = 'Please avoid this activity on the mentioned day.'
    else:
        message = 'This activity would neither increase, nor decrease your vitality level.'

    days_imp = Days.query.order_by(desc(Days.id)).limit(5).all()

    db.session.add(
        Days(
            day=day.text,
            indoor=indoor.text,
            improvement=improvement,
            message=message
            )
    )
    db.session.commit()

    return render_template('index.html', day=day.text, indoor=indoor.text, improvement=improvement, message=message, days_imp=days_imp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
