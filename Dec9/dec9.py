import fileinput
from itertools import islice

lines = []
with fileinput.input(files=('input.txt')) as f:
    for line in f:
        lines.append(line.strip())

height = []
for i in lines:
    height.append([int(x) for x in i])
final = 0

# PART I
low_points = []

def neighbors(row_number, column_number):
    n_list = []
    n_set = set()
    for j in range(column_number - 1, column_number + 2):
        for i in range(row_number - 1, row_number + 2):
            if i == row_number and j == column_number:
                pass
            elif (0 <= i < len(height)) and (0 <= j < len(height[0])) and not ((abs(i-row_number) == 1) and (abs(j-column_number) == 1)):
                n_list.append(height[i][j])
                n_set.add((i, j))
    return n_list, n_set


neighbour_map = dict()

for i in range(0, len(height)):
    for j in range(0, len(height[0])):
        [neigh, neigh_set] = neighbors(i, j)
        neighbour_map[(i, j)] = neigh_set
        lower = 0
        for n in neigh:
            if height[i][j] < n:
                lower += 1
        if lower == len(neigh):
            low_points.append((i, j))
            final += height[i][j] + 1

print('P1: The sum of the risk levels of all low points on your heightmap: ', final)

# PART II


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
print('P2: The product of the sizes of the three largest basins: ', basins[0] * basins[1] * basins[2])
