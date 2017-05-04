import time
import json
import random

def generate_normal_samples():

    sample_list = []
    with open("db.json", "r") as db:
        olddbbdict = json.load(db)

    phys = olddbbdict["phy"]
    meds = olddbbdict["meds"]
    pains = olddbbdict["pain"]
    sos = olddbbdict["sos"]
    ano = olddbbdict["ano"]

    for i in xrange(20):
        pass

    new_db = {"phys" : phys, "meds": meds, "pain": pains, "sos": sos, "ano": ano}


    with open("db.json", "w") as db:
        json.dump(new_db, db)