input_list = []
for i in range(3):
    input_list.append(input())
a = int(input_list[0])
b = int(input_list[1])
c = int(input_list[2])

total_score = 1 * a + 2 * b + 3 * c
if total_score < 10:
    print("sad")
elif total_score >= 10:
    print("happy")

