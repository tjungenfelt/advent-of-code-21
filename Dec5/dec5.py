import fileinput

lines = []
with fileinput.input(files=('input.txt')) as f:
    for line in f:
        lines.append(line.strip())

coord = []

for line in lines:
    line = line.split(' -> ')
    line = [x.split(',') for x in line]
    line = [int(elem) for x in line for elem in x]
    coord.append(line)

d = dict()

# PART I

for i in range(0, len(coord)):
    x = [coord[i][0], coord[i][2]]
    y = [coord[i][1], coord[i][3]]
    if (x[0] == x[1]) or (y[0] == y[1]):
        x = sorted(x)
        y = sorted(y)
        for j in range(x[0], x[1]+1):
            for k in range(y[0], y[1]+1):
                if (k, j) not in d:
                     d[(k, j)] = 1
                else:
                    d[(k, j)] += 1

print(len([val for val in d.values() if val > 1]))


# PART II
d2 = dict()

for i in range(0, len(coord)):
    x = [coord[i][0], coord[i][2]]
    y = [coord[i][1], coord[i][3]]
    if (x[0] == x[1]) or (y[0] == y[1]):
        x = sorted(x)
        y = sorted(y)
        for j in range(x[0], x[1]+1):
            for k in range(y[0], y[1]+1):
                if (k, j) not in d2:
                     d2[(k, j)] = 1
                else:
                    d2[(k, j)] += 1
    else:
        r1 = list(range(x[0], x[1]))
        r2 = list(range(y[0], y[1]))
        print(r1)
        #for i in range(0,len(r1)):
        #    if (r2[i], r1[i]) not in d2:
        #         d2[(r2[i], r1[i])] = 1
        #    else:
        #        d2[(r2[i], r1[i])] += 1

#print(len([val for val in d2.values() if val > 1]))