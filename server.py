

import json

from dateutil import parser
from flask import Flask, request
from flask_cors import CORS, cross_origin
from juggernaut import Juggernaut
from datetime import datetime, timedelta
import random


app = Flask(__name__)
CORS(app)

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
    @classmethod
    def add(cls, message, severity):
        cls._list.append({"id": cls.running_id, "isRead": "false",
        "message": message, "severity": severity})

        cls.running_id += 1

    running_id += 1
    @classmethod
    def mark_read(cls, id):
        for notif in cls._list:
            if str(notif["id"]) == str(id):
                notif["isRead"] = "true"

    @classmethod
    def get_length(cls):
        return len(cls._list)

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

@app.route('/<username>/pain_anomalies')
def pain_anomalies(username):
    anomalies = []
    index = 0
    with open('db.json','r') as dbfile:
        dbdict = json.load(dbfile)

    pain_events = [obj for obj in dbdict["pain"] if obj["username"].lower() == username.lower()]
    pain_events.sort(key=lambda x: x["date"])

    while index < len(pain_events) - 2:
        anomaly = {}
        #if a three point decrease is found, check the size of the ouchy.
        if pain_events[index]["level"] < pain_events[index+1]["level"] and pain_events[index + 1]["level"] < pain_events[index + 2]["level"]:
            anomaly["startWorseningTime"] = pain_events[index]["date"]
            end_index = index+2
            while end_index < len(pain_events) - 1:
                if pain_events[end_index]["level"] < pain_events[end_index+1]["level"]:
                    end_index+=1
                else:
                    break
            anomaly["endWorseningTime"] = pain_events[end_index]["date"]
            if Notifications.get_length() < 3:
                Notifications.add(
                    "An pain anomaly was reported with mikel, he has increasing pain in a few days.. details: %s" % (
                    username),
                    "high")
            anomalies.append(anomaly)

            index = end_index
        index+=1
    return json.dumps({"data": anomalies})

def there_is_a_pain_anomaly(username):
    anomalies = []
    index = 0
    with open('db.json', 'r') as dbfile:
        dbdict = json.load(dbfile)

    pain_events = [obj for obj in dbdict["pain"] if obj["username"].lower() == username.lower()]
    pain_events.sort(key=lambda x: x["date"])

    while index < len(pain_events) - 2:
        anomaly = {}
        # if a three point decrease is found, check the size of the ouchy.
        if pain_events[index]["level"] < pain_events[index + 1]["level"] and pain_events[index + 1]["level"] < \
                pain_events[index + 2]["level"]:
            anomaly["startWorseningTime"] = pain_events[index]["date"]
            end_index = index + 2
            while end_index < len(pain_events) - 1:
                if pain_events[end_index]["level"] < pain_events[end_index + 1]["level"]:
                    end_index += 1
                else:
                    break
            anomaly["endWorseningTime"] = pain_events[end_index]["date"]
            anomalies.append(anomaly)
            #Notifications.add("An pain anomaly was reported with %s, he has increasing pain in a few days.." % username,
             #                 "high")
            index = end_index
        index += 1

    return anomalies != []

def is_sos_three_days_in_a_row(curr_index, sos_events):

    current_sos = parser.parse(sos_events[curr_index]["time_taken"])
    next_sos = parser.parse(sos_events[curr_index+1]["time_taken"])
    next_next_sos = parser.parse(sos_events[curr_index+2]["time_taken"])
    sum = 0
    if current_sos.year == next_sos.year and current_sos.year == next_next_sos.year:
        if current_sos.month== next_sos.month and current_sos.month== next_next_sos.month:

            sum += next_sos.day - current_sos.day
            sum += next_next_sos.day - next_sos.day
            return sum <= 2
    return False

def is_sos_tommorow(curr_index, sos_events):
    current_sos = parser.parse(sos_events[curr_index]["time_taken"])
    next_sos = parser.parse(sos_events[curr_index + 1]["time_taken"])
    if current_sos.year == next_sos.year:
        if current_sos.month== next_sos.month:
            return next_sos.day - current_sos.day <= 1
    return False

