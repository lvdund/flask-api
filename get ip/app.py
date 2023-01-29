from flask import request, Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "hello"

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200

@app.route('/some-url')
def get_data():
    return requests.get('http://localhost:5000/getApi').content

if __name__ == "__main__":
    app.run()