import json

import requests

f = open('./monitor-network-db.json')
data_json = json.load(f)

one_minute = 1 * 60

db = data_json['db']
total = 0
num = 0
if __name__ == '__main__':


    # for i in range(one_minute):
    #      print(db[i])



    # How to send to a remote destination ##
    responses = requests.post("https://httpbin.org/anything", data={
        'email':"asdf@asd.d",
        'result': 1.4
    })

    print(responses.json())
