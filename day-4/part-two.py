
with open("input.txt", "r") as file:
    data = file.readlines()

XMAS = "MAS"
result = 0

for r in range(len(data)):
    data[r] = data[r].replace("\n", "")
    row = data[r]

    for c in range(len(row)):
        if r + 2 < len(data) and c + 2 < len(row):
            # diagonal one
            d1 =  f"{data[r][c]}{data[r+1][c+1]}{data[r+2][c+2]}"
            d2 =  f"{data[r+2][c]}{data[r+1][c+1]}{data[r][c+2]}"
            if (d1 == XMAS or d1[::-1] == XMAS) and (d2 == XMAS or d2[::-1] == XMAS):
                result += 1

print(result)