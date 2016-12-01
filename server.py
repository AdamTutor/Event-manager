from flask import Flask, request, render_template
import db


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/something")
# def something():
#     return ....

@app.route("/api/events/")
def events_list():
    if request.method == "DELETE":
        db.deleteEvents()
        return ("", 204)
    elif request.method == "GET":
        events = db.allEvents()
        return event_to_json(events)
if __name__ == "__main__":
    app.run()
