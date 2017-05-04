

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
    running_id = 0
    def add(self, message, severity):
        _list.append({"id": running_id, "isRead": "false", 
        "message": message, "severity": severity})

    running_id += 1

    def mark_read(self, id):
        for notif in self._list:
            if notif["id"] == id:
                notif["isRead"] = "true";

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
    return json.dumps(Notifications._list)

@app.route("/readnotif", methods=['POST'])
def read_notif():

    #  wget --post-data "id=1" http://localhost:5000/????/report/pain


    assert request.method == 'POST'
    id = request.form["id"]
    Notifications.mark_read(id)
    return json.dumps({})  # need to return something ...


@app.route("/<username>/report/pain", methods=['POST'])
def handle_report(username):

    #  wget --post-data "report={???}" http://localhost:5000/????/report/pain


    assert request.method == 'POST'
    save_report_to_the_db(request.form["report"])
    if there_is_anomaly():
        Notifications.add("An anomaly was reported with %s, you might want to check him out." % username, 
         "high")
    else:
        Notifications.add("%s filled in a pain report" % username,  "medium")
    return json.dumps({})  # need to return something ...


def save_report_to_the_db(report):
    print "Saving Report to the DB......"  # change this

def there_is_anomaly():
    return True # change this