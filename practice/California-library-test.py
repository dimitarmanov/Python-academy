import json

if __name__ == '__main__':
    with open("./ca-library.json") as f:
        data_json = json.load(f)
    #print(data_json)
    print("The name of the library is", data_json["name"])
    str = data_json["address"]["street"]
    print("It's on", str)
    city = data_json["address"]["city"]
    state = data_json["address"]["state"]
    print("It's in the city", city, "in the state of", state)
    print("The phone number is", data_json["phone"])
    for hours in data_json["hours"]:
        if hours["day"] == "Wednesday":
            print("The library is open from",hours["open"])
            print("The library closes at", hours["close"])

## Todo  Print the title, author, and publication year of each book in the library's collection.
