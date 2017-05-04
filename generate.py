import time

while True:
    with open("db.json", "a") as db:
        db.write("\n")
    time.sleep(7)

