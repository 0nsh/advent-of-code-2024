with open("example.txt", "r") as file:
    data = file.readlines()


def is_safe(array) -> bool:
    diff = []
    negatives, positives = 0, 0
    for i in range(1, len(array)):
        diff.append(abs(array[i] - array[i - 1]))
        if array[i] - array[i - 1] < 0:
            negatives += 1
        elif array[i] - array[i - 1] > 0:
            positives += 1

    if(negatives == 0 or positives == 0) and max(diff) <= 3 and min(diff) >= 1:
        return True
    else:
        return False

safe, unsafe = 0, 0
for line in data:
    array = list(map(int, line.split()))
    if is_safe(array):
        safe += 1
    else:
        unsafe += 1

print(safe, unsafe)
