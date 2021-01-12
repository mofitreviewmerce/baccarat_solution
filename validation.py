special_seq = ['B', 'B', 'P', 'P', 'B', 'P', 'B', 'P']

f = open('./data/log_c4.txt', 'r')
lines = f.readlines()
f.close()

seq_list = []
temp_seq = []
for line in lines:
    for i in list(line):
        if i == 'B' or i == 'P':
            temp_seq.append(i)
    seq_list.append(temp_seq)
    temp_seq = []

for seq in seq_list:
    sp_len = len(special_seq)
    gs_len = len(seq)
    temp_count = 0
    for i in range(gs_len-sp_len):
        j = 0
        while seq[i+j] == special_seq[j]:
            temp_count += 1
            j += 1
            if temp_count == 8:
                break

        if temp_count == 8:
            print(seq)
            print(i+1)
            temp_count = 0
        else:
            temp_count = 0
