import flask
from flask import Flask, request
from flask_cors import CORS, cross_origin

from database import Database
from json import dumps

api_v2_cors_config = {
    "origins": ["*"],  # Angular Container IP
    "methods": ["DELETE", "GET", "POST"],
    "allow_headers": ["Authorization", "Content-Type"],
}

app = Flask(__name__)

# Intialize MySQL connection
db = Database(app)

CORS(
    app,
    resources={
        r"/new": api_v2_cors_config,
        r"/edit/*": api_v2_cors_config,
        r"/delete/*": api_v2_cors_config,
    },
)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/new", methods=["POST"])
@cross_origin(**api_v2_cors_config)
def new():
    task = request.json["title"]
    description = request.json["description"]
    id = db.register(task, description)
    return (str(id), 201)


@app.route("/edit/<int:id>", methods=["POST"])
@cross_origin(**api_v2_cors_config)
def edit(id):
    if not db.check(id):
        return "Record not found", 400
    task = request.json["title"]
    description = request.json["description"]
    db.updateTitle(id, task)
    db.updateDescription(id, description)
    return ("", 204)


@app.route("/tasks", methods=["GET"])
@cross_origin(**api_v2_cors_config)
def list():
    list = db.list()
    response = flask.jsonify(list)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return dumps(list)


@app.route("/delete/<int:id>", methods=["DELETE"])
@cross_origin(**api_v2_cors_config)
def delete(id):
    if not db.check(id):
        return "Record not found", 400
    db.delete(id)
    return ("", 204)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500, debug=True)
