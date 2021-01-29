import macro.bet_calculator as bet_calculator
import time
import sys


def calculate_income(side_for_game, seq, pre_relative_bet_size):
    if seq[-1] == side_for_game:
        return pre_relative_bet_size
    elif seq[-1] == 'T':
        return 0
    else:
        return -1 * pre_relative_bet_size


def f1(x):
    return x[0]


p = open("./data/shoeResult.txt", 'a')

result_seq = []
distribution_dict = {}
last_streak_dict = {}

for i in range(1):
    # sampleLoc = "./data/sample" + str(i+1) + ".txt"
    sampleLoc = "./data/8_10000_260121164427.txt"
    f = open(sampleLoc)

    add_element = False
    seq_temp = []
    seq_list = []

    count = 0
    while True:
        if (count % 10000) == 0:
            print("\r", end='')
            print("Progress: ", (count // 10000)/10, "%                  ", end='', sep='')
            sys.stdout.flush()
        line = f.readline()
        if not line:
            break

        if add_element:
            if line[0] == 'B' or line[0] == 'T' or line[0] == 'P':
                seq_temp.append(line[0])

        if line[:11] == "Shoe number":
            add_element = True
        elif line[:12] == "Shoe results":
            add_element = False
            seq_list.append(seq_temp)
            seq_temp = []
            count += 1

    f.close()

    total_result = 0
    shoe_counter = 0
    for seq in seq_list:
        game_seq = []
        side_for_shoe = ''
        pre_relative_bet_size = 0
        relative_bet_size = 0
        just_sat_down = False
        asset = 0
        shoe_result = 0

        for round_result in seq:
            game_seq.append(round_result)
            relative_bet_size, side_for_shoe, streak_side, streak_number = bet_calculator.calculate_action(game_seq)
            if just_sat_down:
                if relative_bet_size <= 1:
                    just_sat_down = False
                    last_result = calculate_income(side_for_shoe, game_seq, pre_relative_bet_size)
                    shoe_result += last_result
                    print(relative_bet_size, side_for_shoe, streak_side, streak_number)
                    print(last_result, relative_bet_size, shoe_result)
                else:
                    last_result = 0
                    shoe_result += last_result
                    print(relative_bet_size, side_for_shoe, streak_side, streak_number)
                    print(last_result, relative_bet_size, shoe_result)
            else:
                last_result = calculate_income(side_for_shoe, game_seq, pre_relative_bet_size)
                shoe_result += last_result
                print(relative_bet_size, side_for_shoe, streak_side, streak_number)
                print(last_result, relative_bet_size, shoe_result)
            pre_relative_bet_size = relative_bet_size
        print(game_seq)

        temp_seq = []
        for ele in game_seq:
            if ele != 'T':
                temp_seq.append(ele)

        is_last = True
        while len(temp_seq) != 0:
            streak, side = bet_calculator.calculate_streak(temp_seq, 0, side_for_shoe)
            winlose = "W" if side == side_for_shoe else "L"
            dist_str = str(winlose) + str(streak)
            print(dist_str, " ", temp_seq[:-streak])
            if dist_str in distribution_dict:
                distribution_dict[dist_str] += 1
            else:
                distribution_dict[dist_str] = 1

            if is_last:
                is_last = False
                if dist_str in last_streak_dict:
                    last_streak_dict[dist_str] += 1
                else:
                    last_streak_dict[dist_str] = 1

            temp_seq = temp_seq[:-streak]

        print("Shoe Result:", shoe_counter)
        shoe_str = str(shoe_result) + "," + "\n"
        p.write(shoe_str)
        total_result += shoe_result
        shoe_counter += 1

        if shoe_counter == 1:
            break

    result_seq.append(total_result)

res = sorted(distribution_dict.items(), key=f1, reverse=True)
for i in res:
    dist_str = i[0] + "," + str(i[1]) + "\n"
    p.write(dist_str)
p.close()

print(result_seq)
print(res)
print(last_streak_dict)
