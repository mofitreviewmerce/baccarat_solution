from json import dumps
from httplib2 import Http


def make_message(bot_name, relative_bet_size, side_for_shoe, streak_side, streak_number, seq, minimum_bet_size):
    num = minimum_bet_size * relative_bet_size
    num_1b = num // 10
    num_100m = num % 10
    side = 'T' if side_for_shoe == '' or relative_bet_size == 0 else side_for_shoe
    win_lose = 'W' if streak_side == side_for_shoe else 'L'
    last_10_seq = list(reversed(seq))[:10]
    last_10_str = ''
    for i in last_10_seq:
        last_10_str += i
    message = bot_name + ":\t" + side + str(num_1b*10 + num_100m) + win_lose + str(streak_number) + "\t" + last_10_str
    print(num_1b, num_100m)

    return message


def send(message):
    url = 'https://chat.googleapis.com/v1/spaces/AAAAQbaUcRM/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=J-dduBYQW60VqyODSQjn1R0SgzsQszvqMblCielOjRs%3D'
    bot_message = {
        'text': message}

    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )
