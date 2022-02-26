# S1
input_list = []
for i in range(int(6)):
    input_list.append(input())
win_counter = 0
loss_counter = 0
for i in input_list:
    if i == "W":
        win_counter += 1
    else:
        loss_counter += 1
if win_counter == 1 or win_counter == 2:
    print("3")
elif win_counter == 3 or win_counter == 4:
    print("2")
elif win_counter == 5 or win_counter == 6:
    print("1")
else:
    print("-1")

# S2

def row_sum(matrix, row_num):
    sum = 0
    for i in range(4):
        sum += int(matrix[row_num][i])

    return sum


def col_sum(matrix, col_num):
    sum = 0
    for i in range(4):
        sum += int(matrix[i][col_num])

    return sum

input_list = []
for i in range(int(4)):
    input_list.append(input().split())
#horizontal sum
h_sum = 0

sum_row_1 = row_sum(input_list, 0)
sum_row_2 = row_sum(input_list, 1)
sum_row_3 = row_sum(input_list, 2)
sum_row_4 = row_sum(input_list, 3)


sum_col_1 = col_sum(input_list, 0)
sum_col_2 = col_sum(input_list, 1)
sum_col_3 = col_sum(input_list, 2)
sum_col_4 = col_sum(input_list, 3)

if sum_row_1 == sum_row_2 == sum_row_3 == sum_row_4 == sum_col_1 == sum_col_2 == sum_col_3 == sum_col_4:
    print('MAGIC')
else:
    print("NOT MAGIC")

S3
a = input()

def palindromes(word):
    i = 0
    j = len(word) - 1

    if len(word) == 0:
        return 0

    while i != j and i+1 != j:
        if word[i] == word[j]:
            i += 1
            j -= 1
        else:
            return 0

    if i+1 == j:
        if word[i] != word[j]:
            return 0

    return len(word)

# check

result_num = 0
for i in range(len(a)):
    for j in range(len(a), -1, -1):
        word = a[i:j]
        max_num = palindromes(word)
        result_num = max(max_num, result_num)
print (result_num)





print(palindromes(a))

# S4
d_time = list(input())
del d_time[2]

# converting to integers
x = 0
while x < len(d_time):
    d_time[x] = int(d_time[x])

    x += 1

ten = [1, 0, 0, 0]
time = 0
add_time = 1

# Cycling through two hours of time
while time != 120:
    # Defining rush hour
    if d_time[1] >= 7 and d_time[1] <= 9 or d_time == ten:
        rush_hour = True
    else:
        rush_hour = False

    if rush_hour == True:
        add_time = 0.5
    else:
        add_time = 1
    # new minute
    if d_time[3] != 9 and d_time[1] != 4:
        d_time[3] += 1

    # new multiple of ten miinutes
    elif d_time[3] == 9 and d_time[2] != 5:
        d_time[3] = 0
        d_time[2] += 1

    # new one-digit hour
    elif d_time[3] == 9 and d_time[2] == 5 and d_time[1] != 9:
        d_time[1] += 1
        d_time[2] = 0
        d_time[3] = 0

    # switch to 10
    elif d_time[1] == 9 and d_time[2] == 5 and d_time[3] == 9:
        d_time[0] = 1
        d_time[1] = 0
        d_time[2] = 0
        d_time[3] = 0

    # new two-digit time
    elif d_time[2] == 5 and d_time[3] == 9 and d_time[0] == 1:
        # not to 20
        if d_time[1] != 9:
            d_time[1] += 1
        # to 20
        elif d_time[1] == 9:
            d_time[0] = 2
            d_time[1] = 0
            d_time[2] = 0
            d_time[3] = 0
    # to 00:01
    elif d_time[0] == 2 and d_time[1] == 4:
        d_time[0] = 0
        d_time[1] = 0
        d_time[2] = 0
        d_time[3] = 1
    time += add_time

print(d_time[0], d_time[1], ':', d_time[2], d_time[3])

#S5
question = int(input())
num_people = int(input())
dmoj_v = input().split()
peg_v = input().split()

# convert lists to ints
for s in range(len(dmoj_v)):
    dmoj_v[s] = int(dmoj_v[s])

for s in range(len(peg_v)):
    peg_v[s] = int(peg_v[s])

# problem one
if question == 1:
    x, total_speed = 0, 0
    while x < num_people:
        speeds = [max(dmoj_v), max(peg_v)]
        bike_speed = max(speeds)

        # take used up speeds off of the list
        dmoj_v.pop(dmoj_v.index(max(dmoj_v)))
        peg_v.pop(peg_v.index(max(peg_v)))

        # add to total speed and reset bike speed
        total_speed += bike_speed
        bike_speed = 0

        x += 1

elif question == 2:
    x, total_speed = 0,0
    while x < num_people:
        speeds = [max(dmoj_v), min(peg_v)]
        bike_speed = max(speeds)

        dmoj_v.pop(dmoj_v.index(max(dmoj_v)))
        peg_v.pop(peg_v.index(min(peg_v)))

        total_speed += bike_speed
        bike_speed = 0

        x += 1

# output results
print(total_speed)




