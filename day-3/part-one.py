import re
with open("input.txt", "r") as file:
    data = file.readlines()


def find_mul_instances(text):
    # Pattern to match mul(digits, digits)
    pattern = r'mul\((\d+),\s*(\d+)\)'
    
    # Find all matches in the text
    matches = re.findall(pattern, text)
    
    return matches


muls = []
for line in data:
    muls.extend(find_mul_instances(line))

result = 0
for (i, j) in muls:
    i_n, j_n = int(i), int(j)
    if i_n // 1000 < 1 and j_n // 1000< 1:
        result += i_n * j_n
print(result)
