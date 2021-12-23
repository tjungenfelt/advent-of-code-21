import pandas as pd


data = pd.read_csv('input2.txt', sep=' ', names=['direction', 'units'])
dl = data.values.tolist()

# PART I
pos = 0
depth = 0

for i in range(0, len(dl)):
    if dl[i][0] == "forward":
        pos += dl[i][1]
    elif dl[i][0] == "down":
        depth += dl[i][1]
    else:
        depth -= dl[i][1]

print("What do you get if you multiply your final horizontal position by your final depth? ", depth*pos)

# PART II

pos = 0
depth = 0
aim = 0

for j in range(0, len(dl)):
    if dl[j][0] == "forward":
        pos += dl[j][1]
        depth += aim*dl[j][1]
    elif dl[j][0] == "down":
        aim += dl[j][1]
    else:
        aim -= dl[j][1]

print("What do you get if you multiply your final horizontal position by your final depth? ", depth*pos)