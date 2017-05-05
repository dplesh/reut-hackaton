

import json
from flask import Flask, request
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




class Notifications(object):
    _list = []



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
    with open('db.json','r') as dbfile:
        dbdict = json.load(dbfile)

    # import ipdb; ipdb.set_trace()
    users = list(set([obj["username"] for obj in dbdict["pain"]]))
    return json.dumps({"data": users})


@app.route('/notifications')
def notifications():
    notif = Notifications._list[:] # if u want other notif mecha change this
    Notifications._list = []
    return json.dumps(notif)

@app.route("/<username>/report/pain", methods=['POST'])
def handle_report(username):

    #  wget --post-data "report={???}" http://localhost:5000/????/report/pain


    assert request.method == 'POST'
    save_report_to_the_db(request.form["report"])
    if there_is_anomaly():
        Notifications._list.append(username) # change this
    return json.dumps({})  # need to return something ...


def save_report_to_the_db(report):
    print "Saving Report to the DB......"  # change this

def there_is_anomaly():
    return True # change this