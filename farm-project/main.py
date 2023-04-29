import json
# First open the json file
if __name__ == '__main__':
    f = open("./farm_data.json")
    data_json = json.load(f)
    startNum = 0
    name = ''

    # Loop through farms to get highest daily_milk_yield
    for obj in data_json["farms"]:
        for animal in obj["animals"]:
            if 'daily_milk_yield' in animal:
                if startNum < animal['daily_milk_yield']:
                    startNum = animal['daily_milk_yield']
                    name = obj['name']
    print("The farm with the highest milk yield is", name, "with daily milk yield of", startNum)
    print("--------------------")
    # Get all animal types
    animal_types = set()
    for farm in data_json["farms"]:
        for animal in farm["animals"]:
            animal_types.add(animal["type"])

    animal_counts = {}
    animal_weights = {}
    # Save animal counts and entire animal type weight
    for farm in data_json["farms"]:
        for animal in farm["animals"]:
            animal_type = animal["type"]
            weight = animal["average_weight"]

            # !!! I don't understand this !!! #
            if animal_type in animal_counts:
                animal_counts[animal_type] += 1
                animal_weights[animal_type] += weight
            else:
                animal_counts[animal_type] = 1
                animal_weights[animal_type] = weight

    # Calculate average animal weight, based on entire animal weight / animal type count
    cowsAverageWeight = animal_weights["Cow"] / animal_counts["Cow"]
    chickenAverageWeight = animal_weights["Chicken"] / animal_counts["Chicken"]
    pigAverageWeight = animal_weights["Pig"] / animal_counts["Pig"]
    goatAverageWeight = animal_weights["Goat"] / animal_counts["Goat"]

    print("The cows average weight is ",cowsAverageWeight)
    print("The chickens average weight is ",chickenAverageWeight)
    print("The pigs average weight is ",pigAverageWeight)
    print("The goats average weight is ",goatAverageWeight)

## Коя култура има най-висока дневна добивна способност на всички ферми?
    # crop_types = set()
    # for farm in data_json["farms"]:
    #     for crop in farm["crops"]:
    #         crop_types.add(crop["type"])
    #         daily_yield = crop["daily_yield"]  # Extract daily yield for the current crop
    #         # do something with daily_yield here
    # print(daily_yield, crop_types)
    print("--------------------")
 ## 4. Which animal type has highest feed_cost ##
    animal_type_feed_costs = {}

    # Iterate through the animals in the dataset and update the feed cost for each animal type in the dictionary
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

    print("--------------------")



## 6. Каква е средната тегло на прасетата на фермите в региона “South”?
    s_region = "South"
    pig_count = {}
    pig_weight = {}
    for farm in data_json["farms"]:
        if farm["region"] == s_region:
            for animal in farm["animals"]:
                if animal["type"] == "Pig":
                    pig = animal["type"]
                    pweight = animal["average_weight"]
                    if pig in pig_count:
                        pig_count[pig] += 1
                        pig_weight[pig] += pweight
                    else:
                        pig_count[pig] = 1
                        pig_weight[pig] = pweight
    for pig in pig_count:
        avg_weight = pig_weight[pig] / pig_count[pig]
        print(f"Average weight of {pig}s in {s_region} region: {avg_weight}")
    print("--------------------")


## 7. Каква е дневната добивна способност на Soybeans в региона “Rocky Mountains”?

    rm_region = 'Rocky Mountains'
    soy = 'Soybeans'
    total_soy = 0
    for farm in data_json['farms']:
        for crop in farm['crops']:
            if farm['region'] == rm_region and crop["type"] == soy:
                total_soy += crop['daily_yield']

    print(f"The total yield of soybeans in {rm_region} is {total_soy}")

print("--------------------")

# Каква е общата дневна добивна способност на всички култури в региона “Southwest”?

sw_region = 'Southwest'
total_crop_yield = 0
for farm in data_json['farms']:
    if farm['region'] == sw_region:
            for crop in farm['crops']:
                total_crop_yield += crop['daily_yield']

print(f"The total yield from all crops in {sw_region} is {total_crop_yield}")

print("--------------------")

# Каква е общата дневна яйчна добивна способност на всички кокошки (value-то е Chickens) по всички ферми?

total_eggs = 0

for farm in data_json['farms']:
    for animal in farm['animals']:
        if animal['type'] == 'Chicken':
            total_eggs += animal['daily_egg_yield']

print(f'The total daily eggs yield from all farms is {total_eggs}')

print("--------------------")

# Кой животински вид има най-висок разход на храна на ден за всички ферми в региона “West”?

w_region = 'West'
ani_type = ''
cow_feed_cost = 0
pig_feed_cost = 0
chicken_feed_cost = 0
goat_feed_cost = 0

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

print(f"The animal with the highest feed cost in the {w_region} region is {max_animal['type']} with a feed cost of {max_animal['feed_cost']}")

print("--------------------")


