import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import fileinput
import itertools


depths = []
with fileinput.input(files=('input2.txt')) as f:
    for line in f:
        depths.append(int(line))

print(depths)