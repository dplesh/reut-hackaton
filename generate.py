import time
import json
import random
from datetime import  datetime, timedelta

def generate_normal_samples():

    sample_list = []
    with open("db.json", "r") as db:
        olddbbdict = json.load(db)

    phys = olddbbdict["phy"]
    meds = olddbbdict["meds"]
    pains = olddbbdict["pain"]
    sos = olddbbdict["sos"]
    ano = olddbbdict["ano"]

    initial_date = datetime.today() - timedelta(days=random.randint(30,35)
                                                ,minutes=random.randint(6,19)
                                                ,seconds=random.randint(13,31))
    while initial_date<datetime.now():

        initial_date = initial_date + timedelta(minutes=random.randint(6*60,9*60)
                                                ,seconds=random.randint(13,31))

    new_db = {"phys" : phys, "meds": meds, "pain": pains, "sos": sos, "ano": ano}


    with open("db.json", "w") as db:
        json.dump(new_db, db)