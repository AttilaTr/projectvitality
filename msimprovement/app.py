from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/get_improvement', methods=['POST'])
def get_improvement():
    improvementday = {
        'Monday' : 3,
        'Tuesday' : 2,
        'Wednesday' : 1,
        'Thursday' : 0,
        'Friday' : -1,
        'Saturday' : 2,
        'Sunday' : 4
    }
    improvementindoor = {
        'sleeping 8 hours' : 5,
        'taking quick nap after lunch' : 1,
        'eating healthy food' : 3,
        'eating unhealthy food' : -2,
        'cooking proper food' : 4,
        'playing games / watching TV during the night' : -5,
        'having great sex' : 6,
        'having dissapointing sex' : -3,
        'working on computer not taking breaks' : -2,
        'doing yoga' : 5,
        'doing some aerobic': 5,
        'dancing' : 4,
        'doing some exercise' : 3,
        'not doing any pyhisical activity' : -4
    }
    day=request.json['day']
    indoor=request.json['indoor']
    improvement = day + indoor
    return jsonify(improvement)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

