

def result(score):
    a = score[0] * 3 + score[1] * 2 + score[2] * 1
    b = score[3] * 3 + score[4] * 2 + score[5] * 1
    if a < b:
        return "B"
    if a > b:
        return "A"
    if a == b:
        return "T"

score = [10, 3, 7, 8, 9, 6]


print(result(score))

def decode(string):
    # “num symbol”
    result = []

    for i in range(len(string)):
        a = string[i].split(" ")
        line = int(a[0]) * a[1]
        # result.append(line)
        print(line)

string = ["9 +", "4 -", "3 ="]
decode(string)


# S3
result_string = ""

input_str = "3.14155555"


index = 0

while index<len(input_str):

    char = input_str[index]
    check_index = index + 1
    num = 1
    while check_index < len(input_str) and input_str[check_index] == char:
        check_index += 1
        num += 1

    result_string += ' ' + str(num) + " " + char

    index = check_index


print result_string[1:]



li1 = [1,2]
li2 = [3,4]
def horizontal_flip(li1,li2):
    li1[0], li2[0] = li2[0], li1[0]
    li1[1], li2[1] = li2[1], li1[1]
def vertical_flip(li1,li2):
    li1[0], li1[1] = li1[1], li1[0]
    li2[0], li2[1] = li2[1], li2[0]
input_str = input()
for i in input_str :
    if i == "H":
        horizontal_flip(li1,li2)

    elif i == "V":
        vertical_flip(li1, li2)
    else:
        print("error")
string1 = str(li1[0])+ " " + str(li1[1])
string2 = str(li2[0]) + " " + str(li2[1])
print(string1)
print(string2)

# S5
orig_1, rep_1 = input().split()
orig_2, rep_2 = input().split()
orig_3, rep_3 = input().split()

step, orig, final = input().split()

sequence = []


def helper(str_in, orig_seq, rep_seq, num):
    idx = str_in.find(orig_seq)

    if idx != -1:
        return [str(num) + ' ' + str(idx + 1) + ' ' + str_in[: idx] + rep_seq + str_in[idx + len(orig_seq):]]


cond_1 = helper(orig, orig_1, rep_1, 1)
if cond_1:
    sequence.append(cond_1)

cond_2 = helper(orig, orig_2, rep_2, 2)
if cond_2:
    sequence.append(cond_2)

cond_3 = helper(orig, orig_3, rep_3, 3)
if cond_3:
    sequence.append(cond_3)

print(sequence)
for _ in range(int(step) - 1):

    iteration = len(sequence)

    for _ in range(iteration):

        curr_seq = sequence.pop(0)
        last = curr_seq[-1]
        # print last
        curr_word = last.split()[-1]

        curr_seq_1 = curr_seq[:]
        cond_1 = helper(curr_word, orig_1, rep_1, 1)
        if cond_1:
            curr_seq_1 += cond_1
            sequence.append(curr_seq_1)

        curr_seq_2 = curr_seq[:]
        cond_2 = helper(curr_word, orig_2, rep_2, 2)
        if cond_2:
            curr_seq_2 += cond_2
            sequence.append(curr_seq_2)

        curr_seq_3 = curr_seq[:]
        cond_3 = helper(curr_word, orig_3, rep_3, 3)
        if cond_3:
            curr_seq_3 += cond_3
            sequence.append(curr_seq_3)

print(sequence)

for seq in sequence:
    if len(seq) >= 4:
        if seq[3].split()[-1] == final:
            for s in seq:
                print(s)
            break














