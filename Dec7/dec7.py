import fileinput

lines = []
with open('input.txt') as f:
    pos = f.readline()
    pos = pos.split(',')
    pos = [int(x) for x in pos]


r = range(min(pos), max(pos)+1)
p1 = [0] * (max(pos)+1)

# PART I
for i in r:
    for p in range(0,len(pos)):
        p1[i] += abs(i-pos[p])

print(min(p1))

# PART II
p2 = [0] * (max(pos)+1)
for i in r:
    for p in range(0,len(pos)):
        p2[i] += (1+abs(i-pos[p]))*abs(i-pos[p])/2

print(min(p2))
