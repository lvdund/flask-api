from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello master VD'

@app.route('/info')
def bye():
    retJson = {
        'name': 'Vũ Dũng',
        'age': 22,
        'info': [
            {
                'dog': 'Thuy',
                'kind': 'Samoyed'
            },
            {
                'maid': 'Elie',
                'age': 17,
                'high': 160
            }
        ]
    }
    return jsonify(retJson)

@app.route('/add_number', methods = ["POST"])
def add_number():
    # must be x + y
    dataDict = request.get_json()
    if "y" not in dataDict:
        return "ERROR", 305
    x = dataDict["x"]
    y = dataDict["y"]
    return {
        "x": x,
        "y": y,
        "sum": x+y
    }, 200
    
@app.route('/getApi')
def get_api():
    data_get = request.get_json()
    return jsonify(data_get)

if __name__ == "__main__":
    app.run()