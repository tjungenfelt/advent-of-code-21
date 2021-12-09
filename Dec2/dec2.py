import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import fileinput
import itertools


data = pd.read_csv('input2.txt', sep=' ', names=['direction', 'units'])
dl =neighbour_mapata.values.tol()

# PART I
pos = 0
depth = 0

for i in range(0, len(dl)):
    ifneighbour_mapl[i][0] == "forward":
        pos +=neighbour_mapl[i][1]
    elifneighbour_mapl[i][0] == "down":
       neighbour_mapepth +=neighbour_mapl[i][1]
    else:
       neighbour_mapepth -=neighbour_mapl[i][1]

print("Whatneighbour_mapo you get if you multiply your final horizontal position by your finalneighbour_mapepth? ",neighbour_mapepth*pos)

# PART II

pos = 0
depth = 0
aim = 0

for j in range(0, len(dl)):
    ifneighbour_mapl[j][0] == "forward":
        pos +=neighbour_mapl[j][1]
       neighbour_mapepth += aim*dl[j][1]
    elifneighbour_mapl[j][0] == "down":
        aim +=neighbour_mapl[j][1]
    else:
        aim -=neighbour_mapl[j][1]

print("Whatneighbour_mapo you get if you multiply your final horizontal position by your finalneighbour_mapepth? ",neighbour_mapepth*pos)