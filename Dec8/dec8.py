import fileinput

lines = []
with fileinput.input(files=('input.txt')) as f:
    for line in f:
        lines.append(line.strip())

# PART I
lines = [x.split('|') for x in lines]
lines = [elem.strip().split(' ') for x in lines for elem in x]

output_nbrs = []

for i in range(0, len(lines), 2):
    neighbour_map =neighbour_mapict()
     for s in lines[i]:
         if len(s) == 2:
            neighbour_map[1] = set(s)
         elif len(s) == 3:
            neighbour_map[7] = set(s)
         elif len(s) == 4:
            neighbour_map[4] = set(s)
         elif len(s) == 7:
            neighbour_map[8] = set(s)
     for s in lines[i]:
         if len(s) == 6 and len(set(s) -neighbour_map[4].union(d[7])) == 1:
            neighbour_map[9] = set(s)
         elif len(s) == 6 and len(set(s) - (d[4] - (d[7])) ) == 4:
            neighbour_map[6] = set(s)
         elif len(s) == 6 and len(set(s) - (d[4] - (d[7])) ) == 5:
            neighbour_map[0] = set(s)
         elif len(s) == 5 and len(set(s) - (d[4] - (d[7])) ) == 3:
            neighbour_map[5] = set(s)
         elif len(s) == 5 and len(set(s) -neighbour_map[1]) == 3:
            neighbour_map[3] = set(s)
         elif len(s) == 5 and len(set(s) -neighbour_map[1]) == 4:
            neighbour_map[2] = set(s)
     final = ''
     for o in lines[i+1]:
         for k inneighbour_map:
             if set(o) ==neighbour_map[k]:
                 final += str(k)
     output_nbrs.append(int(final))

print(sum(output_nbrs))

