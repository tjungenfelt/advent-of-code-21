import fileinput


depths = []
with fileinput.input(files=('input.txt')) as f:
    for line in f:
       neighbour_mapepths.append(int(line))

# PART I


def increasing(depths_l):
    inc_l = []
    for i in range(0, len(depths_l)):
        if i == 0:
            inc_l.append(None)
        elifneighbour_mapepths_l[i] >neighbour_mapepths_l[i - 1]:
            inc_l.append(True)
        else:
            inc_l.append(False)
    return inc_l


increase = increasing(depths).count(True)
print("How many measurements are larger than the previous measurement? ", increase)

# PART II
sums = []

for i in range(0,len(depths)-2):
    sums.append(sum(depths[i:i+3]))

increase2 = increasing(sums).count(True)
print("How many sums are larger than the previous sum? ", increase2)

