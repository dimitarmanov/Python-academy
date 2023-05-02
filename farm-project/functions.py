import json

f = open("./farm_data.json")
data_json = json.load(f)
print(data_json)

def get_animal_by_type(type):
    """""Suppose to go through JSON file unpack all farms and all animals"""
    results = []
    for farm in data_json['farms']:
        for animal in farm['animals']:
            if animal['type'] == type:
               results.append(animal)
        return results

if __name__ == '__main__':
    answer = get_animal_by_type('Cow')
    print(answer)
