import fileinput
from itertools import islice

lines = []
with fileinput.input(files=('input.txt')) as f:
    for line in f:
        lines.append(line.strip())

height = []
for i in lines:
    height.append([int(x) for x in i ])
final = 0

#PART I
low_points = []

for i in range(0, len(height)):
    for j in range(0, len(height[0])):
        if i == 0:
            if j == 0:
                n = [height[i][j + 1], height[i + 1][j]]
            elif j == len(height[0])-1:
                n = [height[i][j - 1], height[i + 1][j]]
            else:
                n = [height[i][j + 1], height[i][j - 1], height[i + 1][j]]
        elif j == 0:
            if i == len(height)-1:
                n = [height[i][j + 1], height[i - 1][j]]
            else:
                n = [height[i][j + 1], height[i - 1][j], height[i + 1][j]]
        elif i == len(height)-1:
            if j == len(height[0])-1:
                n = [height[i][j - 1], height[i - 1][j]]
            else:
                n = [height[i][j + 1], height[i][j - 1], height[i - 1][j]]
        elif j == len(height[0])-1:
            n = [height[i + 1][j], height[i][j - 1], height[i - 1][j]]
        else:
            n = [height[i + 1][j], height[i][j - 1], height[i - 1][j], height[i][j + 1]]
        bool = []
        for num in n:
            if height[i][j] < num:
                bool.append(True)
            else:
                bool.append(False)
        if sum(bool) == len(bool):
            low_points.append((i, j))
            final += height[i][j] + 1

print(final)

# PART II

neighbour_map = dict()
basin = 0
l = set()

for i in range(0, len(height)):
    for j in range(0, len(height[0])):
        if i == 0:
            if j == 0:
                neighbour_map[(i, j)] = {(i, j + 1), (i + 1,j)}
            elif j == len(height[0])-1:
                neighbour_map[(i, j)] = {(i, j - 1), (i + 1, j)}
            else:
                neighbour_map[(i, j)] = {(i, j + 1), (i, j - 1), (i + 1, j)}
        elif j == 0:
            if i == len(height)-1:
                neighbour_map[(i, j)] = {(i, j + 1), (i - 1, j)}
            else:
                neighbour_map[(i, j)] = {(i, j + 1), (i - 1, j), (i + 1, j)}
        elif i == len(height)-1:
            if j == len(height[0])-1:
                neighbour_map[(i, j)] = {(i, j - 1), (i - 1, j)}
            else:
                neighbour_map[(i, j)] = {(i, j + 1), (i, j - 1), (i - 1, j)}
        elif j == len(height[0])-1:
            neighbour_map[(i, j)] = {(i + 1, j), (i, j - 1), (i - 1, j)}
        else:
            neighbour_map[(i, j)] = {(i + 1, j), (i, j - 1), (i - 1, j), (i, j + 1)}
        if height[i][j] == 9:
            neighbour_map[(i, j)].clear()
            l.add((i, j))


for i in range(0, len(height)):
    for j in range(0, len(height[0])):
        neighbour_map[(i, j)] = neighbour_map[(i, j)] - l

#print(d)


def find_neigh(point):
    points = set()
    points.add(point)
    for n in neighbour_map[point]:
        if height[point[0]][point[1]] < height[n[0]][n[1]] < 9:
            points.update(find_neigh(n))
    return points

basins = []

for lp in low_points:
    basins.append(len(find_neigh(lp)))

basins = sorted(basins, reverse=True)

print(basins[0]*basins[1]*basins[2])












