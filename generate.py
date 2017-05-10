import time
import json
import random
from datetime import  datetime, timedelta

def generate_normal_samples():

    sample_list = []
    with open("db.json", "r") as db:
        olddbbdict = json.load(db)

    phys = olddbbdict["phys"]
    meds = olddbbdict["meds"]
    pains = olddbbdict["pain"]
    sos = olddbbdict["sos"]
    ano = olddbbdict["ano"]

    pain_level = random.randint(0,6)
    initial_date = datetime.today() - timedelta(days=random.randint(5,7)
                                                ,minutes=random.randint(6,19)
                                                ,seconds=random.randint(13,31))
												
    new_pains = []
												
    while initial_date < datetime.now():

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

        if random.randint(1, 20) == 20:
            dict_add["was_sos_med"] = "true"
        else:
            dict_add["was_sos_med"] = "false"

        influences_list = ["Couldn't walk", "Can't do nothing", "Hurt realy bad, but could work", "Could walk"]
        dict_add["influences"] = influences_list[random.randint(0, len(influences_list) - 1)]

        mood_list = ["fine", "anger", "depressed", "tired", "exhausted"]
        dict_add["mood"] = mood_list[random.randint(0, len(mood_list) - 1)]

        # Update the working variables
        initial_date = initial_date + timedelta(minutes=random.randint(6 * 60, 9 * 60)
                                                , seconds=random.randint(13, 31))

        pain_level = pain_level + 1 - random.randint(0, 2)
        new_pains.append(dict_add)


    new_db = {"phys": phys, "meds": meds, "pain": new_pains, "sos": sos, "ano": ano}

    print "Im printing"
    with open("db1.json", "w") as db:
        json.dump(new_db, db)


def create_sos_anomaly():
    with open("db.json", "r") as db:
        olddbbdict = json.load(db)

    phys = olddbbdict["phy"]
    meds = olddbbdict["meds"]
    pains = olddbbdict["pain"]
    sos = olddbbdict["sos"]
    ano = olddbbdict["ano"]

    pain_level = 8
    initial_date = datetime.today() - timedelta(hours=2)

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
        initial_date = initial_date + timedelta(hours=1)

        pain_level = pain_level + 1 - random.randint(0, 2)
        pains.append(dict_add)

    new_db = {"phys": phys, "meds": meds, "pain": pains, "sos": sos, "ano": ano}

    print "Im printing"
    with open("db1.json", "w") as db:
        json.dump(new_db, db)


def create_pain_anomaly():
    with open("db.json", "r") as db:
        olddbbdict = json.load(db)

    phys = olddbbdict["phy"]
    meds = olddbbdict["meds"]
    pains = olddbbdict["pain"]
    sos = olddbbdict["sos"]
    ano = olddbbdict["ano"]

    pain_level = 8
    initial_date = datetime.today() - timedelta(hours=2)

    print ("Creating the Anomaly")
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

        dict_add["was_sos_med"] = False

        influences_list = ["Couldn't walk", "Can't do nothing", "Hurt realy bad, but could work", "Could walk"]
        dict_add["influences"] = influences_list[random.randint(0, len(influences_list) - 1)]

        mood_list = ["fine", "anger", "depressed", "tired", "exhausted", "feeling pain"]
        dict_add["mood"] = mood_list[random.randint(0, len(mood_list) - 1)]

        # Update the working variables
        initial_date = initial_date + timedelta(hours=1)

        pain_level = pain_level + 1 - random.randint(0, 2)
        pains.append(dict_add)

    new_db = {"phys": phys, "meds": meds, "pain": pains, "sos": sos, "ano": ano}

    print "Im printing"
    with open("db1.json", "w") as db:
        json.dump(new_db, db)
