f = open('input.txt', 'r')

elements = []
max_cals = []
for line in f:
    if not line.strip():
        calories = 0
        for element in elements:
            calories += int(element)
        max_cals.append(calories)
        elements = []
    else:
        elements.append(line.strip())
f.close()

max_cals.sort()
print(max_cals[-1] + max_cals[-2] + max_cals[-3])