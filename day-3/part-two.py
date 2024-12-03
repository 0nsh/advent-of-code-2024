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
data = "".join(data)
parts = data.split("don't()")
process_parts = [parts[0]]

for part in parts[1:]:
    if "do()" in part:
        process_parts.extend(part.split("do()")[1:])

for part in process_parts:
    muls.extend(find_mul_instances(part))

result = 0
for (i, j) in muls:
    i_n, j_n = int(i), int(j)
    if i_n // 1000 < 1 and j_n // 1000< 1:
        result += i_n * j_n
print(result)
