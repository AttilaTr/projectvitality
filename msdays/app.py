from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/get_day', methods=['GET'])
def get_day():
    return random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

@app.route('/get_improvement', methods=['POST'])
def get_improvement():
    improvement = {
        'Monday' : '3',
        'Tuesday' : '2',
        'Wednesday' : '1',
        'Thursday' : '0',
        'Friday' : '-1',
        'Saturday' : '2',
        'Sunday' : '4'
    }
    return improvement[request.data.decode('utf-8')]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)