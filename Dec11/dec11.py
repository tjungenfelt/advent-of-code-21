import fileinput
import numpy as np

lines = []
with fileinput.input(files=('input.txt')) as f:
    for line in f:
        lines.append(line.strip())

grid = np.array([list(map(int, r)) for r in lines])
flashes = 0


def neighbors(row_number, column_number):
    n_set = set()
    for j in range(column_number - 1, column_number + 2):
        for i in range(row_number - 1, row_number + 2):
            if i == row_number and j == column_number:
                pass
            elif (0 <= i < len(grid)) and (0 <= j < len(grid[0])):
                n_set.add((i, j))
    return n_set


def flashing(r, c, matrix):
    neigh = neighbors(r, c)
    for n in neigh:
        if matrix[n[0], n[1]] != 0:
            matrix[n[0], n[1]] += 1
    matrix[r][c] = 0
    return matrix

# PART I

for step in range(0, 100):
    grid += 1
    flashed = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] > 9]
    while flashed:
        for p in flashed:
            grid = flashing(p[0], p[1], grid)
        flashed = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] > 9]
    flashes += len([(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 0])

print("P1. How many total flashes are there after 100 steps? ", flashes)

# PART II

grid = np.array([list(map(int, r)) for r in lines])
steps = 0

while True:
    grid += 1
    steps += 1
    flashed = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] > 9]
    while flashed:
        for p in flashed:
            grid = flashing(p[0], p[1], grid)
        flashed = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] > 9]
    if len([(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 0]) == len(grid) * len(grid[0]):
        break

print("P2. What is the first step during which all octopuses flash? ", steps)
