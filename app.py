from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/hello")
def hello():
    return jsonify({"message": "Hello from Jenkins deployed API!"})

@app.route("/bye")
def bye():
    return jsonify({"message": "Goodbye from updated API!"})

@app.route("/ping")
def ping():
    return jsonify({"message": "Pong from Jenkins CI/CD!"})


@app.route("/ok")
def ok():
    return jsonify({"message": "Auto deploy is REALLY working!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
