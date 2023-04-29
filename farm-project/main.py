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
## 3. Каква е средната тегло на прасетата на фермите в региона “South”?
    region = "South"
    pig_count = {}
    pig_weight = {}
    for farm in data_json["farms"]:
        if farm["region"] == region:
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
        print(f"Average weight of {pig}s in {region} region: {avg_weight}")
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




