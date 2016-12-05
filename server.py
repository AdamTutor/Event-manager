from flask import Flask, request, render_template, redirect
from jinja2 import Template
import db


app = Flask(__name__)
@app.route("/")
def index():
    return render_template("schedule.html", events=db.allEvents())

@app.route("/teams/", methods=["GET", "POST"])
def teams():
    if request.method == "GET":
        return render_template("teams.html", teams=db.allTeams())
    else:
        # do stuff with form data
        db.registerTeam(request.form['team-name'])
        return redirect("/teams/")

@app.route("/teams/new/", methods=["GET"])
def newTeam():
    return render_template("create.html")

@app.route("/events/new/", methods=["GET"])
def newEvent():
    return render_template("event_form.html")




if __name__ == "__main__":
    app.run()
