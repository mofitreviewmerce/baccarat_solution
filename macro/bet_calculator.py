import math


anon_game_seq = ['B', 'B', 'P', 'P', 'B', 'P', 'T', 'B', 'P', 'T', 'P', 'B', 'P', 'B', 'P', 'B', 'B', 'B', 'B', 'T', 'P', 'B', 'P', 'B', 'T', 'P', 'P', 'B', 'B', 'B', 'B', 'B', 'B', 'P', 'T', 'B', 'P', 'B', 'B', 'B', 'B', 'P', 'B', 'T', 'P', 'B', 'P', 'P', 'B', 'P', 'B', 'P', 'P', 'B', 'B', 'B', 'B', 'T', 'P', 'T']
deci_game_seq = []


def right_rotate(lists, num):
    output_list = []

    # Will add values from n to the new list
    for item in range(len(lists) - num, len(lists)):
        output_list.append(lists[item])

        # Will add the values before
    # n to the end of new list
    for item in range(0, len(lists) - num):
        output_list.append(lists[item])

    return output_list


def side_for_shoe(seq):
    if len(seq) == 0:
        return ''
    else:
        if seq[0] == 'T':
            return side_for_shoe(seq[1:])
        elif seq[0] == 'B' or seq[0] == 'P':
            return seq[0]
            # return 'P'
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


def calculate_action_martingale(seq, winning_streak, losing_streak, pre_side_to_bet, round_num, loc, just_sat_down):
    relative_bet_size = 0
    streak = 0
    global deci_game_seq
    global anon_game_seq

    if just_sat_down or round_num == 0:
        print("Shoe Started")
        f = open(loc, 'r')
        lines = f.readlines()
        f.close()

        temp_seq = []
        for i in list(lines[-1]):
            if i == 'B' or i == 'P':
                temp_seq.append(i)

        if len(temp_seq) == 0:
            deci_game_seq = anon_game_seq
        else:
            deci_game_seq = temp_seq

    side_to_bet = deci_game_seq[round_num % len(deci_game_seq)]

    print(deci_game_seq)
    print(round_num % len(deci_game_seq))
    print(side_to_bet)

    if winning_streak != 0:
        side_to_bet = pre_side_to_bet
        relative_bet_size = 2 ** (math.ceil(winning_streak/2) - 1)
        streak = winning_streak
    elif losing_streak != 0:
        if losing_streak >= 2:
            side_to_bet == 'B' if pre_side_to_bet == 'P' else 'P'
        relative_bet_size = 2 ** (losing_streak - 1)
        streak = losing_streak
    else:
        relative_bet_size = 0
        streak = 0

    return [relative_bet_size, side_to_bet, '', streak]


"""
def calculate_action_141020(seq):
    streak, side = calculate_streak(seq, 0, '')
    relative_bet_size = 0
    side_to_bet = ''

    if side == 'B':
        side_to_bet = 'P'
    elif side == 'P':
        side_to_bet = 'B'

    if streak >= 3:
        if streak - 3 == 0:
            relative_bet_size = 1
        elif streak - 3 == 1:
            relative_bet_size = 4
        elif streak - 3 == 2:
            relative_bet_size = 10
        elif streak - 3 == 3:
            relative_bet_size = 20
    else:
        relative_bet_size = 0

    return [relative_bet_size, side_to_bet, side, streak]
"""


# 1 3 8 20
"""
def calculate_action_13820(seq):
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

    print("1")
    relative_bet_size = calculate_bet_size(side_for_shoe, streak_side, streak_num)

    print("1")

    return [relative_bet_size, side_for_shoe, streak_side, streak_num]


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
