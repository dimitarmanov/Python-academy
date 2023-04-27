import json
from datetime import datetime

if __name__ == '__main__':
    f = open("./data.json")
    data_json = json.load(f)
    print(data_json)
    total_number = 0
    total_float_number = 0
    jokers = 0
    year2000 = 0
    numbers_with_joker = 0

    # Check what the key is
    # for key in data_json:
    #     print(key)

    for obj in data_json["result"]:
        has_joker = False
# Сумата на всички integer числа
        if 'number' in obj:
            total_number += obj['number']
# Сумата на всички float числа
        if 'float' in obj:
            total_float_number += obj['float']
# Колко реда съдържа думата “Joker”
        if 'string' in obj and obj['string'].lower() == "joker":
            jokers += 1
            has_joker = True
# Колко реда има след 2000 година в дата полето
        if 'date' in obj:
            date = datetime.strptime(obj['date'], "%Y-%m-%d").date()
            if date.year >= 2000:
                year2000 += 1
# Сумата на всички integer числа когато boolean е True и string съдържа joker
        if 'boolean' in obj and obj['boolean'] == True and 'number' in obj and has_joker:
            numbers_with_joker += obj["number"]

    print("Number:", total_number)
    print("Float:", total_float_number)
    print("Jokers:", jokers)
    print("Year 2000: ", year2000)
    print("Numbers with joker and True: ", numbers_with_joker)
