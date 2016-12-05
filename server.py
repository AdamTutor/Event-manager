from flask import Flask, request, render_template
from jinja2 import Template
import db


app = Flask(__name__)
@app.route("/")
def index():
    return render_template("schedule.html", events=db.allEvents())

@app.route("/create/")
def create():
    return render_template("create.html")

@app.route("/teams/")
def teams():
    return render_template("teams.html", )


if __name__ == "__main__":
    app.run()
