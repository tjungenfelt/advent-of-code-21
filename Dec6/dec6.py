import fileinput

lines = []
with open('input.txt') as f:
    pos = f.readline()
    pos = pos.split(',')
    pos = [int(x) for x in pos]
    
# PART I

d = dict()
for x in range(0, 9):
    d[x] = 0

for i in range(0, len(pos)):
    if pos[i] not in d:
        d[pos[i]] = 1
    else:
        d[pos[i]] += 1

part1 = d.copy()
part2 = d.copy()


def count_fish(d_fish, days):
    for day in range(0, days):
        z = d_fish[0]
        for x in range(1, 9):
            d_fish[x - 1] = d_fish[x]
        d_fish[8] = z
        d_fish[6] += z
    return sum(d_fish.values())

#def lanternfish(l, days):
#    for i in range(0, days):
#        if 0 in l:
#            for x in range(0, l.count(0)):
#                l.append(9)
#                l[l.index(0)] = 7
#        l = [x-1 for x in l]
#    return len(l)


print('How many lantern fish would there be after 80 days? ',  count_fish(part1, 80))

# PART II

print('How many lantern fish would there be after 256 days? ',  count_fish(part2, 256))











