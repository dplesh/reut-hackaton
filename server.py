

import json
from flask import Flask
from flask_cors import CORS, cross_origin
from juggernaut import Juggernaut



app = Flask(__name__)
CORS(app)
jug = Juggernaut()

# Priority 2: POST Request from client to get new Pain Report
pass

# Priority 2: POST Request form client to get new Activities Report
pass

# Priority 1: GET Request from Doctor Web to get Pain Reports by User
pass

# Priority 1: GET Request from Doc Web to get any anomalies
pass

# Priority 1.5: GET Request from Doc Web to get activities report
pass

# Priority 0: On Different key presses generate different pain reports for a user on the """DB""".
pass  # Implemented on generate.py

@app.route('/<username>/meds')
def meds(username):
    with open('db.json','r') as dbfile:
        dbdict = json.load(dbfile)

    # import ipdb; ipdb.set_trace()
    matching = [obj for obj in dbdict["meds"] if obj["username"].lower() == username.lower()]
    return json.dumps({"data": matching})

@app.route('/<username>/phy')
def phy(username):
    with open('db.json','r') as dbfile:
        dbdict = json.load(dbfile)

    # import ipdb; ipdb.set_trace()
    matching = [obj for obj in dbdict["phy"] if obj["username"].lower() == username.lower()]
    return json.dumps({"data": matching})



@app.route('/<username>/anomalies')
def anomalies(username):
    with open('db.json','r') as dbfile:
        dbdict = json.load(dbfile)

    return "meow"


@app.route('/<username>/sos')
def sos(username):
    return "meow"

@app.route('/<username>/pain')
def pain(username):
    with open('db.json','r') as dbfile:
        dbdict = json.load(dbfile)

    # import ipdb; ipdb.set_trace()
    matching = [obj for obj in dbdict["pain"] if obj["username"].lower() == username.lower()]
    return json.dumps({"data": matching})


@app.route('/users')
def users():
    return {"data": ["Mikel"]}


@app.route("/<username>/report/pain", methods=['POST']):
def handle_report(username):
    assert request.method == 'POST'
    save_report_to_the_db()
    jug.publish(username, "published pain")


def save_report_to_the_db(report):
    print "Saving Report to the DB......"