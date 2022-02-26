#S1
input_list = []
for i in range(2):
    input_list.append(input())
if int(input_list[0]) > 0 and int(input_list[1]) > 0:
    print("1")
elif int(input_list[0]) < 0 and int(input_list[1]) > 0:
    print("2")
elif int(input_list[0]) < 0 and int(input_list[1]) < 0:
    print("3")
elif int(input_list[0]) > 0 and int(input_list[1]) < 0:
    print("4")
else:
    print("X!=0, Y!=0")

#S2
input_list = []
for i in range(2):
    input_list.append(input())
result = int(input_list[0])
k = int(input_list[1])
a = int(input_list[0])
for i in range(1, k+1):
    result = result + a*10
    a = a*10
print(result)

#S3
input_list = []
for i in range(3):
    input_list.append(input())
#estimated route
t = int(input_list[2])
a = input_list[0].split()
b = input_list[1].split()
for i in range(len(a)):
    a[i] = int(a[i])
for i in range(len(b)):
    b[i] = int(b[i])
if abs(a[0] - b[0]) + abs(a[1] - b[1]) > t:
    print("N")
elif abs(a[0] - b[0]) + abs(a[1] - b[1]) == t:
    print("Y")
elif abs(a[0] - b[0]) + abs(a[1] - b[1]) < t:
    if (t - (abs(a[0] - b[0]) + abs(a[1] - b[1])))% 2 == 0 :
        print("Y")
    else:
        print('N')

#S4
a = input()
a = int(a)
start_h = 12
counter = 0

for i in range(1, a+1):
    curr_h = i // 60
    curr_min = i % 60

    total_hr = (curr_h + start_h) % 12
    if total_hr == 0:
        total_hr = 12

    curr_min = str(curr_min)
    if len(curr_min) == 1:
        curr_min = '0' + curr_min

    total = str(total_hr) + curr_min

    flag = 10
    for x in range(len(total)-2):
        if not int(total[x+1]) - int(total[x]) == int(total[x+2]) - int(total[x+1]):
            flag = 11
            break

    if flag == 10:
        counter += 1
print(counter)

# "Favourite Times" J4 2017
# Alec Dewulf
# December 26, 2019
# An extremely long problem that requires you to literlly make a clock

duration = int(input())

# starting time is 12: 00
time = [1, 2, 0, 0]

y = 0
num_sequence = 0

while y < duration:
    # FOUR DIGIT TIME
    if len(time) == 4:
        # not a new multiple of ten minutes in 4 digit time
        if time[3] != 9:
            new_min = time[3] + 1
            time.pop(3)
            time.append(new_min)

        # is a new multiple of ten minutes in 4 digit time
        elif time[3] == 9 and time[2] != 5:
            time.pop(3)
            new_min = time[2] + 1
            time.pop(2)
            time.append(new_min)
            time.append(0)

        # for 12:59
        elif sum(time) == 17:
            time = [1, 0, 0]

        # normal hour for 4 digits
        elif time[2] == 5 and time[3] == 9:
            new_hour = time[1] + 1
            time = [1, new_hour, 0, 0]

    # 12:34 is an arithamtic sequence
    if len(time) == 4:
        if time[1] == 2 and time[2] == 3 and time[3] == 4:
            num_sequence += 1


    # THREE DIGIT TIME
    elif len(time) == 3:
        # three digit time new minute
        if time[2] != 9:
            new_min = time[2] + 1
            time.pop(2)
            time.append(new_min)
        # 100
        # three digit time new multiple of 10 minutes
        elif time[2] == 9 and time[1] != 5:
            new_min = time[1] + 1
            time.pop(2)
            time.pop(1)
            time.append(new_min)
            time.append(0)
        # adding a new normal hour
        elif time[2] == 9 and time[1] == 5 and time[0] != 9:
            new_hour = time[0] + 1
            time = [new_hour, 0, 0]
        # going from 9:59 to 10:00
        elif time[0] == 9 and time[1] == 5 and time[2] == 9:
            time = [1, 0, 0, 0]

        # checking for an arithmatic sequence
        for i in range(0, 5):
            if time[0] + i == time[1] and time[1] + i == time[2]:
                num_sequence += 1
            elif time[0] - i == time[1] and time[1] - i == time[2]:
                num_sequence += 1

    y += 1

print(num_sequence)






















