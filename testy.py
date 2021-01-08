import macro.bet_calculator as bet_calculator

game_seq = ['B', 'P', 'P', 'P', 'P', 'P', 'T', 'P', 'B', 'B', 'B', 'P', 'B', 'P', 'B', 'B']
side_for_shoe = 'B'
temp_seq = []
dist_dic = {}

for i in game_seq:
    if i != 'T':
        temp_seq.append(i)

print(temp_seq)

while len(temp_seq) != 0:
    streak, side = bet_calculator.calculate_streak(temp_seq, 0, side_for_shoe)
    dist_str = str(side) + str(streak)
    if dist_str in dist_dic:
        dist_dic[dist_str] += 1
    else:
        dist_dic[dist_str] = 1
    temp_seq = temp_seq[:-streak]

print(dist_dic)
