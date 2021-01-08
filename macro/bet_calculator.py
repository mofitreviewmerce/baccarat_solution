import math


def side_for_shoe(seq):
    if len(seq) == 0:
        return ''
    else:
        if seq[0] == 'T':
            return side_for_shoe(seq[1:])
        elif seq[0] == 'B' or seq[0] == 'P':
            return seq[0]
        else:
            return ''


def calculate_streak(seq, streak, side):
    if len(seq) == 0:
        return streak, side
    else:
        if streak == 0:
            if seq[-1] == 'T':
                streak = 0
                side = ''
            else:
                streak = 1
                side = seq[-1]
            return calculate_streak(seq[:-1], streak, side)
        else:
            if seq[-1] == 'T':
                return calculate_streak(seq[:-1], streak, side)
            if seq[-1] == side:
                return calculate_streak(seq[:-1], streak+1, side)
            elif seq[-1] != side:
                return streak, side


def calculate_action(seq):
    side_for_game = side_for_shoe(seq)
    streak, side = calculate_streak(seq, 0, '')
    relative_bet_size = 0

    if side_for_game == '':
        relative_bet_size = 0
    else:
        if side == side_for_game:
            relative_bet_size = 2 ** (math.ceil(streak/2) - 1)
        else:
            if streak >= 5:
                relative_bet_size = 0
            elif streak == 1:
                relative_bet_size = 1
            elif streak == 2:
                relative_bet_size = 3
            elif streak == 3:
                relative_bet_size = 8
            elif streak == 4:
                relative_bet_size = 20
            else:
                pass


    # print("Side for Shoe: ", side_for_game)
    # print("Streak Side: ", side)
    # print("Streak Number: ", streak)
    # print("Relative Bet Size: ", relative_bet_size)

    return [relative_bet_size, side_for_game, side, streak]


"""
def calculate_action(seq):
    relative_bet_size = 0

    for i in range(len(seq)):
        if seq[0] == 'T':
            seq = seq[1:]
        else:
            break
    # it's all t, so bet 0 (do nothing by it)
    if len(seq) == 0:
        return [relative_bet_size, '']

    side_for_shoe = seq[0]
    seq = seq[1:]
    # first game after initial ties are done, so start the bet with minimum size (= 1)
    relative_bet_size = 1
    if len(seq) == 0:
        return [relative_bet_size, side_for_shoe]

    streak_num = 0
    streak_side = ''
    while len(seq) != 0:
        if streak_num == 0 and seq[0] != 'T':
            streak_side = seq[0]
            streak_num = 1
        else:
            if seq[0] == 'T':
                pass
            elif seq[0] == streak_side:
                streak_num += 1
            else:
                streak_num = 0
                streak_side = ''
        seq = seq[1:]

    relative_bet_size = calculate_bet_size(side_for_shoe, streak_side, streak_num)

    return [relative_bet_size, side_for_shoe]


def calculate_bet_size(side_for_shoe, streak_side, streak_num):
    print("Side for Shoe: ", side_for_shoe)
    print("Streak Side: ", streak_side)
    print("Streak Number: ", streak_num)
    if streak_num == 0:
        relative_bet_size = 1
    else:
        # winning streak
        if streak_side == side_for_shoe:
            relative_bet_size = 2 ** math.ceil(streak_num/2)
        # losing streak
        else:
            if streak_num >= 4:
                relative_bet_size = 0
            else:
                relative_bet_size = 2 ** streak_num

    return relative_bet_size
"""


