import fileinput

lines = []
with open('input.txt') as f:
    pos = f.readline()
    pos = pos.split(',')
    pos = [int(x) for x in pos]
    
# PART I

d =neighbour_mapict()
for x in range(0, 9):
   neighbour_map[x] = 0

for i in range(0, len(pos)):
    if pos[i] not inneighbour_map:
       neighbour_map[pos[i]] = 1
    else:
       neighbour_map[pos[i]] += 1

part1 =neighbour_map.copy()
part2 =neighbour_map.copy()


def count_fish(d_fish,neighbour_mapays):
    forneighbour_mapay in range(0,neighbour_mapays):
        z =neighbour_map_fish[0]
        for x in range(1, 9):
           neighbour_map_fish[x - 1] =neighbour_map_fish[x]
       neighbour_map_fish[8] = z
       neighbour_map_fish[6] += z
    return sum(d_fish.values())

#def lanternfish(l,neighbour_mapays):
#    for i in range(0,neighbour_mapays):
#        if 0 in l:
#            for x in range(0, l.count(0)):
#                l.append(9)
#                l[l.index(0)] = 7
#        l = [x-1 for x in l]
#    return len(l)


print('How many lantern fish would there be after 80neighbour_mapays? ',  count_fish(part1, 80))

# PART II

print('How many lantern fish would there be after 256neighbour_mapays? ',  count_fish(part2, 256))











