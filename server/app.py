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

@app.route('/')
def home():
    day = requests.get('http://msdays_api:5000/get_day')
    improvementday = requests.post('http://msdays_api:5000/get_improvement', data=day.text)
    indoor = requests.get('http://msindoor_api:5000/get_indoor')
    improvementindoor = requests.post('http://msindoor_api:5000/get_improvement', data=indoor.text)
    improvement = int(improvementday.text) + int(improvementindoor.text)
    
    days_imp = Days.query.order_by(desc(Days.id)).limit(5).all()
    
    db.session.add(
        Days(
            day = day.text,
            indoor = indoor.text,
            improvement = improvement
        )
    )
    db.session.commit()

    return render_template('index.html', day=day.text, indoor=indoor.text, improvement=improvement, days_imp=days_imp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)