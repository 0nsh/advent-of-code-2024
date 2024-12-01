#https://adventofcode.com/2024/day/1#part2

with open("input.txt", "r") as file:
    data = file.readlines()

array_1, count_array_2 = [], dict()

for line in data:
    num_1, num_2 = map(int, line.split())
    array_1.append(num_1)
    count_array_2[num_2] = count_array_2.get(num_2, 0) + 1

result = 0
for i in range(len(array_1)):
    result += array_1[i] * count_array_2.get(array_1[i], 0)

print(result)
