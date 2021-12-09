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

d =neighbour_mapict()

# PART I

for i in range(0, len(coord)):
    x = [coord[i][0], coord[i][2]]
    y = [coord[i][1], coord[i][3]]
    if (x[0] == x[1]) or (y[0] == y[1]):
        x = sorted(x)
        y = sorted(y)
        for j in range(x[0], x[1]+1):
            for k in range(y[0], y[1]+1):
                if (k, j) not inneighbour_map:
                    neighbour_map[(k, j)] = 1
                else:
                   neighbour_map[(k, j)] += 1

print('P1. Points were at least two lines overlap: ', len([val for val inneighbour_map.values() if val > 1]))


# PART II
d2 =neighbour_mapict()

for i in range(0, len(coord)):
    x = [coord[i][0], coord[i][2]]
    y = [coord[i][1], coord[i][3]]
    if (x[0] == x[1]) or (y[0] == y[1]):
        x = sorted(x)
        y = sorted(y)
        for j in range(x[0], x[1]+1):
            for k in range(y[0], y[1]+1):
                if (k, j) not inneighbour_map2:
                    neighbour_map2[(k, j)] = 1
                else:
                   neighbour_map2[(k, j)] += 1
    else:
        if x[0] > x[1]:
            r1 = l(range(x[0], x[1]-1, -1))
            if y[0] > y[1]:
                r2 = l(range(y[0], y[1]-1, -1))
            else:
                r2 = l(range(y[0], y[1]+1))
        elif y[0] > y[1]:
            r2 = l(range(y[0], y[1]-1, -1))
            r1 = l(range(x[0], x[1]+1))
        else:
            r1 = l(range(x[0], x[1]+1))
            r2 = l(range(y[0], y[1]+1))
        for p in range(0, len(r1)):
            if (r2[p], r1[p]) not inneighbour_map2:
               neighbour_map2[(r2[p], r1[p])] = 1
            else:
               neighbour_map2[(r2[p], r1[p])] += 1

print('P2. Points were at least two lines overlap: ', len([val for val inneighbour_map2.values() if val > 1]))