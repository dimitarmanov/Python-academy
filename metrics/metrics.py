import json
from datetime import datetime
from time import sleep

import psutil as psutil

db = []


def monitor_data():
    current_time = datetime.now()
    cpu = psutil.cpu_percent(4)
    ram = psutil.virtual_memory()[2]
    system_resources = {
        "time": str(current_time),
        "cpu": cpu,
        "ram": ram,
    }
    return system_resources


def save_db(db):
    with open("monitor-db.json", 'w') as f:
        f.write(json.dumps({
            'db': db
        }))


if __name__ == '__main__':
    max_cycles = 60
    while True:
        data = monitor_data()
        db.append(data)
        save_db(db)
        sleep(1)

        max_cycles -= 1
        if max_cycles == 0:
            break
