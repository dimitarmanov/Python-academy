data_json = {
    "farms": [
        {
            "name": "Farm1",
            "region": "asdasdasd",
            "animal": [
                {
                    "type": "chicken",
                    "daily_egg_yield": 10,
                    "average_weight": 15,
                    "feed_cost": 50,
                }, {
                    "type": "cow",
                    "daily_milk_yield": 25,
                    "average_weight": 500,
                    "feed_cost": 600,
                }, {
                    "type": "bull",
                    "daily_pork_yield": 200,
                    "average_weight": 3000,
                    "feed_cost": 600,
                }
            ]
        }, {
            "name": "Farm2",
            "region": "asdasdasd",
            "animal": [
                {
                    "type": "chicken",
                    "daily_egg_yield": 10,
                    "average_weight": 1,
                    "feed_cost": 10,
                }, {
                    "type": "cow",
                    "daily_milk_yield": 20,
                    "average_weight": 100,
                    "feed_cost": 200,
                }, {
                    "type": "bull",
                    "daily_pork_yield": 100,
                    "average_weight": 1000,
                    "feed_cost": 500,
                }
            ]
        }, {
            "name": "Farm3",
            "region": "asdasdasd",
            "animal": [
                {
                    "type": "chicken",
                    "daily_egg_yield": 120,
                    "average_weight": 15,
                    "feed_cost": 210,
                }, {
                    "type": "cow",
                    "daily_milk_yield": 520,
                    "average_weight": 1020,
                    "feed_cost": 2300,
                }, {
                    "type": "bull",
                    "daily_pork_yield": 1500,
                    "average_weight": 10020,
                    "feed_cost": 5400,
                }
            ]
        },
    ]
}

# total_egg = 0
# total_milk = 0
# total_egg_milk = 0
# total_meat = 0
#
# biggest_milk = 0
# current_farm_name = ""

# ferms = data_json["farms"]
# for ferm in ferms:
#     ferm_milk = 0
#     for animal in ferm["animal"]:
#         animal_type = animal["type"]
#         if "cow" in animal_type:
#             milk = animal['daily_milk_yield']
#             total_milk += milk
#             ferm_milk += milk
#             total_egg_milk += milk
#         elif "chicken" in animal_type:
#             egg = animal['daily_egg_yield']
#             total_egg += egg
#             total_egg_milk += egg
#         elif "bull" in animal_type:
#             meat = animal['daily_pork_yield']
#             total_meat += meat
#
#     if biggest_milk < ferm_milk:
#         biggest_milk = ferm_milk
#         current_farm_name = ferm["name"]
#
# print("BIGGEST MILK", biggest_milk, "from", current_farm_name)
# print("Total milk", total_milk)
# print("Total egg", total_egg)
# print("TOtal egg + milk", total_egg_milk)
# print("TOtal meat", total_meat)

obj = {
}

ferms = data_json["farms"]
for ferm in ferms:
    for animal in ferm["animal"]:
        animal_type = animal["type"]
        weight = animal["average_weight"]
        if not animal_type in obj:
            obj[animal_type] = 0

        obj[animal_type] += weight

max_weight = 0
max_weight_animal = ""

for key in obj:
    weight = obj[key]
    animal_type = key

    if max_weight < weight:
        max_weight = weight
        max_weight_animal = animal_type

print(max_weight, max_weight_animal)
