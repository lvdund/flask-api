from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def checkPost(postedData, funcName):
    if funcName in ["add", "sub"]:
        if "x" not in postedData or "y" not in postedData:
            return 301
        return 200
    
class Add(Resource):
    def post(self):
        postedData = request.get_json()
        status_code = checkPost(postedData, "add")
        if status_code == 301:
            return jsonify({
                "message": "ERROR",
                'status code': status_code
            })
        x = int(postedData["x"])
        y = int(postedData["y"])
        result = {
            'message': x + y,
            'status code': status_code
        }
        return jsonify(result)

class Sub(Resource):
    def post(self):
        postedData = request.get_json()
        status_code = checkPost(postedData, "sub")
        if status_code == 301:
            return jsonify({
                "message": "ERROR",
                'status code': status_code
            })
        x = int(postedData["x"])
        y = int(postedData["y"])
        result = {
            'message': x - y,
            'status code': status_code
        }
        return jsonify(result)

@app.route("/")
def index():
    return "hello master"

api.add_resource(Add, "/add")
api.add_resource(Sub, "/sub")

if __name__ == "__main__":
    app.run(host="0.0.0.0")