def create_sos_anomaly(username):
    sample_list = []
    with open("db.json", "r") as db:
        olddbbdict = json.load(db)

    phys = olddbbdict["phy"]
    meds = olddbbdict["meds"]
    pains = olddbbdict["pain"]
    sos = olddbbdict["sos"]
    ano = olddbbdict["ano"]

    pain_level = 8
    initial_date = datetime.today() - timedelta(minutes=random.randint(3*60, 3*61)
                                                , seconds=random.randint(13, 31))

    for i in xrange(3):

        dict_add = {}
        dict_add["username"] = "mikel"

        body_parts = ["hand", "shoulder", "leg", "feet", "head", "back", "belly", "neck"]
        hurt_body_parts = []
        for i in xrange(random.randint(1, 3)):
            hurt_body_parts.append(body_parts[random.randint(0, len(body_parts) - 1)])
        dict_add["body_parts"] = list(set(hurt_body_parts))

        dict_add["date"] = str(initial_date)

        dict_add["level"] = pain_level

        dict_add["duration"] = random.randint(1, 5)

        context_list = ["Sports", "Temperature Change", "Anger", "Bad Mood", "Nothing"]
        dict_add["context"] = context_list[random.randint(0, len(context_list) - 1)]

        type_list = ["burn", "sharp", "bombing"]
        dict_add["type"] = type_list[random.randint(0, len(type_list) - 1)]

        dict_add["was_sos_med"] = True

        influences_list = ["Couldn't walk", "Can't do nothing", "Hurt realy bad, but could work", "Could walk"]
        dict_add["influences"] = influences_list[random.randint(0, len(influences_list) - 1)]

        mood_list = ["fine", "anger", "depressed", "tired", "exhausted"]
        dict_add["mood"] = mood_list[random.randint(0, len(mood_list) - 1)]

        # Update the working variables
        initial_date = datetime.today() + timedelta(minutes=60
                                                    , seconds=random.randint(1, 7))

        pain_level = pain_level + 1 - random.randint(0, 2)
        pains.append(dict_add)

    new_db = {"phys": phys, "meds": meds, "pain": pains, "sos": sos, "ano": ano}

    print "Im printing"
    with open("db1.json", "w") as db:
        json.dump(new_db, db)

@app.route('/<username>/sos_anomalies')
def sos_anomalies(username):
    anomalies = []
    index = 0
    with open('db.json','r') as dbfile:
        dbdict = json.load(dbfile)

    sos_events = [obj for obj in dbdict["sos"] if obj["username"].lower() == username.lower()]
    sos_events.sort(key=lambda x: x["time_taken"])

    while index < len(sos_events) - 2:
        anomaly = {}
        # if a three point decrease is found, check the size of the ouchy.
        if is_sos_three_days_in_a_row(index, sos_events):
            anomaly["startWorseningTime"] = sos_events[index]["time_taken"]
            end_index = index + 2
            while end_index < len(sos_events) - 1:
                if is_sos_tommorow(end_index, sos_events):
                    end_index += 1
                else:
                    break
            anomaly["endWorseningTime"] = sos_events[end_index]["time_taken"]
            anomalies.append(anomaly)
            if Notifications.get_length() < 3:
                Notifications.add(
                    "An sos anomaly was reported with mikel, he is taking too many sos pills in a few days.. details %s" % (
                    username),
                    "high")

            index = end_index
        index += 1
    return json.dumps({"data": anomalies})

@app.route('/<username>/sos')
def sos(username):
    with open('db.json', 'r') as dbfile:
        dbdict = json.load(dbfile)

    sos_events = [obj for obj in dbdict["sos"] if obj["username"].lower() == username.lower()]
    sos_events.sort(key=lambda x: x["time_taken"])
    return json.dumps({"data":sos_events})

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

@app.route("/readnotif/<id>")
def read_notif(id):
    Notifications.mark_read(id)
    return json.dumps({})  # need to return something ...

Notifications
@app.route("/<username>/report/pain", methods=['POST'])
def handle_report(username):

    assert request.method == 'POST'
    save_report_to_the_db(request.form["report"])
    if there_is_a_pain_anomaly(username):
        pass
        #Notifications.add("An anomaly was reported with %s, you might want to check him out." % username,
         #"high")
    elif pain_anomalies(username) != []:
        #Notifications.add("An anomaly was reported with %s, you might want to check him out." % username,
         #                 "high")
        pass
    else:
        Notifications.add("%s filled in a pain report" % username,  "medium")
    return json.dumps({})  # need to return something ...


def save_report_to_the_db(report):
    print "Saving Report to the DB......"  # change this