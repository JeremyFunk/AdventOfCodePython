f = open('input.txt', 'r')

# read temp.txt line by line
priorities = []
lines = []
for line in f:
    lines.append(line)

for i in range(0, len(lines), 3):

    found = False
    for j in range(len(lines[i])):
        for x in range(len(lines[i + 1])):
            for y in range(len(lines[i + 2])):
                if lines[i][j] == lines[i + 1][x] and lines[i][j] == lines[i + 2][y]:
                    if(lines[i][j].isupper()):
                        priorities.append(ord(lines[i][j]) - 38)
                    else:
                        priorities.append(ord(lines[i][j]) - 96)
                    found = True
                    break
            if(found):
                break
        if(found):
            break

f.close()

total_priority = 0
for i in range(len(priorities)):
    total_priority += priorities[i]
print(total_priority)