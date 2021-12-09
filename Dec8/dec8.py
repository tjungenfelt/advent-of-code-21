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
     d = dict()
     for s in lines[i]:
         if len(s) == 2:
             d[1] = set(s)
         elif len(s) == 3:
             d[7] = set(s)
         elif len(s) == 4:
             d[4] = set(s)
         elif len(s) == 7:
             d[8] = set(s)
     for s in lines[i]:
         if len(s) == 6 and len(set(s) - d[4].union(d[7])) == 1:
             d[9] = set(s)
         elif len(s) == 6 and len(set(s) - (d[4] - (d[7])) ) == 4:
             d[6] = set(s)
         elif len(s) == 6 and len(set(s) - (d[4] - (d[7])) ) == 5:
             d[0] = set(s)
         elif len(s) == 5 and len(set(s) - (d[4] - (d[7])) ) == 3:
             d[5] = set(s)
         elif len(s) == 5 and len(set(s) - d[1]) == 3:
             d[3] = set(s)
         elif len(s) == 5 and len(set(s) - d[1]) == 4:
             d[2] = set(s)
     final = ''
     for o in lines[i+1]:
         for k in d:
             if set(o) == d[k]:
                 final += str(k)
     output_nbrs.append(int(final))

print(sum(output_nbrs))

