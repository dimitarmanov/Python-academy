import json

f = open('./football-data.json')
data_json = json.load(f)

print('----------------')

# how many assists resulted in goals
# What percentage of shots resulted in goals during these matches?

total_goals = 0
total_shots = 0
for team in data_json['teams']:
    for player in team['players']:
        total_goals += player['goals']
        total_shots += player['goals'] + player['assists']
percentage = (total_goals / total_shots) * 100
print(f"All matches: {percentage}%")

print('----------------')


# Did any players score hat-tricks (i.e., three goals in a single match)? If so, which players and which matches?
#TODO
hat_trick_player = ''
home_team = ''
away_team = ''

for team in data_json['teams']:
    for match in data_json['matches']:
        home_team = match['home_team']
        away_team = match['away_team']
        for player in team['players']:
            if player['goals'] > 3:
                hat_trick_player = (player['name'])
                print(f'{hat_trick_player} has scored a hat-trick in match {home_team} vs {away_team}')

print('----------------')

# Which team had the highest number of yellow cards across all of the matches? How many yellow cards did they receive?
yellow_card = 0
team_name = ''
for team in data_json['teams']:
    for player in team['players']:
        yellow_card += (player['yellow_cards'])
        team_name = team['name']
print(f'The team with the highest number of yellow cards is {team_name} with {yellow_card}')

print('----------------')

# Which player had the highest number of assists across all of the matches? How many assists did they have?
assists = 0
name_of_player = ''
for team in data_json['teams']:
    for player in team['players']:
        if player['assists'] > assists:
            assists = player['assists']
            name_of_player = player['name']
print(f'The highest number of assists is {assists} by {name_of_player}')

print('----------------')

# Which match had the most goals scored? How many goals were scored in that match?
home_goals = 0
away_goals = 0
total_num_goals = 0
for match in data_json['matches']:
    home_goals = match['home_goals']
    away_goals = match['away_goals']
    total_num_goals = home_goals + away_goals
   # print(f'most goals {total_num_goals}')


# How many matches ended in a draw?

draw_matches = 0
for match in data_json['matches']:
    if match['winner'] == 'Draw':
        draw_matches += 1
print(f'{draw_matches} ended in a draw')

print('----------------')

# Which player had the highest number of goals across all of the matches? How many goals did they score?

individual_goals = 0
p_name = ''
for team in data_json['teams']:
    for player in team['players']:
        individual_goals = player['goals']
        p_name = player['name']
print(f'{p_name} with {individual_goals}')

print('----------------')

# Which team had the highest number of red cards across all of the matches? How many red cards did they receive?
#TODO

red_card = 0
team_name = ''
for team in data_json['teams']:
    for player in team['players']:
        red_card += player['red_cards']
        team_name = team['name']
print(f'{team_name} has {red_card} red cards')

print('----------------')
