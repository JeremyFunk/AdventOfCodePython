f = open('input.txt', 'r')

# read temp.txt line by line
priorities = []
for line in f:
    firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
    found = False
    for i in range(len(firstpart)):
        for j in range(len(secondpart)):
            if(firstpart[i] == secondpart[j]):
                if(firstpart[i].isupper()):
                    priorities.append(ord(firstpart[i]) - 38)
                else:
                    priorities.append(ord(firstpart[i]) - 96)
                found = True
                break
        if(found):
            break

f.close()

total_priority = 0
for i in range(len(priorities)):
    total_priority += priorities[i]
print(total_priority)