import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import fileinput
import itertools


data = pd.read_csv('input2.txt', sep=' ', names=['direction','units'])
dlist = data.values.tolist()

# PART I
pos = 0
depth = 0

for i in range(0, len(dlist)):
    if dlist[i][0] == "forward":
        pos += dlist[i][1]
    elif dlist[i][0] == "down":
        depth += dlist[i][1]
    else:
        depth -= dlist[i][1]

print("What do you get if you multiply your final horizontal position by your final depth? ", depth*pos)

# PART II

pos = 0
depth = 0
aim = 0

for j in range(0, len(dlist)):
    if dlist[j][0] == "forward":
        pos += dlist[j][1]
        depth += aim*dlist[j][1]
    elif dlist[j][0] == "down":
        aim += dlist[j][1]
    else:
        aim -= dlist[j][1]

print("What do you get if you multiply your final horizontal position by your final depth? ", depth*pos)