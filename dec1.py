import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import fileinput
import itertools

# PART I
depths = []
with fileinput.input(files=('input.txt')) as f:
    for line in f:
        depths.append(int(line))

copy = []

for i in range(0,len(depths)):
    if i == 0:
        copy.append(None)
    elif depths[i] > depths[i-1]:
        copy.append(True)
    else:
        copy.append(False)

increase = copy.count(True)
#print(increase)

# PART II
df = pd.DataFrame(depths, columns = ['depths'])
#print(max(range(0,len(depths))))
sums = []

for i in range(0,len(depths)-2):
    sums.append(sum(depths[i:i+3]))

copy2 = []

for i in range(0,len(sums)):
    if i == 0:
        copy2.append(None)
    elif sums[i] > sums[i-1]:
        copy2.append(True)
    else:
        copy2.append(False)

increase2 = copy2.count(True)
print(increase2)