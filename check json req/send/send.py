from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "age": 22,
        "name": "Vu Dung"
    })

if __name__ == "__main__":
    app.run()