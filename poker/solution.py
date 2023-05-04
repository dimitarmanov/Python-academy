import json


def get_perfect_player():
    player_perfect_score = {}
    for game in data_json:
        for player in game["players"]:
            player_name = player["name"]
            if player_name not in player_perfect_score:
                player_perfect_score[player_name] = 0

            player_perfect_score[player_name] += player["perfect_move_percentage"]

    max_player_perfect = 0
    perfect_player = ""
    for player in player_perfect_score:
        score = player_perfect_score[player]

        if max_player_perfect < score:
            max_player_perfect = score
            perfect_player = player

    print("The most perfect player is", perfect_player, "with score", max_player_perfect)


def get_player_with_most_wins():
    player_max_wins = {}
    for game in data_json:
        for player in game["players"]:
            player_name = player["name"]
            if player_name not in player_max_wins:
                player_max_wins[player_name] = 0

            if player["position"] == 1:
                player_max_wins[player_name] += 1

    max_player_wins = 0
    player_with_most_wins = ""

    for player in player_max_wins:
        score = player_max_wins[player]

        if max_player_wins < score:
            max_player_wins = score
            player_with_most_wins = player

    print("The player with most wins is", player_with_most_wins, max_player_wins, "Wins")


def calculate_win_loss_ratio():
    player_wins = {}
    player_losses = {}

    for game in data_json:
        for player in game["players"]:
            player_name = player["name"]
            if player_name not in player_wins:
                player_wins[player_name] = 0
                player_losses[player_name] = 0

            player_wins[player_name] += player['win_count']
            player_losses[player_name] += player['loss_count']

    players = ["Alice", "Bob", "Charlie", "Dave", "Eve", "Frank", "Grace", "Harry"]
    for player in players:
        wins = player_wins[player]
        loss = player_losses[player]
        ratio = wins / loss
        print("Player", player, "has", round(ratio, 2), "hand win ratio or", round(ratio, 2) * 100, "%")


def find_player_buddies():
    player_play_buddies = {}

    for game in data_json:
        players_in_the_game = []
        for player in game["players"]:
            players_in_the_game.append(player["name"])

        for player in players_in_the_game:
            # Тука махаме играча върхи който работим за да получим само хората с който е играл.
            # Копираме масива за да не го променим с .remove функцията

            players_in_the_game_clone = players_in_the_game.copy()
            players_in_the_game_clone.remove(player)

            for play_buddy in players_in_the_game_clone:
                buddy_players = sorted([player, play_buddy])
                play_buddy_key = buddy_players[0] + "--" + buddy_players[1]

                if play_buddy_key not in player_play_buddies:
                    player_play_buddies[play_buddy_key] = 0

                player_play_buddies[play_buddy_key] += 1


    max_play_buddies = 0
    play_buddies = ""

    for buddies in player_play_buddies:
        play_times = player_play_buddies[buddies]
        if max_play_buddies < play_times:
            max_play_buddies = play_times
            play_buddies = buddies

    print(player_play_buddies)
    print("Max play times together is", max_play_buddies, "for the duo", play_buddies)


if __name__ == '__main__':
    data = open("games.json", "r")
    data_json = json.load(data)

    get_perfect_player()
    get_player_with_most_wins()
    calculate_win_loss_ratio()
    find_player_buddies()