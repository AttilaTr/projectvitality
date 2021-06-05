from flask import Flask, request
import random

app = Flask(__name__)

choices=['sleeping 8 hours', 'taking quick nap after lunch', 'eating healthy food', 'eating unhealthy food', 'playing games / watching TV during the night', 'having great sex', 'having dissapointing sex', 'working on computer not taking breaks', 'doing yoga', 'dancing', 'doing some aerobic', 'doing some exercise', 'not doing any pyhisical activity', 'cooking proper food']

@app.route('/get_indoor', methods=['GET'])
def get_indoor():
    return random.choice(choices)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)