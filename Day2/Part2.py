# read temp.txt line by line

f = open('input.txt', 'r')

individual_value = {"A": 1, "B": 2, "C": 3}

score = 0

for line in f:
    elements = line.split()
    value1 = individual_value[elements[0]]

    if(elements[1] == "X"):
        score += 0
        
        if(value1 == 1):
            score += 3
        if(value1 == 2):
            score += 1
        if(value1 == 3):
            score += 2
    elif(elements[1] == "Y"):
        score += 3
        score += value1
    elif(elements[1] == "Z"):
        score += 6
        
        if(value1 == 1):
            score += 2
        if(value1 == 2):
            score += 3
        if(value1 == 3):
            score += 1

    
f.close()

print(score)