f = open('input.txt', 'r')

containers = []
for line in f:
    containers.append(line)
    if(line[0].isdigit()):
        break

stacks = []
for i in range(9):
    stack = []
    for j in range(len(containers) - 1):
        character = containers[j].split(" ")[i]
        if(character != ""):
            stack.append(character)
    stacks.append(stack)

print(stacks)
