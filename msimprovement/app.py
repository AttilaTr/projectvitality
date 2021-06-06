from flask import Flask, request

app = Flask(__name__)

@app.route('/get_improvement_day', methods=['POST'])
def get_improvement_day():

    improvementday = {
        'Monday' : '3',
        'Tuesday' : '2',
        'Wednesday' : '1',
        'Thursday' : '0',
        'Friday' : '-1',
        'Saturday' : '2',
        'Sunday' : '4'
    }

    return improvementday[request.data.decode('utf-8')]

@app.route('/get_improvement_indoor', methods=['POST'])
def get_improvement_indoor():

    improvementindoor = {
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

    return improvementindoor[request.data.decode('utf-8')]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)