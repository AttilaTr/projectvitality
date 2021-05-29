from flask import Flask
import random

app = Flask(__name__)

@app.route('/get_day', methods=['GET'])
def get_day():
    return random.choice(['Monday', 'Tuesday', 'Wednesday'])

@app.route('/get_improvement', methods=['POST'])
def get_improvement():
    improvement = {
        'Monday' : '7',
        'Tuesday' : '6',
        'Wednesday' : '5'
    }
    return improvement[request.data.decode('utf-8')]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)