import datetime
import json


if __name__ == '__main__':

    # Using with to open and close the file automatically
    with open("./chat-gpt.json") as f:
        data_json = json.load(f)

    print("The title of the book is:", data_json['title'])
    print("The author is:", data_json['author'])
    published = (data_json['year']) # Define Variable for year it was published
    today = datetime.date.today()
    curr_year = today.year
    print("The book was published", curr_year - published, "years ago") # Number of years since the book was published
    print("The book has", data_json["pages"], "pages")
    print("The book was published by", data_json["publisher"])



