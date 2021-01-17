import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from cs50 import SQL

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
DATABASE = os.path.join(PROJECT_ROOT, 'todo.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////" + DATABASE
db = SQLAlchemy(app)

app.config["AUTO_RELOAD_TEMPLATES"] = True


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    todo_time = db.column(db.String(80))
    complete = db.Column(db.Boolean)

@app.route("/")
def index():
    db = SQL("sqlite:///todo.db")
    todo_list = db.execute("""SELECT * FROM todo""")
    return render_template("index.html", todo_list=todo_list)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")

    db = SQL("sqlite:///todo.db")

    db.execute("""
                INSERT INTO todo (title, todo_time, complete)
                VALUES (:title, :todo_time, :complete)""",
                title=title, todo_time=str(request.form.get("time")), complete=False)
    return redirect(url_for("index"))


@app.route("/complete/<string:todo_id>")
def complete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/delete/<string:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))





if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
