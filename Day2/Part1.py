# read temp.txt line by line

f = open('input.txt', 'r')

individual_value = {"X": 1, "Y": 2, "Z": 3, "A": 1, "B": 2, "C": 3}

score = 0

for line in f:
    elements = line.split()
    value1 = individual_value[elements[0]]
    value2 = individual_value[elements[1]]
    score += value2

    if(value1 == value2):
        score += 3
    if(value1 == 1 and value2 == 2) or (value1 == 2 and value2 == 3) or (value1 == 3 and value2 == 1):
        score += 6
    
    
f.close()

print(score)