import random

from config import GAME_CHOICES, RULES, SCOREBOARD, MATCH_ELEMENT
from decorators import log_time


def get_user_choice():
    user_input = input("Enter your choice (r,p,s): ")
    if user_input not in GAME_CHOICES:
        print("Invalid input....")
        return get_user_choice()
    return user_input


def get_system_choice():
    return random.choice(GAME_CHOICES)


def update_scoreboard(result):
    if result['user'] == 3:
        SCOREBOARD['user'] += 1
    else:
        SCOREBOARD['system'] += 1

    print('#' * 20)
    print('##', f'user: {SCOREBOARD["user"]}'.ljust(16), '##')
    print('##', f'system: {SCOREBOARD["system"]}'.ljust(16), '##')
    print('#' * 20)


def find_winner(user, system):
    match = {user, system}
    if len(match) == 1:
        return None
    return RULES[tuple(sorted(match))]


def play_one_hand():
    result = {'user': 0, 'system': 0}

    while result['user'] < 3 and result['system'] < 3:
        user_choice = get_user_choice()
        system_choice = get_system_choice()
        winner = find_winner(user_choice, system_choice)

        if winner == user_choice:
            result['user'] += 1
            msg = "You Win!! ✅"
        elif winner == system_choice:
            result['system'] += 1
            msg = "You Lose!! ❌"
        else:
            msg = "You Draw!! 🫱🏻‍🫲🏼"

        print(
            f'you: {MATCH_ELEMENT[user_choice]} \n'
            f'system: {MATCH_ELEMENT[system_choice]} \n'
            f'result: {msg} '
            f'{result}')

    update_scoreboard(result)
    play_again = input("Would you like to play again? (y/n): ")
    if play_again == 'y':
        play_one_hand()


@log_time
def play():
    play_one_hand()


if __name__ == '__main__':
    play()
