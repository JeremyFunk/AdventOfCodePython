f = open('input.txt', 'r')

contained_pairs = []
for line in f:
    pairs = line.split(",")
    pair1 = pairs[0].split("-")
    lower1 = int(pair1[0])
    upper1 = int(pair1[1])
    pair2 = pairs[1].split("-")
    lower2 = int(pair2[0])
    upper2 = int(pair2[1])

    if(not (lower1 > upper2 or upper1 < lower2)):
        contained_pairs.append((lower2, upper2))

print(len(contained_pairs))