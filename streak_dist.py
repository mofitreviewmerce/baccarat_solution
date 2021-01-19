import macro.bet_calculator as bet_calculator


def f1(x):
    return x[0]


loc_str1 = './data/log_' + 'c543' + '.txt'
f = open(loc_str1)
lines = f.readlines()
f.close()

temp_seq = []
seq_list = []

for line in lines:
    for i in list(line):
        if i == 'B' or i == 'T' or i == 'P':
            temp_seq.append(i)
    seq_list.append(temp_seq)
    temp_seq = []

distribution_dict = {}

for seq in seq_list:
    temp_seq = []
    for ele in seq:
        if ele != 'T':
            temp_seq.append(ele)

    while len(temp_seq) != 0:
        streak, side = bet_calculator.calculate_streak(temp_seq, 0, '')
        winlose = "B" if side == 'B' else "P"
        dist_str = str(winlose) + str(streak)
        print(dist_str, " ", temp_seq[:-streak])
        if dist_str in distribution_dict:
            distribution_dict[dist_str] += 1
        else:
            distribution_dict[dist_str] = 1

        temp_seq = temp_seq[:-streak]

loc_str2 = './data/' + 'c543' + '_distribution.txt'
p = open(loc_str2, 'a')
res = sorted(distribution_dict.items(), key=f1, reverse=True)
for i in res:
    dist_str = i[0] + "," + str(i[1]) + "\n"
    p.write(dist_str)
p.close()
