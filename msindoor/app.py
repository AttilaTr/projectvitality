from flask import Flask, request
import random

app = Flask(__name__)

choices=['sleeping 8 hours', 'taking quick nap after lunch', 'eating healthy food', 'eating unhealthy food', 'playing games / watching TV during the night', 'having great sex', 'having dissapointing sex', 'working on computer not taking breaks', 'doing yoga', 'dancing', 'doing some aerobic', 'doing some exercise', 'not doing any pyhisical activity', 'cooking proper food']

@app.route('/get_indoor', methods=['GET'])
def get_indoor():
    return random.choice(choices)
    
@app.route('/get_improvement', methods=['POST'])
def get_improvement():
    improvement = {
        'sleeping 8 hours' : '5',
        'taking quick nap after lunch' : '1',
        'eating healthy food' : '3',
        'eating unhealthy food' : '-2',
        'cooking proper food' : '4',
        'playing games / watching TV during the night' : '-5',
        'having great sex' : '6',
        'having dissapointing sex' : '-3',
        'working on computer not taking breaks' : '-2',
        'doing yoga' : '5',
        'doing some aerobic': '5',
        'dancing' : '4',
        'doing some exercise' : '3',
        'not doing any pyhisical activity' : '-4'
    }
    return improvement[request.data.decode('utf-8')]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)