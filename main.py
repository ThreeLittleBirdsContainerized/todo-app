from flask import Flask, render_template, request, redirect, url_for
import database as db
from json import dumps

db.init()
app = Flask(__name__)


@app.route("/")
def index():
    list = db.list()
    return render_template("index.html", todo=list, id=1, title=2, description=3)


@app.route("/new", methods=["POST"])
def new():
    task = request.form["task"]
    description = request.form["description"]
    id = db.register(task, description)
    return (str(id), 201)

    # return render_template("form.html", title="New Task", headline="list.append(new)", button=".addTask()")


@app.route("/edit/<int:id>", methods=["POST"])
def edit(id):
    if not db.check(id):
        return "Record not found", 400
    task = request.form["task"]
    description = request.form["description"]
    db.updateTitle(id, task)
    db.updateDescription(id, description)
    return ("", 204)


@app.route("/tasks", methods=["GET"])
def list():
    list = db.list()
    return dumps(list)


@app.route("/<int:id>", methods=["DELETE"])
def delete(id):
    if not db.check(id):
        return "Record not found", 400
    db.delete(id)
    return ("", 204)


@app.route("/test")
def test():
    return render_template("test.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(port=5500, debug=True)
