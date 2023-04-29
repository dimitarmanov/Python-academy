import json



# Кой животински вид има най-висок разход на храна на ден?

if __name__ == '__main__':
    f = open("./farm_data.json")
    data_json = json.load(f)

    animal_type_feed_costs = {}
    for obj in data_json["farms"]:
        for animal in obj["animals"]:
            animal_type = animal["type"]
            animal_cost_feed = animal["feed_cost"]
            if animal_type not in animal_type_feed_costs:
                animal_type_feed_costs[animal_type] = [animal_cost_feed]
            else:
                animal_type_feed_costs[animal_type].append(animal_cost_feed)

    # Find the highest feed cost for each animal type and print the results
    for animal_type, feed_costs in animal_type_feed_costs.items():
        max_feed_cost = max(feed_costs)
        print(f"The highest feed cost for {animal_type} is {max_feed_cost}.")

    ani_type = ''
    cow_feed_cost = 0
    pig_feed_cost = 0
    chicken_feed_cost = 0
    goat_feed_cost = 0
    animal_type_feed_costs = {}

    for farm in data_json['farms']:
        for animal in farm['animals']:

            if animal['type'] == 'Chicken':
                chicken_feed_cost += animal['feed_cost']

            elif animal['type'] == 'Goat':
                goat_feed_cost += animal['feed_cost']

            elif animal['type'] == 'Pig':
                pig_feed_cost += animal['feed_cost']

            elif animal['type'] == 'Cow':
                cow_feed_cost += animal['feed_cost']

    animals = [{'type': 'Chicken', 'feed_cost': chicken_feed_cost},
               {'type': 'Goat', 'feed_cost': goat_feed_cost},
               {'type': 'Pig', 'feed_cost': pig_feed_cost},
               {'type': 'Cow', 'feed_cost': cow_feed_cost}]
    max_animal = max(animals, key=lambda x: x['feed_cost'])

    print(max_animal)