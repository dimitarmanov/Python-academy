import json

f = open('./games.json')
data_json = json.load(f)


if __name__ == '__main__':

    print('---------')

    # 1. Във всички игри кой играграч има най-много  perfect_move_percentage?

    perfect_move = 0
    player_name = ''
    games_count = 0
    for games in data_json:
        for player in games['players']:
            # if player['perfect_move_percentage'] > perfect_move:
            #     perfect_move += player['perfect_move_percentage']
            #     player_name = player['name']
            if player['perfect_move_percentage'] == 1:
                games_count += 1
                player_name = player['name']
    print(f'The player with the most perfect move percentages is {player_name} happened in {games_count} games')

    print('---------')

    # 2. Във всички игри кой най-много печели/губи

    win_count = 0
    loss_count = 0
    win_player = ''
    loss_player = ''
    for games in data_json:
        for player in games['players']:
            if player['win_count'] > win_count:
                win_count += player['win_count']
                win_player = player['name']

            if player['loss_count'] > loss_count:
                loss_count += player['loss_count']
                loss_player = player['name']

    print(f'Highest win count of {win_count} player is {win_player}')

    print(f'Highest loss count of {loss_count} player is {loss_player}')

    print('---------')

    # 3. Да се калкулира win/loss ratio-то на всички играчи

    Alice_win = 0
    Alice_loss = 0
    Bob_win = 0
    Bob_loss = 0
    Charlie_win = 0
    Charlie_loss = 0
    Dave_win = 0
    Dave_loss = 0
    Eve_win = 0
    Eve_loss = 0
    Frank_win = 0
    Frank_loss = 0
    Grace_win = 0
    Grace_loss = 0
    Harry_win = 0
    Harry_loss = 0

    for games in data_json:
        for player in games['players']:
            if player['name'] == 'Alice':
                Alice_win += player['win_count']
                Alice_loss += player['loss_count']
            if player['name'] == 'Bob':
                Bob_win += player['win_count']
                Bob_loss += player['loss_count']
            if player['name'] == 'Charlie':
                Charlie_win += player['win_count']
                Charlie_loss += player['loss_count']
            if player['name'] == 'Dave':
                Dave_win += player['win_count']
                Dave_loss += player['loss_count']
            if player['name'] == 'Eve':
                Eve_win += player['win_count']
                Eve_loss += player['loss_count']
            if player['name'] == 'Frank':
                Frank_win += player['win_count']
                Frank_loss += player['loss_count']
            if player['name'] == 'Grace':
                Grace_win += player['win_count']
                Grace_loss += player['loss_count']
            if player['name'] == 'Harry':
                Harry_win += player['win_count']
                Harry_loss += player['loss_count']

    print(f'The win ratio of Alice is {Alice_win} and loss ratio is {Alice_loss}')
    print(f'The win ratio of Bob is {Bob_win} and loss ratio is {Bob_loss}')
    print(f'The win ratio of Charlie is {Charlie_win} and loss ratio is {Charlie_loss}')
    print(f'The win ratio of Dave is {Dave_win} and loss ratio is {Dave_loss}')
    print(f'The win ratio of Eve is {Eve_win} and loss ratio is {Eve_loss}')
    print(f'The win ratio of Frank is {Frank_win} and loss ratio is {Frank_loss}')
    print(f'The win ratio of Grace is {Grace_win} and loss ratio is {Grace_loss}')
    print(f'The win ratio of Harry is {Harry_win} and loss ratio is {Harry_loss}')

    print('---------')

    # 4. КОИ ДВАМА ИГРАЧИ СА ИГРАЛИ НАЙ_МНОГО ЗАЕДНО

    for games in data_json:
        for player in games['players']:
            pass
