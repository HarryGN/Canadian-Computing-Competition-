input_list = []
for i in range(3):
    input_list.append(input())

counter = 0

def total_calculation(counter):
    total = 0
    for i in range(counter):
        total += int(input_list[1]) * pow(int(input_list[2]),i )
    return total
while total_calculation(counter) <= int(input_list[0]):
    counter += 1
    total_calculation(counter)
counter -= 1
print(counter)











