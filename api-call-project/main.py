## Ignore

import json
import os
import requests

def get_steam_apps():
    if os.path.isfile("steam_app_list.json"):
        f = open("./steam_app_list.json")
        file_text = f.read()
        if file_text != "":
            data_json = json.loads(file_text) # From string to JSON
            return data_json

    r = requests.get("https://api.steampowered.com/ISteamApps/GetAppList/v2/")
    if r.status_code == 200:
        result = r.json()
        with open("./steam_app_list.json", "w") as f:
            f.write(json.dumps(result)) # From JSON to string
        return result

def get_steam_app_by_appid():
    if not apps:
        return

    counter = 0
    for app in apps['applist']['apps']:
        get_steam_app_by_appid(app['appid'])

        print(app)
        counter += 1

    if counter >= 5:
        break


if __name__ == '__main__':
 steam_apps = get_steam_apps()
 if
 counter = 0
 for app in steam_apps:
     print(app)
     counter +=1


