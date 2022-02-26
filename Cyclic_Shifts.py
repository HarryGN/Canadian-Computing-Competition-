input_list = []
for i in range(2):
    input_list.append(input())

T = input_list[0]
S = input_list[1]

cyclic_list = []

for _ in range(len(S)):
    cyclic = S[1:] + S[0]
    cyclic_list.append(cyclic)
    S = cyclic

result = 'no'
for cyclic in cyclic_list:
    if cyclic in T:
        result = 'yes'

print(result)