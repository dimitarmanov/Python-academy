from datetime import datetime
from time import sleep
import psutil as psutil
import json


def monitor_network(interface):
    current_time = str(datetime.now())
    network = psutil.net_io_counters(pernic=True)
    interface_data = network.get(interface)

    system_resources = {
        "time": str(current_time),
        "interface": interface,
        "sent_bytes": interface_data.bytes_sent,
        "recv_bytes": interface_data.bytes_recv
    }
    return system_resources


def save_db(db):
    with open("monitor-network-db.json", 'w') as f:
        f.write(json.dumps({
            'db': db
        }))


if __name__ == '__main__':
    interface = 'en0'
    db = []
    max_cycles = 60
    while True:
        data = monitor_network(interface)
        db.append(data)
        save_db(db)
        sleep(1)

        max_cycles -= 1
        if max_cycles == 0:
            break



