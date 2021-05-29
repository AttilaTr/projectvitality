from flask import Flask
from flask.templating import render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    day = requests.get('http://projectvitality_api:5000/get_day')
    improvement = requests.post('http://projectvitality_api/get_improvement', data=day.text)
    return render_template('index.html', day=day.text, improvement=improvement.text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)