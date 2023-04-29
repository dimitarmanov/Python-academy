import json

if __name__ == '__main__':
    with open("./ca-library.json") as f:
        data_json = json.load(f)
    print("The name of the library is", data_json["name"])
    str = data_json["address"]["street"]
    print("It's on", str)

    city = data_json["address"]["city"]
    state = data_json["address"]["state"]
    print("It's in the city", city, "in the state of", state)
    print("The phone number is", data_json["phone"])

    print("---------")

    for hours in data_json["hours"]:
        if hours["day"] == "Wednesday":
            print("The library is open from",hours["open"])
            print("The library closes at", hours["close"])

    print("---------")
    for book in data_json["books"]:
        print("The title of the book is", book["title"])
        print("The author is", book["author"])
        print("The book was pubhsed in", book["year"])
        print("--------")


## Todo  Print the title, author, and publication year of each book in the library's collection.
