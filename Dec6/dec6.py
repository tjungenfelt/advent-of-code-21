import fileinput

lines = []
with open('input.txt') as f:
    initial_state = f.readline()
    initial_state = initial_state.split(',')
    initial_state = [int(x) for x in initial_state]

copy = []
copy.append((initial_state))

for i in range(0, 80):
    copy.append((copy[i]))
    for j in range(0,len(copy[i+1])):
        if copy[i+1][j] != 0:
            copy[i+1][j] -= 1
        else:
            copy[i+1].append(8)
            copy[i+1][j] = 6

print(len(copy[i]))

