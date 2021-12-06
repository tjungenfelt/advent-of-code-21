import pandas as pd
import numpy as np

data = pd.read_csv('input3.txt', names=['binary'], dtype=str)

# PART I
gamma = ""
eps = ""
for j in range(0, len(str((data['binary'][0])))):
    hej = 0
    for i in range(0, len(data['binary'])):
        hej += int(data['binary'][i][j])
    if hej/len(data['binary']) > (1/2):
        gamma = gamma+"1"
        eps = eps + "0"
    else:
        gamma = gamma+"0"
        eps = eps + "1"

print("What is the power consumption of the submarine? ", int(gamma, 2)*int(eps, 2))

# PART II
o2 = data
co2 = data


def most_common(df, col):
    df['bool'] = True
    hej = 0
    for i in range(0, len(df['binary'])):
        hej += int(df['binary'][i][col])
        if df['binary'][i][col] == "0":
            df.loc[i, 'bool'] = False
    if hej/len(df['binary']) >= (1/2):
        return df[df['bool']].reset_index(drop=True)
    else:
        return df[~df['bool']].reset_index(drop=True)


def least_common(df, col):
    df['bool'] = True
    hej = 0
    for i in range(0, len(df['binary'])):
        hej += int(df['binary'][i][col])
        if df['binary'][i][col] == "0":
            df.loc[i, 'bool'] = False
    if hej/len(df['binary']) >= (1/2):
        return df[~df['bool']].reset_index(drop=True)
    else:
        return df[df['bool']].reset_index(drop=True)


for j in range(0, len(str((o2['binary'][0])))):
    if len(o2['binary']) > 1:
        o2 = most_common(o2, j)

for j in range(0, len(str((co2['binary'][0])))):
    if len(co2['binary']) > 1:
        co2 = least_common(co2, j)

print("What is the life support rating of the submarine? ", int(o2['binary'][0], 2)*int(co2['binary'][0], 2))

