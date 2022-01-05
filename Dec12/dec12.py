import fileinput
import numpy as np

lines = []
with fileinput.input(files=('input.txt')) as f:
    for line in f:
        lines.append(line.strip())

lines = [elem.split('-') for elem in lines]

print(lines)
