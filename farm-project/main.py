import json
# First open the json file
if __name__ == '__main__':
    f = open("./farm_data.json")
    data_json = json.load(f)


    # 1. Коя ферма има най-висока дневна млечна добивна способност?

    startNum = 0
    name = ''

    for obj in data_json["farms"]:
        for animal in obj["animals"]:
            if 'daily_milk_yield' in animal:
                if startNum < animal['daily_milk_yield']:
                    startNum = animal['daily_milk_yield']
                    name = obj['name']
    print("The farm with the highest milk yield is", name, "with daily milk yield of", startNum)
    print("--------------------")

    # 2. Кой животински вид има най-висока средна тегло по всички ферми?
    #TODO this needs to be fixed

    animal_types = set()
    for farm in data_json["farms"]:
        for animal in farm["animals"]:
            animal_types.add(animal["type"])


    animal_counts = {}
    animal_weights = {}
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

    cowsAverageWeight = animal_weights["Cow"] / animal_counts["Cow"]
    chickenAverageWeight = animal_weights["Chicken"] / animal_counts["Chicken"]
    pigAverageWeight = animal_weights["Pig"] / animal_counts["Pig"]
    goatAverageWeight = animal_weights["Goat"] / animal_counts["Goat"]

    print("The cows average weight is ",cowsAverageWeight)
    print("The chickens average weight is ",chickenAverageWeight)
    print("The pigs average weight is ",pigAverageWeight)
    print("The goats average weight is ",goatAverageWeight)

    print("--------------------")

# 3. Коя култура има най-висока дневна добивна способност на всички ферми?
    wheat_yield = 0
    barley_yield = 0
    soy_yield = 0
    corn_yield = 0

    for farm in data_json['farms']:
        for crop in farm['crops']:
            if crop['type'] == 'Wheat':
                wheat_yield += crop['daily_yield']
            elif crop['type'] == 'Corn':
                corn_yield += crop['daily_yield']
            elif crop['type'] == 'Soybeans':
                soy_yield += crop['daily_yield']
            elif crop['type'] == 'Barley':
                barley_yield += crop['daily_yield']

    crops = [{'type': 'Corn', 'daily_yield': corn_yield},
             {'type': 'Soybeans', 'daily_yield': soy_yield},
             {'type': 'Wheat', 'daily_yield': wheat_yield},
             {'type': 'Barely', 'daily_yield': barley_yield}]
    max_crops = max(crops, key=lambda x: x['daily_yield'])

    print(f"The crop with the highest daily yield is {max_crops['type']} with {max_crops['daily_yield']}")

    print("--------------------")


    ## 4. Кой животински вид има най-висок разход на храна на ден?]
    #TODO This needs to be fixed
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
        print(f"The animal with the highest feed cost for {animal_type} is {max_feed_cost}.")

    print("--------------------")

    # 5.Каква е общата дневна яйчна добивна способност на всички кокошки (value-то е Chickens) по всички ферми?

    total_eggs = 0

    for farm in data_json['farms']:
        for animal in farm['animals']:
            if animal['type'] == 'Chicken':
                total_eggs += animal['daily_egg_yield']

    print(f'The total daily eggs yield from all farms is {total_eggs}')

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

# 8. Каква е общата дневна добивна способност на всички култури в региона “Southwest”?

sw_region = 'Southwest'
total_crop_yield = 0
for farm in data_json['farms']:
    if farm['region'] == sw_region:
        for crop in farm['crops']:
            total_crop_yield += crop['daily_yield']

print(f"The total yield from all crops in {sw_region} is {total_crop_yield}")

print("--------------------")

# 9. Кой животински вид има най-висок разход на храна на ден за всички ферми в региона “West”?

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

print(
    f"The animal with the highest feed cost in the {w_region} region is {max_animal['type']} with a feed cost of {max_animal['feed_cost']}")

print("--------------------")

# 10. Каква е общата дневна яйчна добивна способност на всички ферми в региона “Plains”?

pl_region = 'Plains'
pl_total_egg_yield = 0

for farm in data_json['farms']:
    if farm['region'] == pl_region:
        for animal in farm['animals']:
            if animal['type'] == 'Chicken':
                pl_total_egg_yield += animal['daily_egg_yield']

print(f"The total egg yield in {pl_region} region is {pl_total_egg_yield}")


