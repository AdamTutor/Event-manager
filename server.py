from flask import Flask, request, render_template
from jinja2 import Template
import db


app = Flask(__name__)
@app.route("/")
def index():
    return render_template("schedule.html")

@app.route("/teams/")
def teams():
    teams = db.allTeams()
    print(teams)
    return render_template("schedule.html", teams=db.allEvents())

# @app.route("/something")
# def something():
#     return ....

if __name__ == "__main__":
    app.run()
