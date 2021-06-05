from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/get_day', methods=['GET'])
def get_day():
    return random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)