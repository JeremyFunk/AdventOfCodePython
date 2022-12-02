f = open('input.txt', 'r')

elements = []
max_cals = 0
for line in f:
    if not line.strip():
        calories = 0
        for element in elements:
            calories += int(element)
        if(calories > max_cals):
            max_cals = calories
        elements = []
    else:
        elements.append(line.strip())
f.close()

print(max_cals)