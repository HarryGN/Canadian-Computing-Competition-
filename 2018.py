# S1
input_list = []
for i in range(4):
    input_list.append(input())

num = "89"
if input_list[0] in num and input_list[1] == input_list[2] and input_list[3] in num:
    print("ignore")
else:
    print("answer")


# S2
input_list = []
for i in range(3):
    input_list.append(input())


li2 = input_list[1]
li3 = input_list[2]
output = 0
for li2e, li3e in zip(li2,li3):
    if li2e == li3e == "C":
        output += 1

print(output)

# S3
a = input()
b = a.split()
for i in range(len(b)):
    b[i] = int(b[i])
for i in range(5):
    c = b.copy()
    c.insert(i, 0)
    # left
    idx = i
    while idx > 0:
        c[idx - 1] = c[idx] + c[idx-1]
        idx -= 1
    #right
    idx = i
    while idx < len(c) - 1:
        c[idx + 1] = c[idx] +c[idx + 1]
        idx += 1
    print (c)

#S4
input_num = input()
input_list = []
for i in range(int(input_num)):
    input_list.append(input().split())

def rotate_90(matrix):
    # flip left-right
    for i in range(len(matrix)):
        for j in range(int(len(matrix)/2)):
            matrix[i][j], matrix[i][-1-j] = matrix[i][-1-j],matrix[i][j]

    # symmetric flip
    for i in range(len(matrix)):
        for idx in range(i+1):
            temp = matrix[i][idx]
            matrix[i][idx] = matrix[idx][i]
            matrix[idx][i] = temp




def check(matrix):

    for i in range(len(matrix)- 1):
        for j in range(len(matrix)-1):
            if matrix[i][j] >= matrix[i][j+1] or matrix[i][j] >= matrix[i+1][j]:
                return False

    return True



while check(input_list) == False:
    rotate_90(input_list)

for i in range(int(input_num)):
    result = ''
    for j in range(len(input_list[i])):
        result = result + input_list[i][j] + ' '
    print(result[:-1])










