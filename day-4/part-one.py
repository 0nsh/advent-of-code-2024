
with open("input.txt", "r") as file:
    data = file.readlines()

XMAS = "XMAS"
result = 0

for r in range(len(data)):
    data[r] = data[r].replace("\n", "")
    row = data[r]

    for c in range(len(row)):
        # left
        if c >= 3 and row[c-3:c+1][::-1] == XMAS:
            result += 1

        # right
        if c + 3 < len(row) and row[c:c+4] == XMAS:
            result += 1

        # up
        if r >= 3 and f"{data[r][c]}{data[r-1][c]}{data[r-2][c]}{data[r-3][c]}" == XMAS:
            result += 1

        # bottom
        if r + 3 < len(data) and f"{data[r][c]}{data[r+1][c]}{data[r+2][c]}{data[r+3][c]}" == XMAS:
            result += 1

        # daigonal up left
        if r >= 3 and c >= 3 and f"{data[r][c]}{data[r-1][c-1]}{data[r-2][c-2]}{data[r-3][c-3]}" == XMAS:
            result += 1

        # diagonal up right
        if r >= 3 and c + 3 < len(row) and f"{data[r][c]}{data[r-1][c+1]}{data[r-2][c+2]}{data[r-3][c+3]}" == XMAS:
            result += 1

        # diagonal down left
        if r + 3 < len(data) and c >= 3 and f"{data[r][c]}{data[r+1][c-1]}{data[r+2][c-2]}{data[r+3][c-3]}" == XMAS:
            result += 1

        # diagonal down right
        if r + 3 < len(data) and c + 3 < len(row) and f"{data[r][c]}{data[r+1][c+1]}{data[r+2][c+2]}{data[r+3][c+3]}" == XMAS:
            result += 1
    

print(result)