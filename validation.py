special_seq = ['B', 'B', 'P', 'P', 'B', 'B', 'P', 'P', 'B', 'B']

f = open('./data/log_c543.txt', 'r')
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

line_num = 1
digit_len = 10
seq_unique_seq = []
new_seq = []
unique_seq_num = 0
for seq in seq_list:
    new_seq = []
    gs_len = len(seq)
    for i in range(gs_len-digit_len):
        special_seq = seq[i:i+digit_len]
        if special_seq not in new_seq:
            new_seq.append(special_seq)

    seq_unique_seq.append(new_seq)
    print(new_seq)
    print(len(new_seq))

    line_num += 1
    unique_seq_num += len(new_seq)

print(unique_seq_num/line_num)

line_num = 0
special_seq_num = 0
list_of_dict = []
total_dict = {}
for seq in seq_list:
    temp_dict = {}
    for special_seq in seq_unique_seq[line_num]:
        special_seq_num = 0
        sp_len = len(special_seq)
        gs_len = len(seq)
        temp_count = 0
        for i in range(gs_len-sp_len):
            if i == 0:
                pass
            else:
                j = 0
                while seq[i+j] == special_seq[j]:
                    temp_count += 1
                    j += 1
                    if temp_count == digit_len:
                        break

                if temp_count == digit_len:
                    if str(special_seq) in total_dict:
                        total_dict[str(special_seq)] += 1
                    else:
                        total_dict[str(special_seq)] = 1

                    if str(special_seq) in temp_dict:
                        temp_dict[str(special_seq)] += 1
                    else:
                        temp_dict[str(special_seq)] = 1
                    temp_count = 0
                else:
                    temp_count = 0

    list_of_dict.append(temp_dict)

    line_num += 1

p = open('./data/unique543.txt', 'a')
for i in range(len(list_of_dict)):
    data = str(seq_list[i]) + '\n' + str(list_of_dict[i]) + '\n' + '\n'
    p.write(data)
p.close()

sorted_total_dict = dict(sorted(total_dict.items(), key=lambda item: item[1]))
print(sorted_total_dict)

sorted_list_of_dict = []
for adict in list_of_dict:
    sorted_list_of_dict.append(dict(sorted(adict.items(), key=lambda item: item[1])))

for i in sorted_list_of_dict:
    p = open('./data/unique543.txt', 'a')
    data = str(i) + '\n'
    p.write(data)
    p.close()
    print(i)
    print(len(i))
