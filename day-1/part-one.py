# https://adventofcode.com/2024/day/1#part1

with open("input.txt", "r") as file:
    data = file.readlines()

array_1, array_2 = [], []

for line in data:
    array_1.append(int(line.split()[0]))
    array_2.append(int(line.split()[1]))

array_1.sort()
array_2.sort()

result = 0
for i in range(len(array_1)):
    result += abs(array_1[i] - array_2[i])

print(result)
